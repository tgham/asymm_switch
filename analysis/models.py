import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy.io
from scipy.special import softmax
from tqdm.auto import tqdm
import warnings
import itertools
warnings.filterwarnings('ignore')


## RL model 
class TI_RL:
 
    def __init__(self, n_items):
        self.t = 0
        self.n_items = n_items


    def run(self, params, df_trials, model, model_set, fit, recovery = False):

        
        ## initialise model's internal variables
        self.n_items = int(np.nanmax(df_trials['Item_1']))
        self.n_trials = len(df_trials)
        self.Q = np.zeros((self.n_items)) 
        self.vdiff = np.zeros(self.n_trials)
        self.Qvals = np.zeros((self.n_trials,self.n_items)) 
        self.CP = np.zeros(self.n_trials) +0.5
        self.correctP = np.zeros(self.n_trials)+0.5
        self.ELO = np.zeros((self.n_trials))
        self.trial_loss = np.zeros(self.n_trials)
        self.cum_loss = np.zeros(self.n_trials)
        self.a1s = np.zeros(self.n_trials+1)
        self.a2s = np.zeros(self.n_trials+1)
        self.asymm = np.zeros(self.n_trials)
        self.pairs = np.array(list(itertools.combinations(np.arange(0,self.n_items), 2)))


        ## intitialise params
        self.base_LR = params[0]
        
        #Q-symm
        if model == 0:
            self.a1s[:] = params[0]
            self.a2s[:] = params[0]
            self.eta = params[1]
            self.tauI = params[2]
            if model_set == 1: ## i.e. 1 new pair of LRs after switch
                self.omi1 = params[-1]
                self.omi2 = params[-1]
            elif model_set == 2: ## i.e. 2 new pairs of LRs after switch
                self.omi1 = params[-2]
                self.omi2 = params[-1]
        


        #Q-asymm
        elif model == 1:
            self.a1s[:] = params[0]
            self.a2s[:] = params[1]
            self.eta = params[2]
            self.tauI = params[3]
            if model_set == 1: 
                self.omi1 = params[-1]
                self.omi2 = params[-1]
            elif model_set == 2: 
                self.omi1 = params[-2]
                self.omi2 = params[-1]

        #Q-adapt (entropy func)
        elif model == 2:
            self.a1s[:] = params[0]
            self.a2s[:] = 0
            self.eta = params[1]
            self.tauI = params[2] 
            if model_set == 1: 
                self.omi1 = params[-1]
                self.omi2 = params[-1]
            elif model_set == 2: 
                self.omi1 = params[-2]
                self.omi2 = params[-1]


        #Q-adapt (parameterised entropy func)
        elif model == 12:
            self.a1s[:] = params[0]
            self.a2s[:] = 0
            self.eta = params[1]
            self.tauI = params[2]
            self.meta = params[3]
            if model_set == 1: 
                self.omi1 = params[-1]
                self.omi2 = params[-1]
            elif model_set == 2: 
                self.omi1 = params[-2]
                self.omi2 = params[-1]
        

        #prevent error caused by division by tau=0
        if self.tauI == 0:
            self.tauI = np.finfo(float).tiny

        
        
        ## get trial info 

        # first trial of switch block
        self.switch = np.argwhere(df_trials['Switched'].to_numpy()=='post')[0].squeeze() 
        # self.switch = 1000

        #idx of TI trials
        self.TI_idx = np.where(df_trials['Feedback_on'] == 0)[0]


        ## trial loop
        for t in range(0,self.n_trials):


            #first, check whether the first (or second) switch trial was reached, in which case activate the new learning rates
            if model_set in (np.arange(1,3)) and t == self.switch:#df_trials['InverseFb'].argmax(): #df_trials['switched'].argmax():
                self.a1s[t-1:] = self.omi1
                self.a2s[t-1:] = self.omi2
            

            ## get info for current trial

            #item values  at trial t
            self.Qvals[t][:] = self.Q

            #get winner and loser of current trial
            current_trial = df_trials.iloc[t]
            loser = int(current_trial['Losing_Item'])-1
            winner = int(current_trial['Winning_Item'])-1

            ## CP (i.e. prob of choosing the winner)
            self.correctP[t] = self.sigmoid(self.Q[winner] - self.Q[loser], self.tauI)

            #flip probability to match how items were presented, so that CP = probability of choosing 2nd item (winner)
            if current_trial['Item_2'] == current_trial['Winning_Item']:
                self.CP[t] = self.correctP[t]
            elif current_trial['Item_2'] == current_trial['Losing_Item']:
                self.CP[t] = 1-self.correctP[t]
                

            ## Learning
            if (df_trials['Feedback_on'].iloc[t] == 1):

                ## difference-weighted updating
                self.vdiff[t] = (self.Q[winner] - self.Q[loser])*self.eta 

                # adaptive asymm, determined by choice entropy
                if model == 2:

                    self.asymm[t] = self.entropy(self.correctP[t])
                    
                    ## spread the overall LR resource over a1 and a2 according to the asymm
                    LRs = self.spread_LRs(self.base_LR, self.asymm[t])
                    self.a1s[t] = LRs[0]
                    self.a2s[t] = LRs[1]

                ## adapive asymm, determined by parameterised choice entropy
                elif model ==12:

                    self.asymm[t] = self.entropy_like(self.correctP[t], self.meta)

                    ## spread the overall LR resource over a1 and a2 according to the asymm
                    LRs = self.spread_LRs(self.base_LR, self.asymm[t])
                    self.a1s[t] = LRs[0]
                    self.a2s[t] = LRs[1]


                ## update winners and losers
                self.Q[winner] = self.Q[winner] + self.a1s[t]   * np.maximum(1 - self.vdiff[t] - self.Q[winner],0) #winner
                self.Q[loser] = self.Q[loser]   + self.a2s[t]   * np.minimum(-1 + self.vdiff[t] - self.Q[loser],0) #loser


        ## normalise Qvalues between 0 and 1
        self.Qvals = self.normalise(self.Qvals, -1, 1)
        # self.Qvals+=0.5
        
        ## convert model bhvr into binary choices
        self.m_choices = np.round(self.CP)
        self.m_chosen_item = np.where(self.m_choices==0, df_trials['Item_1'], df_trials['Item_2'])
        

        ##calculate loss and model evidence
        if fit == True:

            ## convert human choices to bool (0 if item 1 chosen, 1 if item 2 chosen)
            if recovery == False:
                self.p_choices = (df_trials['Chosen_Item'] == df_trials['Item_2']).to_numpy(dtype=bool)

            ## or, if fitting to a simulated dataset, use binomial choice probabilities from the generative model
            elif recovery == True:
                self.p_choices = df_trials['gen_choices'].to_numpy()

            self.loss_func()
            self.AIC = 2 * len(params) + self.loss
            self.BIC = np.log(self.n_trials) * len(params) + self.loss
        
        elif fit == False:
            self.loss = []

        return self.loss


    def loss_func(self):
        
        #fix CP = 1 or CP = 0 to avoid log(1/0) = inf
        self.CP[(self.CP==0) & (self.p_choices)]  = 0 + np.finfo(float).tiny
        self.CP[(self.CP==1) & (~self.p_choices)] = 1 - np.finfo(float).eps

        
        ## loss for trials where P answered 1, then for 0
        self.trial_loss[self.p_choices>=0.5] = 2 * np.log(1.0/self.CP[self.p_choices>=0.5])
        self.trial_loss[~self.p_choices>=0.5] = 2 * np.log(1.0/(1-self.CP[~self.p_choices>=0.5]))

        ## sum loss for all trials
        self.loss = np.sum(self.trial_loss)

        ## sum loss only for TI trials
        # self.loss = np.sum(self.trial_loss[self.TI_idx])

        ## cumulative loss
        self.cum_loss = np.cumsum(self.trial_loss)


    def sigmoid(self, x, tau, b = 0):
        prob = 1/(1 + np.exp(-x/tau)) - b
        return prob
    
    def entropy(self, p):
        entropy = -p*np.log2(p) - (1-p)*np.log2(1-p)
        if np.isnan(entropy):
            entropy = 0
        return entropy
    
    def entropy_like(self,p,b):
        entropy = -4*b*p**2 + 4*b*p +1-b
        return entropy
    
    def spread_LRs(self, x, b):
        y1 = x * (1+b)/2
        y2 = x * (1-b)/2
        return [y1, y2] + np.abs(np.min([x,0]))


    def pseudo_r_sq(self, evidence_model, n_t, free):
        n_t = int(n_t)
        # choices_null = np.ones((n_t),dtype=bool)
        CP_null = np.ones((n_t))*0.5

        # loss and evidence under null (random choice) (adjust appropriately if using BIC instead of AIC)
        loss_null = np.sum(2*np.log(1/CP_null))
        evidence_null = np.log(n_t) * free + loss_null

        # calculate pseudo R2
        ratio = (evidence_model/ evidence_null)
        if ratio>1: #prevent rounding error
            ratio=1
            print
        pR_2 = 1 - ratio

        return pR_2
    
    def normalise(self, x, min_val, max_val):
        y = (x - np.min(x)) / (np.max(x) - np.min(x)) * (max_val - min_val) + min_val
        return y 

    

    ## simulating function
    def simulate(self, all_data, model, model_set, current_model, participants, full_params, fit = True, recovery = False):


        #add a new column for simulated performance in the big dataframe containing participant data
        all_data['CP '+current_model] = np.zeros(len(all_data))
        all_data['asymm '+current_model] = np.zeros(len(all_data))
        all_data['a1 '+current_model] = np.zeros(len(all_data))
        all_data['a2 '+current_model] = np.zeros(len(all_data))
        all_data['Accuracy '+current_model] = np.zeros(len(all_data))
        all_data[current_model+'_Chosen_Item'] = np.zeros(len(all_data))
        all_data['trial loss '+current_model] = np.zeros(len(all_data))
        all_data['cum loss '+current_model] = np.zeros(len(all_data))


        #create new columns for Q values of each item, and pairP of each pair, and CP assoc w each item
        for Q in range(self.n_items):
            all_data[current_model + ' item ' + str(Q+1)] = np.zeros(len(all_data))
            all_data['Item_'+str(Q+1)+'_chosen_'+current_model] = np.zeros(len(all_data)) + np.nan

        
        
        ## loop through participants
        for p_n in tqdm(range(len(participants))):
            p = participants[p_n]

            ## get trials, params and then run
            df_trials = all_data[(all_data['Participant'] == p)] # & (all_data['Block'] <= 6)
            params = full_params[p_n]
            self.run(params, df_trials, model, model_set, fit, recovery)

            
            # add output from simulationback to the original participant dataframe
            all_data.loc[all_data['Participant'] == p,'CP '+current_model] = self.CP
            all_data.loc[all_data['Participant'] == p,'asymm '+current_model] = self.asymm
            all_data.loc[all_data['Participant'] == p,'Accuracy '+current_model] = self.correctP
            all_data.loc[all_data['Participant'] == p,current_model+'_Chosen_Item'] = self.m_chosen_item
            all_data.loc[all_data['Participant'] == p,'trial loss '+current_model] = self.trial_loss
            for Q in range(self.n_items):
                all_data.loc[all_data['Participant'] == p,current_model + ' item ' + str(Q+1)] = self.Qvals[:,Q]
                
        ## add some more columns for the choice matrix plotting
        all_data['Largest_CP_'+current_model] = np.zeros(len(all_data))
        all_data['Smallest_CP_'+current_model] = np.zeros(len(all_data))
        all_data['Largest_CP_'+current_model].loc[all_data['Item_2'] == all_data['Largest_number']] = all_data['CP '+current_model].loc[all_data['Item_2'] == all_data['Largest_number']]
        all_data['Smallest_CP_'+current_model].loc[all_data['Item_2'] == all_data['Smallest_number']] = all_data['CP '+current_model].loc[all_data['Item_2'] == all_data['Smallest_number']]
        all_data['Largest_CP_'+current_model].loc[all_data['Item_2'] == all_data['Smallest_number']] = 1-all_data['CP '+current_model].loc[all_data['Item_2'] == all_data['Smallest_number']]
        all_data['Smallest_CP_'+current_model].loc[all_data['Item_2'] == all_data['Largest_number']] = 1-all_data['CP '+current_model].loc[all_data['Item_2'] == all_data['Largest_number']]

        ## record CP for each item
        for i in range(1,self.n_items+1):
            all_data.loc[all_data['Item_1']==i, 'Item_'+str(i)+'_chosen_'+current_model] = 1-(all_data.loc[all_data['Item_1']==i, 'CP '+current_model])
            all_data.loc[all_data['Item_2']==i, 'Item_'+str(i)+'_chosen_'+current_model] = all_data.loc[all_data['Item_2']==i, 'CP '+current_model]

        return all_data, params
    

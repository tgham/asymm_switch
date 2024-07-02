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
    





## SMC model
class TI_SMC:
    
    def __init__(self,
                n_items = 7):   
        
        ## initialisation

        #useful bits
        self.n_particles = 100
        self.n_items = n_items
        self.t = 0
        self.init_mu = 0
        self.init_var = 1
        self.init_kappa = 100

        #determine SMC version
        self.version = 'normal'
        # self.version = 'log_normal'


    ## model behaviour

    #state process (Gaussian walk)
    def g_walk(self, xp, t, init = False): 
        
        
        #x is normally distributed
        if (self.version == 'normal'):
            if init == True:
                dist = np.random.normal(loc=self.init_mu, scale=np.sqrt(self.init_var),
                                size=(self.n_particles, self.n_items))
                    
            else:
                noise = np.random.randn(self.n_particles, self.n_items)*np.sqrt(self.evo_var)
                dist = xp + noise
                
        
        #x is log normally distributed 
        elif self.version == 'log_normal':

            if init == True:
                self.init_var = 1
                self.init_mu = 0
                
                ## normal
                # dist = np.random.normal(loc=self.init_mu, scale=np.sqrt(self.init_var),
                #                 size=(self.n_particles, self.n_items))
                
                ## log normal
                dist = np.random.lognormal(mean=self.init_mu, sigma = np.sqrt(self.init_var), 
                                            size=(self.n_particles,self.n_items)) 
                # dist = (np.random.normal(loc = self.init_mu, scale = np.sqrt(self.init_var), size = (self.n_particles, self.n_items))**self.kappa)
                # dist *= -1
                
                ## truncated version
                # mu = self.init_mu
                # sigma = np.sqrt(self.init_var)
                # dist = scipy.stats.truncnorm.rvs((0 - mu) / sigma, (np.inf - mu) / sigma, loc=mu, scale=sigma, size = (self.n_particles, self.n_items))

            else:
                
                ## original log normal drift
                # noise = np.random.randn(self.n_particles, self.n_items)* np.sqrt(self.evo_var)
                # dist = -np.exp(np.log(-1*xp) + noise)
                dist =  np.random.lognormal(mean=np.log(xp), sigma = np.sqrt(self.evo_var),
                                            size=(self.n_particles,self.n_items))

                ## parameterised log normal drift
                # noise = np.random.randn(self.n_particles, self.n_items)* np.sqrt(self.evo_var)
                # dist = self.kappa**(((np.emath.logn(self.kappa, -xp)) + noise))
                # dist = np.random.normal(loc = (-1*xp)**(1/self.kappa), scale = np.sqrt(self.evo_var), size = (self.n_particles, self.n_items))
                # dist *= -1
                # dist = dist**self.kappa

                ## boxcox drift
                # dist = self.inv_boxcox(self.boxcox(xp, self.kappa) + noise, self.kappa)

                ## log normal drift in proportion to CP?
                # noise = np.random.normal(0, self.evo_var*(1-self.CP_corr_weighted[t-1]),
                #                             size=(self.n_particles,self.n_items))
                # dist = np.exp(np.log(xp) + noise)


                ## normal drift with increasing SD
                # sigma = np.sqrt(np.mean(xp,0)*self.evo_var)
                # sigma = np.sqrt(self.evo_var)
                # dist = np.random.normal(loc = xp, scale = sigma, size = (self.n_particles, self.n_items))

                ## normal drift, determined by previous trial's CP
                # dist = np.abs(np.random.normal(loc = xp, scale = self.evo_var*(1-self.CP_corr_weighted[t-1]), size = (self.n_particles, self.n_items)))
                
                ## truncate the log of xp so that all values are positive
                # sig = np.mean(np.emath.logn(self.kappa, xp),0)
                # # trunc_log = np.abs(np.log(xp))
                # # sigma = np.sqrt(np.mean(trunc_log,0)*self.evo_var)
                # # min = 0
                # # max = 1
                # # sig = (sig - np.min(sig)) / (np.max(sig) - np.min(sig)) * (max - min) + min
                # sigma = self.evo_var
                # # sigma = (1-self.CP_corr_weighted[t-1])
                # dist = self.kappa**(np.random.normal(loc = np.emath.logn(self.kappa, xp), scale = sigma, size = (self.n_particles, self.n_items)))
                
                ## truncated version
                # mu = xp
                # sigma = np.sqrt(self.evo_var)
                # sigma = self.evo_var*np.mean(xp,0)
                # sigma = (np.mean(xp,0)**(1-self.coef)) * self.evo_var

                # coef = self.item_KL[t-1]/self.item_KL[t-1].sum()
                # coef = coef/coef.sum()
                # if np.isnan(coef.sum()):
                #     coef =0.2
                # sigma = coef 

                # dist = scipy.stats.truncnorm.rvs((0 - mu) / sigma, (np.inf - mu) / sigma, loc=mu, scale=sigma, size = (self.n_particles, self.n_items))

                ## gamma
                # shape = 0.5
                # scale = 2
                # noise = np.random.gamma(shape, scale, size = (self.n_particles, self.n_items))
                # noise -= np.median(noise,0)
                # dist = xp + noise
                
                ## gamma+norm
                # dist = np.random.normal(loc = xp, scale = np.sqrt(self.evo_var), size = (self.n_particles, self.n_items)) #gamma
                # dist += np.random.gamma(shape = 1, scale = 0.5, size = (self.n_particles, self.n_items))
                
                ## skewed ND
                # dist = scipy.stats.skewnorm.rvs(a = -0.1, loc = xp, scale = self.evo_var, size = (self.n_particles, self.n_items)) 


                
        return dist


    #model makes choice
    def choice(self,  t, loser, winner): 

        #get the particle estimates for the losing (loser) and winning (winner) items
        x_loser = (self.particles[t+1,:,loser])
        x_winner = (self.particles[t+1,:,winner])
        
        #if using Weber scaling, get max item for each pair of compared particles and divide the difference between xi and xj by this
        if self.version == 'log_normal':
            scaler = 1
            CP_corr = self.sigmoid((x_winner - x_loser), self.beta, scaler) 

        elif (self.version == 'normal'):
            # scaler=1
            # CP_corr = self.sigmoid((x_winner)-(x_loser), self.beta, scaler) 

            ## calculate diff between each particle estimate k for the winner and every other particle j of the loser
            diff = x_winner[:,np.newaxis] - x_loser[np.newaxis,:]

            ## calculate CP for each pair of particles
            CP_corr = self.sigmoid(diff, self.beta,1)
            

        # clip??
        # CP_corr = np.clip(CP_corr, 0.000001, 1)

        return CP_corr


    ## weights

    #entire weight update step
    def weight_update(self, t, CP_corr, winner, loser):
        # CP_corr[(CP_corr==0)] = 0 + np.finfo(float).tiny #(avoid log(0) = -inf error) 
        # self.w_update[t] = np.log(CP_corr)
        # self.w_log[t+1,:] = self.norm_w_log[t,:] + np.log(CP_corr) #use CP_correct to update log weights
        # self.wgts[t+1,:] = np.exp(self.w_log[t+1,:]) #unlog the unnormalised wgts for normalisation and ESS calcs
        # self.norm_w[t+1,:] = self.wgts[t+1,:]/np.sum(self.wgts[t+1,:]) #normalise...
        # self.norm_w[t+1, self.norm_w[t+1,:]==0] = 0 + np.finfo(float).tiny #(avoid log(0) = -inf error) 
        # self.norm_w_log[t+1,:] = np.log(self.norm_w[t+1,:]) #...then log
        self.norm_w[t+1,:,:] = self.norm_w[t,:,:]
        winner_w = self.norm_w[t,:,winner]
        loser_w = self.norm_w[t,:,loser]
        self.norm_w[t+1,:,winner] = winner_w * np.sum(winner_w[:,np.newaxis]*CP_corr,1)
        self.norm_w[t+1,:,loser] = loser_w * np.sum(loser_w[:,np.newaxis]*(1-CP_corr),1)
        self.norm_w[t+1,:,winner] = self.norm_w[t+1,:,winner]/np.sum(self.norm_w[t+1,:,winner])
        self.norm_w[t+1,:,loser] = self.norm_w[t+1,:,loser]/np.sum(self.norm_w[t+1,:,loser])

        # CP_corr[(CP_corr==0)] = 0 + np.finfo(float).tiny #(avoid log(0) = -inf error) 
        # self.w_update[t] = np.log(CP_corr)
        # self.w_log[t+1,:] = self.norm_w_log[t,:] + np.log(CP_corr) #use CP_correct to update log weights
        # self.wgts[t+1,:] = np.exp(self.w_log[t+1,:]) #unlog the unnormalised wgts for normalisation and ESS calcs
        # self.norm_w[t+1,:] = self.wgts[t+1,:]/np.sum(self.wgts[t+1,:]) #normalise...
        # self.norm_w[t+1, self.norm_w[t+1,:]==0] = 0 + np.finfo(float).tiny #(avoid log(0) = -inf error) 
        # self.norm_w_log[t+1,:] = np.log(self.norm_w[t+1,:]) #...then log

    ## resampling
    def resample_move(self, t, winner, loser):
        
        #resample with replacement
        self.ESS[t] = 1/np.sum(self.norm_w[t+1,:]**2) #calculate new ESS
        if self.ESS[t] < (self.ESSrmin * self.n_particles): 
            # self.wtf.append(self.norm_w[t+1,:])
            self.rs[t] = 1

            #sample particles proportional to their weight
            rs_weights = self.wgts[t+1,:]/(self.wgts[t+1,:].sum(0))
            # rs_weights = self.soft_temp(self.w_log[t+1,:], tau = 1)
            aa = np.random.choice(np.arange(0,self.n_particles), self.n_particles, p = rs_weights)
            self.particles[t+1,:,:] = self.particles[t+1,aa,:]

            #randomly index a limited number of low-weight particles and replace with uniformly distributed particles
            # n_reset = int(self.n_particles*self.KL[t])
            # n_reset = int(self.n_particles*(1-self.CP_corr_weighted[t]))
            # n_reset = int(self.n_particles*0.001)
            # w_inv = self.wgts[t+1,:]/(self.wgts[t+1,:].sum(0))
            # w_inv /= w_inv.sum()
            # bb = np.random.choice(np.arange(0,self.n_particles), n_reset)
            # self.particles[t+1,bb,:] = np.random.uniform(0, np.max(self.particles[t+1,:,:]), size = (n_reset, self.n_items))

            #renormalise
            self.norm_w[t+1,:] = 1/self.n_particles
            self.norm_w_log[t+1,:] = np.log(self.norm_w[t+1,:])
            # self.respawn(t, winner, loser)
            
        else:
            self.rs[t] = 0
            
        
    #weights remain the same on non-adj trials
    def no_learning(self,t):
        # self.w_log[t+1,:] = self.w_log[t,:]
        # self.norm_w[t+1,:] = self.norm_w[t,:]
        # self.norm_w_log[t+1,:] = self.norm_w_log[t,:]
        # self.wgts[t+1,:] = self.wgts[t,:]
        # self.ESS[t+1] = self.ESS[t]
    
        self.norm_w[t+1,:,:] = self.norm_w[t,:,:]

    ## calculate hierarchy update index 
    def KL_div(self, t, winner, loser):

        # for each pair
        KL = []
        obj_k = []
        winner_KL = []
        loser_KL = []
        for pair in self.pairs:

            # get p(i<j) according to weights before and after the update, using weighted average
            # CP_corr = self.choice(t, pair[0], pair[1])
            # pre_CP_corr = np.average(CP_corr, weights = self.norm_w_log[t])
            # post_CP_corr = np.average(CP_corr, weights = self.norm_w_log[t+1])
            
            # get p(i<j) according to weights before and after the update, weighting each CP indiviually
            CP_corr = self.choice(t, pair[0], pair[1])
            pre_CP_corr = np.average(CP_corr, weights = self.norm_w_log[t]) 
            # pre_CP_corr = CP_corr * self.norm_w_log[t]
            # pre_CP_corr = pre_CP_corr/np.sum(pre_CP_corr)

            post_CP_corr = np.average(CP_corr, weights = self.norm_w_log[t+1]) 
            # post_CP_corr = CP_corr * self.norm_w_log[t+1]
            # post_CP_corr = post_CP_corr/np.sum(post_CP_corr)

            # calculate KL divergence between the two, and also with the reverse (i.e. the KL divergence of p(j<i) before and after feedback)
            KL1 = post_CP_corr * np.log(post_CP_corr/pre_CP_corr)
            KL2 = (1-post_CP_corr) * np.log((1-post_CP_corr)/(1-pre_CP_corr))
            KL1 = np.nansum(KL1)
            KL2 = np.nansum(KL2)

            # sum divergences
            KL.append(KL1 + KL2)

            # add KL to big matrix
            self.item_KL[t, pair[0]] += KL1 + KL2
            self.item_KL[t, pair[1]] += KL1 + KL2
            
           # trial-by-trial change in objective knowledge
            # if t > self.switch:
            #     idx1 = self.post_gtr[self.dir][pair[0]]
            #     idx2 = self.post_gtr[self.dir][pair[1]]
            #     if idx1 > idx2:
            #         CP_corr = self.choice(t, pair[1], pair[0])
            # obj_k.append(np.log(np.sum(CP_corr)) - np.log(self.n_particles))





        # sum across all pairs
        self.KL[t] = np.sum(self.item_KL[t])/2
        # self.obj_k[t] = np.sum(obj_k)


    def knowledge(self,t,winner,loser):
        for pair in self.pairs:
            CP = np.average(self.choice(t, pair[0], pair[1]), weights = self.norm_w_log[t+1])
            self.subj_k[t, pair[0]] += np.abs(CP-0.5)
            self.subj_k[t, pair[1]] += np.abs(CP-0.5)
        self.relative_k = (1-self.normalise(self.subj_k[t],0.001,1))



    #respawn according to the KL divergence for the winner and loser
    def respawn(self, t, winner, loser):
        # n_reset_winner = int(self.n_particles*(1-self.CP_corr_weighted[t]))
        # n_reset_loser = int(self.n_particles*(1-self.CP_corr_weighted[t]))
        n_reset_winner = int(self.n_particles*self.winner_KL[t]/self.KL[t])
        n_reset_loser = int(self.n_particles*self.loser_KL[t]/self.KL[t])
        w_inv = self.wgts[t+1,:]/(self.wgts[t+1,:].sum(0))
        w_inv /= w_inv.sum()
        aa_w = np.random.choice(np.arange(0,self.n_particles), n_reset_winner, replace = False)
        aa_l = np.random.choice(np.arange(0,self.n_particles), n_reset_loser, replace = False)
        self.particles[t+1,aa_w,winner] = self.inv_boxcox(np.random.uniform(np.min(self.boxcox(self.particles[t+1,:,:],self.kappa)), np.max(self.boxcox(self.particles[t+1,:,:], self.kappa)), size = n_reset_winner), self.kappa)
        self.particles[t+1,aa_l,loser] = self.inv_boxcox(np.random.uniform(np.min(self.boxcox(self.particles[t+1,:,:], self.kappa)), np.max(self.boxcox(self.particles[t+1,:,:], self.kappa)), size = n_reset_loser), self.kappa)


    def boxcox(self, x, lmbda):
        if lmbda == 0:
            return np.log(x)
        else:
            return (x**lmbda - 1)/lmbda
        
    def inv_boxcox(self, x, lmbda):
        if lmbda == 0:
            return np.exp(x)
        else:
            return (x*lmbda + 1)**(1/lmbda)
        
    def stefan(self, x, kappa):
        # eps=1e-10
        # return (x/(np.abs(x) + eps)) * (np.abs(x)**kappa)
        return np.abs(x)**kappa
    
    def logg(self, x, kappa):
        return np.exp(np.log(x)**kappa)
    
    def soft_temp(self, x, tau=1):
        exp_x = np.exp(x / tau)  # Subtracting np.max(x / tau) for numerical stability
        return exp_x / exp_x.sum(0, keepdims=True)
    
    def normalise(self, x, min_val, max_val):
        y = (x - np.min(x)) / (np.max(x) - np.min(x)) * (max_val - min_val) + min_val
        return y 
    
    

    #run simulation
    def run(self, params, df_trials, fit = True):
        self.n_trials = len(df_trials)


        ## initialisation
        # np.random.seed(seed)

        #params
        # self.version = version
        self.beta = params[0]
        self.evo_var = params[1]
        self.kappa = params[2]
        self.coef = self.kappa
        # self.coef = params[3]
        # self.coef = 0.5
    
        # self.ESSrmin = params[2]
        self.ESSrmin = 0.99
        # self.ESSrmin = params[-1]
        # self.prior = params[4]
        self.prior = 0.1
        # self.evo_var = params[1]
        # self.weber = params[2]
        self.weber = 1

        #trial info
        self.switch = np.argwhere(df_trials['Switched'].to_numpy()=='post')[0].squeeze()
        self.n_items = int(np.nanmax(df_trials['Item_1']))
        self.pairs = np.array(list(itertools.combinations(np.arange(0,self.n_items), 2)))

        #particles
        self.particles = np.zeros((self.n_trials+1, self.n_particles, self.n_items)) #+1 because particles + weights need to be initialised at t=0
        self.particles[0,:,:] = self.g_walk(xp = self.init_mu, t=0, init = True) #initial Gaussian or log Gaussian

        #weights 
        # self.norm_w = np.ones((self.n_trials+1, self.n_particles))/self.n_particles
        # self.w_log = np.copy(self.norm_w) #for some reason?
        # self.norm_w_log = np.log(self.norm_w)
        # self.wgts = np.zeros((self.n_trials+1, self.n_particles))
        # self.w_update = np.zeros((self.n_trials, self.n_particles))
        self.norm_w = np.ones((self.n_trials+1, self.n_particles, self.n_items))/self.n_particles
        self.w_log = np.copy(self.norm_w) #for some reason?
        self.norm_w_log = np.log(self.norm_w)
        self.wgts = np.zeros((self.n_trials+1, self.n_particles, self.n_items))
        self.w_update = np.zeros((self.n_trials, self.n_particles, self.n_items))
        
        #NLL
        self.trial_loss = np.zeros(self.n_trials)
        self.cum_loss = np.zeros(self.n_trials)
        self.trial_NLL = np.zeros(self.n_trials)
        self.cum_NLL = np.zeros(self.n_trials)
        self.kumaran = np.zeros(self.n_trials)

        #resampling
        self.ESS = np.zeros(self.n_trials)
        self.rs = np.zeros(self.n_trials)


        #model behaviour
        self.CP = np.zeros((self.n_trials, self.n_particles)) +0.5
        self.CP_corr = self.CP.copy()
        self.CP_weighted = np.zeros(self.n_trials)
        self.CP_corr_weighted = np.zeros(self.n_trials)
        self.KL = np.zeros(self.n_trials)
        self.item_KL = np.zeros((self.n_trials, self.n_items))
        self.loser_KL = np.zeros(self.n_trials)
        self.winner_KL = np.zeros(self.n_trials)
        self.subj_k = np.zeros((self.n_trials, self.n_items))
        self.obj_k = np.zeros(self.n_trials)
        self.rels = np.zeros((self.n_trials, self.n_items))
        self.rel_weight = np.zeros(self.n_trials)
        self.spread_cost = np.zeros((self.n_trials, self.n_particles))
        self.particle_mean = np.zeros((self.n_trials, self.n_items))
        self.ratio = np.zeros(self.n_trials)
        self.entropy = np.zeros(self.n_trials)
        # self.reliability[0] = 0.5

        #groundtruths
        self.post_gtr = {}
        self.post_gtr['down'] = [6,0,1,2,3,4,5]
        self.post_gtr['up'] = [1,2,3,4,5,6,0]
        self.dir = df_trials['Direction'].iloc[0]


        ## trial loop
        for t in range(0,self.n_trials):

            #gaussian walk
            self.particles[t+1,:,:] = self.g_walk(xp = self.particles[t,:,:], t=t)
            self.particle_mean[t,:] = np.mean(self.particles[t+1,:,:],0)

            #sort items in ascending order
            current_trial = df_trials.iloc[t]
            loser = int(current_trial['Losing_Item'])-1
            winner = int(current_trial['Winning_Item'])-1

            #model choice 
            CP_corr_tmp = self.choice(t, loser, winner)

            ## get the outer product of the currently relevant weights
            w_ws = self.norm_w[t, :,winner]
            l_ws = self.norm_w[t, :,loser]
            outer_w = np.outer(w_ws, l_ws)

            ## computed weighted sum of probs 
            # print(CP_corr_tmp.shape, outer_w.shape)
            self.CP_weighted[t] = np.sum(CP_corr_tmp * outer_w) / np.sum(outer_w)
            # self.CP_corr[t] = CP_corr_tmp

            ##flip p(correct) to match how items were presented, so that CP = probability of choosing 2nd item (winner)

            #linear
            # if current_trial['Item_2'] == current_trial['Winning_Item']:
            #     self.CP[t] = CP_corr_tmp
            # elif current_trial['Item_2'] == current_trial['Losing_Item']:
            #     self.CP[t] = 1-CP_corr_tmp


            ## straightforward mean of p(choice)
            # self.CP_weighted[t] = np.mean(self.CP[t]) 

            ## weighted average of p(choice)
            # self.CP_weighted[t] = np.average(self.CP[t], weights = self.norm_w_log[t]) 

            ## entropy
            # p = np.average(CP_corr_tmp, weights = self.norm_w_log[t])
            # self.entropy[t] = -p*np.log(p) - (1-p)*np.log(1-p)
            
            
            ## convert this weighted CP back into p(correct)
            if current_trial['Item_2'] == current_trial['Winning_Item']:
                self.CP_corr_weighted[t] = self.CP_weighted[t]
            elif current_trial['Item_2'] == current_trial['Losing_Item']:
                self.CP_corr_weighted[t] = 1-self.CP_weighted[t]
            
            
            ## learning

            #weight update on adj trials
            feedback = df_trials['Feedback_on'].iloc[t]
            if feedback == 1:
                # self.weight_update(t, CP_corr_tmp)
                self.weight_update(t, CP_corr_tmp,winner,loser)
            
                #calculate hierarchy update index using KL divergence
                # self.KL_div(t, winner, loser)
            

            #weights remain the same on non-adj trials
            else:
                self.no_learning(t)
            # self.knowledge(t, winner, loser)

            
            #resampling
            # self.resample_move(t, winner, loser)

        ##calculate loss
        if fit == True:
            try:
                self.p_choices = (df_trials['Chosen_Item'] == df_trials['Item_2']).to_numpy() #i.e. 1 when winner chosen, 0 when loser chosen
            except:
                self.p_choices = df_trials['gen_choices'].to_numpy(dtype=bool)
            self.loss_func()
            self.AIC = 2 * len(params) + self.loss
            self.BIC = np.log(self.n_trials) * len(params) + self.loss
        else:
            self.loss = []
            self.NLL = []

        ##convert model's CP into binary choices
        self.m_choices = np.round(self.CP)

        # return self.loss
        return self.NLL

    


    def loss_func(self):

        #calculate average CP for each trial
        # self.CP_ave = np.mean(self.CP, axis=1)
        
        #fix CP = 1 or CP = 0 to avoid log(1/0) = inf
        # self.CP[(self.CP==0)]  = 0 + np.finfo(float).tiny
        # self.CP[(self.CP==1)] = 1 - np.finfo(float).eps
        # self.CP_ave[(self.CP_ave==0) & (self.p_choices)]  = 0 + np.finfo(float).tiny
        # self.CP_ave[(self.CP_ave==1) & (~self.p_choices)] = 1 - np.finfo(float).eps

        ## calculate loss (in this case, chi^2)
        # self.trial_loss[self.p_choices] = 2 * np.log(1.0/self.CP_ave[self.p_choices])
        # self.trial_loss[~self.p_choices] = 2 * np.log(1.0/(1-self.CP_ave[~self.p_choices]))
        # self.trial_loss[self.p_choices] = np.log(np.sum(self.CP[self.p_choices],axis=1)) - np.log(self.n_particles)
        # self.trial_loss[~self.p_choices] = np.log(np.sum(1-self.CP[~self.p_choices],axis=1)) - np.log(self.n_particles)
        # self.loss = -2*np.sum(self.trial_loss)
        # self.cum_loss = np.cumsum(self.trial_loss)


        ## Kumaran 1
        # self.trial_NLL[self.p_choices] = 2 * np.log(1.0/self.CP_weighted[self.p_choices])
        # self.trial_NLL[~self.p_choices] = 2 * np.log(1.0/(1-self.CP_weighted[~self.p_choices]))
        # self.NLL = np.sum(self.trial_NLL)
        # self.cum_NLL = np.cumsum(self.trial_NLL)

        #use the weighted loss
        # self.loss = self.NLL


        ## Kumaran 2
        self.kumaran[self.p_choices] = np.sum(np.exp(self.norm_w_log[:-1][self.p_choices] + np.log(self.CP[self.p_choices])),1) ## this effectively gives a p(x|params) for each trial, which can then be averaged across simulations and logged to give a log likelihood
        self.kumaran[~self.p_choices] = np.sum(np.exp(self.norm_w_log[:-1][~self.p_choices] + np.log(1-self.CP[~self.p_choices])),1)
        self.trial_NLL[self.p_choices] = scipy.special.logsumexp(self.norm_w_log[:-1][self.p_choices] + np.log(self.CP[self.p_choices]), axis=1)
        self.trial_NLL[~self.p_choices] = scipy.special.logsumexp(self.norm_w_log[:-1][~self.p_choices] + np.log(1-self.CP[~self.p_choices]), axis=1)
        self.NLL = -2*np.sum(self.trial_NLL)
        self.cum_NLL = np.cumsum(self.trial_NLL)
        self.loss = self.NLL


        # CP_tmp = self.CP[t]
        # CP_tmp[CP_tmp==0] = 0 + np.finfo(float).tiny #(avoid log(0) = -inf error) 
        # self.NLL[t] = scipy.special.logsumexp(self.norm_w_log[t] + np.log(CP_tmp))

        #loss for trials where P answered 1, then for 0


    def sigmoid(self, x, beta, scaler):
        return 1/(1+ np.exp(-beta*(x/scaler))) #i.e. if using Weber scaling, xi-xj is scaled by max(xi, xj)
        # return 1/(1+ np.exp(-self.beta*(x/scaler))) #i.e. if using Weber scaling, xi-xj is scaled by max(xi, xj)

    def cdf(self, x, sigma):
        return 1-scipy.stats.norm.cdf(0, loc=x, scale=sigma)
    
    
    ## simulating function
    def simulate(self, all_data, current_model, participants, full_params, n_iter = 1, log = False, fit = True):

        # seed=1
        
        #add a new column for simulated performance in the big dataframe containing participant data
        all_data['CP '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['Accuracy '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['choices '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['trial loss '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['cum loss '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['ESS '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['KL '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['obj k '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['rel weight '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['spread cost '+current_model] = np.zeros(len(all_data))+np.nan
        all_data['entropy '+current_model] = np.zeros(len(all_data))+np.nan
        re_fit = {}
        re_fit['Participant'] = []
        re_fit['loss'] = []
        re_fit['BIC'] = []
        for particle in range(self.n_items):
            all_data['Particle ' + str(particle+1) + ' ' + current_model] = np.zeros(len(all_data)) + np.nan
            all_data['Item KL ' + str(particle+1) + ' ' + current_model] = np.zeros(len(all_data)) + np.nan
        
        #loop through participants
        for p_n in tqdm(range(len(participants))):
            p = participants[p_n]
            df_trials = all_data[(all_data['Participant'] == p)]  #& (all_data['Block'] <= 6)
            params = full_params[p_n]

            ## run the model over n_iterations to allow for stochasticity in the model
            big_CP = []
            CP = []
            CP_corr_weighted = []
            CP_weighted = []
            loss = [] 
            trial_loss = []
            cum_loss = []
            particles = []
            ESS = []
            KL = []
            item_KL = []
            rel_weight = []
            spread_cost = []
            entropy = []
            kumaran = []
            # obj_k = []

            for i in range(n_iter):
                self.run(params, df_trials, fit)
                big_CP.append(self.CP)
                CP.append(np.mean(self.CP, axis=1))
                CP_corr_weighted.append(self.CP_corr_weighted)
                CP_weighted.append(self.CP_weighted)
                trial_loss.append(self.trial_loss)
                cum_loss.append(self.cum_loss)
                loss.append(self.loss)
                particles.append(self.particles)
                ESS.append(self.ESS)
                KL.append(self.KL)
                item_KL.append(self.item_KL)
                rel_weight.append(self.rel_weight)
                spread_cost.append(self.spread_cost)
                entropy.append(self.entropy)
                kumaran.append(self.kumaran)
                # obj_k.append(self.obj_k)

                
            ## get the iteration with the smallest lost
            # idx = loss.index(min(loss))
            # loss_tmp = loss[idx]
            # CP_tmp = CP[idx]
            # CP_corr_weighted_tmp = CP_corr_weighted[idx]
            # CP_weighted_tmp = CP_weighted[idx]
            # particles_tmp = particles[idx]
            # ESS_tmp = ESS[idx]
            # KL_tmp = KL[idx]
            # obj_k_tmp = obj_k[idx]

            ## alternatively, average over all iterations
            trial_loss_tmp = np.mean(trial_loss, 0)
            cum_loss_tmp = np.mean(cum_loss, 0)
            loss_tmp = np.mean(loss)
            big_CP_tmp = np.mean(np.array(big_CP), 0)
            CP_tmp = np.mean(np.array(CP), 0)
            CP_corr_weighted_tmp = np.mean(np.array(CP_corr_weighted), 0)
            CP_weighted_tmp = np.mean(np.array(CP_weighted), 0)
            particles_tmp = np.mean(np.array(particles),0)
            ESS_tmp = np.mean(np.array(ESS),0)
            KL_tmp = np.mean(np.array(KL),0)
            item_KL_tmp = np.mean(np.array(item_KL),0)
            rel_weight_tmp = np.mean(np.array(rel_weight),0)
            spread_cost_tmp = np.mean(np.mean(np.array(spread_cost),0),1)
            entropy_tmp = np.mean(np.array(entropy),0)
            kumaran_tmp = -2*np.sum(np.log(np.mean(np.array(kumaran),0)))
            print(loss_tmp,kumaran_tmp)

            
            # add simulated bhvr back to the original participant dataframe
            all_data.loc[all_data['Participant'] == p,'CP '+current_model] = CP_tmp
            all_data.loc[all_data['Participant'] == p,'Accuracy '+current_model] = CP_corr_weighted_tmp
            all_data.loc[all_data['Participant'] == p,'ESS '+current_model] = ESS_tmp
            all_data.loc[all_data['Participant'] == p,'KL '+current_model] = KL_tmp
            all_data.loc[all_data['Participant'] == p,'trial loss '+current_model] = trial_loss_tmp
            all_data.loc[all_data['Participant'] == p,'cum loss '+current_model] = cum_loss_tmp
            all_data.loc[all_data['Participant'] == p,'rel weight '+current_model] = rel_weight_tmp
            all_data.loc[all_data['Participant'] == p,'spread cost '+current_model] = spread_cost_tmp
            all_data.loc[all_data['Participant'] == p,'entropy '+current_model] = entropy_tmp
            # all_data.loc[all_data['Participant'] == p,'obj k '+current_model] = obj_k_tmp
            for particle in range(self.n_items):
                all_data.loc[all_data['Participant'] == p,'Item KL ' + str(particle+1) + ' ' + current_model] = item_KL_tmp[:,particle]
                if log == False:
                    all_data.loc[all_data['Participant'] == p,'Particle '+str(particle+1) + ' ' +current_model] = np.nanmean(particles_tmp[1:,:,particle], axis= 1)
                elif log == True:
                    all_data.loc[all_data['Participant'] == p,'Particle '+str(particle+1) + ' ' +current_model] = np.nanmean(np.log(particles_tmp[1:,:,particle]), axis= 1)
            all_data.loc[all_data['Participant'] == p,'choices '+current_model] = CP_weighted_tmp.round()

            ## save re-fit
            re_fit['Participant'].append(p)
            re_fit['loss'].append(kumaran_tmp)
            self.BIC = np.log(self.n_trials) * len(params) + kumaran_tmp
            re_fit['BIC'].append(self.BIC)
            

            # ## re-calculate loss using the average CPs over all simulations
            # self.CP = big_CP_tmp
            # self.loss_func()
            # print(loss_tmp, self.loss)


        re_fit = pd.DataFrame.from_dict(re_fit).sort_values(
            by='Participant', ignore_index=True)
        


        
        return all_data, re_fit
        # return all_data, params



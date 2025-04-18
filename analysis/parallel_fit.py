# %% [markdown]
# ## Imports 

# %%
# Imports
import time
import random
import numpy as np
from numpy import nan
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv
import math
import scipy.stats as stats
import scipy.io
from scipy.special import softmax
from functools import partial
from scipy.optimize import Bounds, minimize
import itertools
from tqdm.auto import tqdm
import pickle
import multiprocess as mp
from models import TI_RL
from helpers import *
import importlib
import warnings
from model_init import *
warnings.filterwarnings('ignore')


## Load data
dataset = 'euro_move_data'
all_data = pd.read_csv('../../data/'+dataset)


### get some useful counts

#expt info
directions = ['down', 'up']
n_items = int(np.nanmax(all_data['Item_1']))
blocks = all_data['Block'].unique().astype('int')
n_blocks = len(blocks)
n_trials_per_b = all_data.loc[all_data['Block']==1, 'Trial'].nunique()
b_starts = []
half_b_starts = []
for b in blocks:
    start = all_data.loc[all_data['Block']==b]['Trial'].iloc[0]
    b_starts.append(start)
    half_b_starts.append(start)
    half_b_starts.append(start + n_trials_per_b/2)

#participants
participants = all_data['Participant'].unique()
participants.sort()
n_participants = len(participants)
print('pre-excl n_participants = ',n_participants)
print('pre-excl down:',len(all_data.loc[all_data['Direction']=='down','Participant'].unique()))
print('pre-excl up:',len(all_data.loc[all_data['Direction']=='up','Participant'].unique()))
excl_correct = dict.fromkeys(participants)
excl_prob = dict.fromkeys(participants)
excl_nans = dict.fromkeys(participants)


### implement exclusion criteria

##calculate the probability that participants were performing at chance in pre-switch trials
prob_thresh = 0.01
for p in participants:
    correct = np.nansum(all_data[
        (all_data['Participant']==p) 
        &(all_data['Switched']=='pre')
        &(all_data['Accuracy human'].notna())
        ]['Accuracy human'])
    ntrials = len(all_data[
        (all_data['Participant']==p) 
        &(all_data['Switched']=='pre')
        &(all_data['Accuracy human'].notna())
        ])
    excl_correct[p] = correct/ntrials
    excl_prob[p] = 1-stats.binom.cdf(correct, ntrials, 0.5)
    excl_nans[p] = all_data.loc[all_data['Participant']==p, 'Accuracy human'].isna().sum()

##binom method: identify Ps for whom the probability of performing at chance on trials of interest is below the threshold
inc_ps_prob = [p for p, prob in excl_prob.items() if prob<=prob_thresh] 

##identify participants with excessive nans
inc_ps_nans = [p for p, nans in excl_nans.items() if nans<=161]

##exclude
inc_ps = list(set(inc_ps_prob) & set(inc_ps_nans))
# all_data = all_data[all_data['Participant'].isin(inc_ps)]``

#remove nan trials
all_data = all_data[all_data['Accuracy human'].notna()]

## useful (post-cleaning) counts
n_participants = all_data['Participant'].nunique()
n_trials = all_data['Trial'].nunique()
print('post-excl n_participants = ',n_participants)
participants = all_data['Participant'].unique()
down_participants = all_data.loc[all_data['Direction']=='down','Participant'].unique()
up_participants = all_data.loc[all_data['Direction']=='up','Participant'].unique()
down_participants.sort()
up_participants.sort()
all_participants = [down_participants, up_participants]
print()
print('down:',len(down_participants))
print('up:',len(up_participants))

## for each condition, sort participants according to a median split of their TI accuracy post-switch
grouped_down = all_data.loc[(all_data['Direction']=='down') 
                            & (all_data['Feedback_on'] == 0) 
                            & (all_data['Item_1'].isin(np.arange(2,n_items))) 
                            & (all_data['Item_2'].isin(np.arange(2,n_items))) 
                            & (all_data['Switched']=='post')
                            ].groupby('Participant').mean('Accuracy human')[['Accuracy human']]
grouped_up = all_data.loc[(all_data['Direction']=='up') 
                          & (all_data['Feedback_on'] == 0) 
                          & (all_data['Item_1'].isin(np.arange(2,n_items))) 
                          & (all_data['Item_2'].isin(np.arange(2,n_items)))
                          & (all_data['Switched']=='post')
                          ].groupby('Participant').mean('Accuracy human')[['Accuracy human']]

good_down = list(grouped_down.loc[grouped_down['Accuracy human'] >= grouped_down['Accuracy human'].quantile()].index)
bad_down = list(grouped_down.loc[grouped_down['Accuracy human'] < grouped_down['Accuracy human'].quantile()].index)
good_up = list(grouped_up.loc[grouped_up['Accuracy human'] >= grouped_up['Accuracy human'].quantile()].index)
bad_up = list(grouped_up.loc[grouped_up['Accuracy human'] < grouped_up['Accuracy human'].quantile()].index)
good_ps = good_down + good_up
bad_ps = bad_down + bad_up


## identify pairs as low, med or high valued
all_data = pair_value(all_data, 'Item')

## calculate the combined value of each trial
all_data['Combined_value'] = np.zeros(len(all_data))
all_data['Combined_value'] = all_data[['Item_1','Item_2']].sum(1)

## record P's choices as 1s or 0s depending on whether they did or did not choose item_2 (useful for later modelling)
all_data['human_chosen_I2'] = (all_data['Item_2'] == all_data['Chosen_Item']).astype(float)

## record trials where each item was chosen
for i in range(1,8):
    all_data['Item_'+str(i)+'_chosen_human'] = np.zeros(len(all_data)) + np.nan
    all_data.loc[all_data['Item_1']==i, 'Item_'+str(i)+'_chosen_human'] = (all_data.loc[all_data['Item_1']==i, 'Chosen_Item'] == i).astype(float)
    all_data.loc[all_data['Item_2']==i, 'Item_'+str(i)+'_chosen_human'] = (all_data.loc[all_data['Item_2']==i, 'Chosen_Item'] == i).astype(float)


## add some more useful columns for the choice matrix plotting
all_data['Smallest_number'] = all_data[['Item_1','Item_2']].min(axis=1).astype(int)
all_data['Largest_number'] = all_data[['Item_1','Item_2']].max(axis=1).astype(int)
all_data['Smallest_chosen_human'] = (all_data['Chosen_Item'] == all_data['Smallest_number']).astype(int)
all_data['Largest_chosen_human'] = (all_data['Chosen_Item'] == all_data['Largest_number']).astype(int)



### initialise everything for the fit
model_type = 'RL'
parallel = 1


# fit which participants?
fit_participants = participants
n_fit_participants = len(fit_participants)


## callback for parallelised fitting
def append_fit(fit_out):
    fitting_data[current_model]['Participant'].extend(fit_out['Participant'])
    fitting_data[current_model]['Direction'].extend(fit_out['Direction'])
    fitting_data[current_model]['loss'].extend(fit_out['loss'])
    fitting_data[current_model]['n_trials'].extend(fit_out['n_trials'])
    fitting_data[current_model]['success'].extend(fit_out['success'])
    fitting_data[current_model]['nfev'].extend(fit_out['nfev'])
    fitting_data[current_model]['nit'].extend(fit_out['nit'])
    # if len(fit_out['params']) == 1:
    #     fit_out['params'] = [fit_out['params']]
    for i_fit_out in range(len(fit_out['params'])):
        for pa, par in enumerate(current_params):
            fitting_data[current_model][par].append(fit_out['params'][i_fit_out][pa]) 
            fitting_data[current_model][par+'_0'].append(fit_out['x0s'][i_fit_out][pa])

    ## update progress bar
    pbar.update(1)
    

## initialise fitting dictionaries
fitting_data = {}
df_fits = {}

## Loop through models
# for model_set in range(1):
for model_set in [0,1,2]:
    for m in [0,1,2,3]: 
        if model_type == 'RL':
            current_model = all_models[model_set][m]
            current_params = all_params[param_idx[model_set][m]]
        

        ## initilialise dict
        print('model: ', current_model, ', params: ', current_params)
        fitting_data[current_model] = {
            'Participant': [],
            'Direction': [],
            'loss': [],
            'n_trials': [],
            'success': [],
            'nfev': [],
            'nit': []
        }
        for param in all_params:
            fitting_data[current_model][param] = []
            fitting_data[current_model][param+'_0'] = []
    
        if model_type == 'RL':
    
            ## index only those params required by the current model

            #single initial points
            # x0s = np.expand_dims(all_params_0[param_idx[model_set][m]],0)

            #multiple initial points
            x0s = [set_0 for i_set_0, set_0 in enumerate(all_x0s) if i_set_0 in param_idx[model_set][m]]

            # get bounds
            ub = all_ub[param_idx[model_set][m]]
            lb = all_lb[param_idx[model_set][m]]

        x0s = list(itertools.product(*x0s))
        print('n x0s = ',len(x0s))
        print(x0s)

        #add smallest floating point to lb==0 to avoid division by 0 error
        lb[lb==0] = np.finfo(float).tiny

        ## set bounds
        bounds = Bounds(lb,ub)

        print('bounds:', bounds)



        ## begin fitting loop

        #unparallelised:
        if parallel ==0:
            print("beginning serial fit with ",mini,', n_p = ',len(fit_participants))
            for p_n in tqdm(range(0,len(fit_participants))):
                p = fit_participants[p_n]
                df_trials = all_data[(all_data['Participant'] == p)
                                    #     &(all_data['Switched']=='pre')
                                    # &((all_data['Block']<4 )| ((all_data['Block']==4) & (all_data['Item_distance']<n_items-1)))
                                        ]
                fit_out = fit_model(m,model_set, df_trials, p, x0s, bounds, mini, minimize_method_opts, model_type, True, False)
                
                # consolidate p's data 
                fitting_data[current_model]['Participant'].extend(fit_out['Participant'])
                fitting_data[current_model]['Direction'].extend(fit_out['Direction'])
                fitting_data[current_model]['loss'].extend(fit_out['loss'])
                fitting_data[current_model]['n_trials'].extend(fit_out['n_trials'])
                fitting_data[current_model]['success'].extend(fit_out['success'])
                fitting_data[current_model]['nfev'].extend(fit_out['nfev'])
                fitting_data[current_model]['nit'].extend(fit_out['nit'])
                print(fit_out)

                for i_fit_out in range(len(fit_out['params'])):
                    for pa, par in enumerate(current_params):
                        fitting_data[current_model][par].append(fit_out['params'][i_fit_out][pa]) 
                        fitting_data[current_model][par+'_0'].append(fit_out['x0s'][i_fit_out][pa])


        #parallelised
        elif parallel ==1:

            #start pool
            n_cores = 20
            pool = mp.Pool(np.min([n_participants, n_cores]))
            print("beginning parallel fit with ",mini,', n_p = ',len(fit_participants))

            #fit to multiple participants at once
            if __name__ == '__main__':
                pbar = tqdm(total = n_fit_participants)
                fit_out = [pool.apply_async(fit_model, args = (m,model_set, all_data[(all_data['Participant'] == p)
                                                                                    #  &(all_data['Switched']=='pre')   #NB  UNCOMMENT THESE LINES TO FIT ONLY PRE-SWITCH TRIALS
                                                                                    # &((all_data['Block']<4 )| ((all_data['Block']==4) & (all_data['Item_distance']<n_items-1)))
                                                                                     ], p, x0s, bounds, mini, minimize_method_opts, model_type, True, False), callback=append_fit) for p in fit_participants]
                pool.close()
                pool.join()

        #remove empty keys (e.g. for params not used by the current model)
        del_keys = []
        for key in fitting_data[current_model].keys():
            if not bool(fitting_data[current_model][key]):
                del_keys.append(key)

        for dk in del_keys:
            fitting_data[current_model].pop(dk)
    
        df_fits[current_model] = pd.DataFrame.from_dict(fitting_data[current_model])

        ## print mean of model evidence
        print('mean loss = ',np.mean(df_fits[current_model]['loss']))
        AIC = 2*len(current_params) + df_fits[current_model]['loss'].to_numpy()
        print('mean AIC = ',np.mean(AIC))

        #save
        with open('useful_saves/move/fits/RL_revisions.pkl', 'wb') as f:
            pickle.dump(df_fits,f)
            print('done!')
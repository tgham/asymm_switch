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
import seaborn as sns
import multiprocess as mp
from models import TI_RL, TI_SMC, TI_Remerge
# import plotter
from helpers import *
from model_init import *
import importlib
import warnings
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
all_data = all_data[all_data['Participant'].isin(inc_ps)]

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
parallel = 1
fit_participants = participants
n_fit_participants = len(fit_participants)
model_type = 'RL'

## initialise settings of the trials to be generated
switch_block = 4
n_runs = 10
switch_type = 'move'
to_move = 1
move_to = n_items
switches = np.array(([to_move-1, move_to-1],
                  [move_to-1, to_move-1]))
directions = ['up', 'down']


## callbacks for parallelised fitting
def append_model_recovery(fit_out):
    fitting_recovery[gen_model][fitted_model]['Participant'].extend(fit_out['Participant'])
    fitting_recovery[gen_model][fitted_model]['Direction'].extend(fit_out['Direction'])
    fitting_recovery[gen_model][fitted_model]['loss'].extend(fit_out['loss'])
    fitting_recovery[gen_model][fitted_model]['n_trials'].extend(fit_out['n_trials'])
    fitting_recovery[gen_model][fitted_model]['nfev'].extend(fit_out['nfev'])
    fitting_recovery[gen_model][fitted_model]['nit'].extend(fit_out['nit'])
    for i_fit_out in range(len(fit_out['params'])):
        for pa, par in enumerate(current_params):
            fitting_recovery[gen_model][fitted_model][par].append(fit_out['params'][i_fit_out][pa]) 
            fitting_recovery[gen_model][fitted_model][par+'_0'].append(fit_out['x0s'][i_fit_out][pa])
            
    ## update progress bar
    pbar.update(1)

def append_param_recovery(fit_out):
    fitting_param[current_model]['Participant'].extend(fit_out['Participant'])
    fitting_param[current_model]['Direction'].extend(fit_out['Direction'])
    fitting_param[current_model]['loss'].extend(fit_out['loss'])
    fitting_param[current_model]['n_trials'].extend(fit_out['n_trials'])
    fitting_param[current_model]['nfev'].extend(fit_out['nfev'])
    fitting_param[current_model]['nit'].extend(fit_out['nit'])
    for i_fit_out in range(len(fit_out['params'])):
        for pa, par in enumerate(current_params):
            fitting_param[current_model][par].append(fit_out['params'][i_fit_out][pa]) 
            fitting_param[current_model][par+'_0'].append(fit_out['x0s'][i_fit_out][pa])
            fitting_param[current_model]['gen_'+par].append(fit_out['gen_'+par])

    ## update progress bar
    pbar.update(1)

## load empirical fits
with open('useful_saves/move/fits/RL_entropy_relu.pkl', 'rb') as f:
    df_fits_big = pickle.load(f)
moi = [
    'Q-symm','Q-asymm',
    'Q-adapt'
        ]
rm_models = []
df_fits = best_x0(df_fits_big, moi)
for key in df_fits.keys():
    if key not in moi:
        rm_models.append(key)
        pass
    else:
        df_fits[key] = df_fits[key].loc[df_fits[key]['Participant'].isin(participants)]
df_fits = rename_models(df_fits)
moi = df_fits.keys()
print(moi)
print()



## set the object of recovery
recover = 'model'
# recover = 'param'


### model recovery

## model recovery
if recover == 'model':
    print('model recovery')

    ## initialise the whole gamut of dataframes and dictionaries
    df_recovery = {}
    fitting_recovery = {}
    gen_trials= {}
    tmp = {}
    for gen_m_s in range(1):
        for gen_m in [0,1,12]:
            gen_model = all_models[gen_m_s][gen_m]
            fitting_recovery[gen_model] = {}
            gen_trials[gen_model] = pd.DataFrame()
            df_recovery[gen_model] = {}
            for fit_m_s in range(1):
                for fit_m in [0,1,12]:
                    fitted_model = all_models[fit_m_s][fit_m]
                    current_params = all_params[param_idx[fit_m_s][fit_m]]
                    fitting_recovery[gen_model][fitted_model] = {
                        'Participant': [],
                        'Simulated Participant': [],
                        'Sim_ID': [],
                        'Direction': [],
                        'loss': [],
                        'n_trials': [],
                        'nfev': [],
                        'nit': [],
                    }
                    for param in current_params:
                        fitting_recovery[gen_model][fitted_model][param] = []
                        fitting_recovery[gen_model][fitted_model][param+'_0'] = []
                        

    ## loop through generative models
    for gen_m_s in range(1):
        for gen_m in [0,1,12]:
            gen_model = all_models[gen_m_s][gen_m]

            ## Loop through participants to get full generative dataset
            print('generating '+str(n_runs)+' datasets, for each of '+str(n_fit_participants)+' participants, under ', gen_model)
            for p_n in tqdm(range(n_fit_participants)):
                p = fit_participants[p_n]

                ## get param estimates for gen model + participant
                params = df_fits[gen_model].loc[df_fits[gen_model]['Participant']==p][model_params[gen_model]].to_numpy().squeeze()


                ## generate n_runs datasets under the current generative model and parameter setting
                for sim_p in range(n_runs):
                    
                    ## get trial sequence experienced by that human participant
                    recovery_trials = all_data.loc[all_data['Participant'] == p]

                    ## generate choices under the current generative model and parameter setting
                    RL = TI_RL(n_items)
                    RL.run(params, recovery_trials, gen_m, gen_m_s, fit = False, recovery = True)

                    ## add choices back to the trial df, representing them as the value of the chosen item
                    recovery_trials['Model_Choice'] = RL.m_choices
                    recovery_trials['Model_Chosen_Item'] = np.zeros(len(recovery_trials))
                    recovery_trials.loc[recovery_trials['Model_Choice'] == 0, 'Model_Chosen_Item'] = recovery_trials.loc[recovery_trials['Model_Choice'] == 0, 'Item_1']
                    recovery_trials.loc[recovery_trials['Model_Choice'] == 1, 'Model_Chosen_Item'] = recovery_trials.loc[recovery_trials['Model_Choice'] == 1, 'Item_2']

                    ## or, convert model choice probabilities into binary choices
                    recovery_trials['gen_choices'] = np.random.binomial(1, RL.CP)

                    ## save the ID of the simulation (i.e. the participant whose params we used, and the run number)
                    recovery_trials['Simulated Participant'] = np.zeros(len(recovery_trials))
                    recovery_trials['Simulated Participant'] = sim_p
                    recovery_trials['Sim_ID'] = np.zeros(len(recovery_trials))
                    recovery_trials['Sim_ID'] = 'p'+str(p)+'_sim'+str(sim_p)


                    ## save simulated trials
                    gen_trials[gen_model] = pd.concat((gen_trials[gen_model], recovery_trials))
                        
    # save sequence
    with open('useful_saves/move/recovery/'+str(n_runs)+'_runs_per_p_trials_final.pkl', 'wb') as f:
        pickle.dump(gen_trials, f)


    # ## or just load existing set of generated trials
    # print('loading gen trials...')
    # with open('useful_saves/move/recovery/'+str(n_runs)+'_runs_per_p_trials_d.pkl', 'rb') as f:
    #     gen_trials = pd.read_pickle(f)
    # print('loading complete')
    # print(gen_trials.keys())

    ## whittle down to the 83 post-excl participants
    for key in gen_trials.keys():
        gen_trials[key] = gen_trials[key].loc[gen_trials[key]['Participant'].isin(participants)]

    ## add back in the data-generating parameters...
    # for gen_model in moi:
    #     current_params = model_params[gen_model]
    #     for par in current_params:
    #         gen_trials[gen_model]['gen_'+par] = np.zeros(len(gen_trials[gen_model]))
    #         for p in participants:
    #             gen_trials[gen_model].loc[gen_trials[gen_model]['Participant']==p, 'gen_'+par] = df_fits[gen_model].loc[df_fits[gen_model]['Participant']==p][par].to_numpy().squeeze()


    ### model recovery loop

    ## for each generative model
    for gen_m_s in range(1):
        for gen_m in [0,1,12]:
            gen_model = all_models[gen_m_s][gen_m]

            ## get sim_IDs for later looping
            sim_IDs = gen_trials[gen_model]['Sim_ID'].unique()
            n_simulations = len(sim_IDs)


            ## Fit each model to the simulated choice data
            for fit_m_s in range(1):
                for fit_m in [0,1,12]:

                    ## get fitting model's param settings
                    fitted_model = all_models[fit_m_s][fit_m]
                    current_params = all_params[param_idx[fit_m_s][fit_m]]
                    x0s = [set_0 for i_set_0, set_0 in enumerate(all_x0s) if i_set_0 in param_idx[fit_m_s][fit_m]]
                    x0s = list(itertools.product(*x0s))
                    ub = all_ub[param_idx[fit_m_s][fit_m]]
                    lb = all_lb[param_idx[fit_m_s][fit_m]]
                    lb[lb==0] = np.finfo(float).tiny
                    bounds = Bounds(lb,ub)
                    print('current params',current_params)
                    print('x0s: ',x0s)
                    print('bounds: ',bounds)
                    print('fitting ', fitted_model, ' to ', gen_model)

                    ## unparallelised
                    if parallel == 0:
                        print("beginning serial fit with ",mini,', n_simulations = ',n_simulations)
                        for sim_p_n in tqdm(range(0,n_simulations)):
                            sim_ID = sim_IDs[sim_p_n]
                            df_trials = gen_trials[gen_model].loc[gen_trials[gen_model]['Sim_ID'] == sim_ID]
                            fit = True
                            recovery = True
                            fit_out = fit_model(fit_m,fit_m_s, current_params, df_trials, sim_ID, x0s, bounds, mini, minimize_method_opts, model_type, fit, recovery)
                            
                            # consolidate p's data 
                            fitting_recovery[gen_model][fitted_model]['Participant'].extend(fit_out['Participant'])
                            fitting_recovery[gen_model][fitted_model]['Direction'].extend(fit_out['Direction'])
                            fitting_recovery[gen_model][fitted_model]['loss'].extend(fit_out['loss'])
                            fitting_recovery[gen_model][fitted_model]['n_trials'].extend(fit_out['n_trials'])
                            fitting_recovery[gen_model][fitted_model]['nfev'].extend(fit_out['nfev'])
                            fitting_recovery[gen_model][fitted_model]['nit'].extend(fit_out['nit'])
                            print(fit_out)

                            for i_fit_out in range(len(fit_out['params'])):
                                for pa, par in enumerate(current_params):
                                    fitting_recovery[gen_model][fitted_model][par].append(fit_out['params'][i_fit_out][pa]) 
                                    fitting_recovery[gen_model][fitted_model][par+'_0'].append(fit_out['x0s'][i_fit_out][pa])


                    ## parallelised
                    elif parallel == 1:
                        
                        ## start pool
                        n_cores = 30
                        pool = mp.Pool(np.min([n_simulations, n_cores]))
                        print("beginning parallel fit with ",mini,', n_simulations = ',n_simulations, ', n_cores = ', n_cores)
                        fit = True
                        recovery = True

                        ## fit to multiple participants at once
                        if __name__ == '__main__':
                            pbar = tqdm(total = n_simulations)
                            fit_out = [pool.apply_async(fit_model, args = (fit_m, fit_m_s, current_params, gen_trials[gen_model].loc[(gen_trials[gen_model]['Sim_ID'] == sim_ID)
                                                                                        #  &(gen_trials[gen_model]['Switched']=='pre')
                                                                                        # &((gen_trials[gen_model]['Block']<4 )| ((gen_trials[gen_model]['Block']==4) & (gen_trials[gen_model]['Item_distance']<n_items-1)))
                                                                                        ]
                            , sim_ID, x0s, bounds, mini, minimize_method_opts, model_type, fit, recovery), callback=append_model_recovery) for sim_ID in sim_IDs]
                            pool.close()
                            pool.join()

                    ## remove empty keys (e.g. for params not used by the current model)
                    del_keys = []
                    for key in fitting_recovery[gen_model][fitted_model].keys():
                        if not bool(fitting_recovery[gen_model][fitted_model][key]):
                            del_keys.append(key)
                    for dk in del_keys:
                        fitting_recovery[gen_model][fitted_model].pop(dk)

                    ## save dictionary as df
                    df_recovery[gen_model][fitted_model] = pd.DataFrame.from_dict(fitting_recovery[gen_model][fitted_model])
                    with open('useful_saves/move/recovery/'+str(n_runs)+'_runs_per_p_fits_again.pkl', 'wb') as f:
                        pickle.dump(df_recovery, f)





## param recovery
elif recover == 'param':
    
    ## initialise the whole gamut of dataframes for the recovery
    print('param recovery')
    print()
    df_param = {}
    fitting_param = {}
    gen_trials= {}
    tmp = {}
    for gen_m_s in range(1):
        for gen_m in [1,12]: # i.e. just Q-asymm, Q-adapt
            gen_model = all_models[gen_m_s][gen_m] ## unlike in the model recovery, the generative model is also the fitted model
            fitting_param[gen_model] = {}
            gen_trials[gen_model] = pd.DataFrame()
            current_params = model_params[gen_model]
            df_param[gen_model] = pd.DataFrame()
            fitting_param[gen_model] = {
                'Participant': [],
                'Simulated Participant': [],
                'Sim_ID': [],
                'Direction': [],
                'loss': [],
                'n_trials': [],
                'nfev': [],
                'nit': [],
            }
            for param in current_params:
                fitting_param[gen_model][param] = []
                fitting_param[gen_model][param+'_0'] = []
                fitting_param[gen_model]['gen_'+param] = []

    ## define param bounds
    n_steps = 10
    base = np.finfo(float).tiny
    param_iters = {
        'Q-asymm':{
            'a1': np.linspace(base,0.5, n_steps),
            'a2': np.linspace(base,0.5, n_steps),
            'eta': np.linspace(base,10, n_steps),
            'tauI': np.linspace(base,1, n_steps)
        },
        'Q-adapt':{
            'a0': np.linspace(-0.5,0.5, n_steps),
            'eta': np.linspace(base,10, n_steps),
            'tauI': np.linspace(base,1, n_steps),
            'meta': np.linspace(base,1, n_steps)

        }
    }


    ## generate data under each generative model
    for gen_m_s in range(1):
        for gen_m in [1,12]:
            gen_model = all_models[gen_m_s][gen_m]
            print('generating data under ', gen_model)

            ## loop through participants
            for p_n in tqdm(range(n_fit_participants)):
                p = fit_participants[p_n]
                
                ## get param estimates for gen model + participant
                current_params = model_params[gen_model]
                params = df_fits[gen_model].loc[df_fits[gen_model]['Participant']==p][current_params].to_numpy().squeeze()

                ## iteratively adjust each parameter
                for pi, param in enumerate(current_params):
                    current_param_iters = param_iters[gen_model][param]
                    for pii, param_i in enumerate(current_param_iters):
                        params_tmp = params.copy()
                        params_tmp[pi] = param_i
                        
                        ## get trial sequence experienced by that human participant
                        recovery_trials = all_data.loc[all_data['Participant'] == p]

                        ## generate choices under the current generative model and parameter setting
                        RL = TI_RL(n_items)
                        RL.run(params_tmp, recovery_trials, gen_m, gen_m_s, fit = False, recovery = True)

                        ## add choices back to the trial df, representing them as the value of the chosen item
                        recovery_trials['Model_Choice'] = RL.m_choices
                        recovery_trials['Model_Chosen_Item'] = np.zeros(len(recovery_trials))
                        recovery_trials.loc[recovery_trials['Model_Choice'] == 0, 'Model_Chosen_Item'] = recovery_trials.loc[recovery_trials['Model_Choice'] == 0, 'Item_1']
                        recovery_trials.loc[recovery_trials['Model_Choice'] == 1, 'Model_Chosen_Item'] = recovery_trials.loc[recovery_trials['Model_Choice'] == 1, 'Item_2']

                        ## or, convert model choice probabilities into binary choices
                        recovery_trials['gen_choices'] = np.random.binomial(1, RL.CP)

                        ## save the ID of the simulation (i.e. the participant whose params we used, and the run number)
                        recovery_trials['Sim_ID'] = np.zeros(len(recovery_trials))
                        recovery_trials['Sim_ID'] = 'p'+str(p)+'_'+param+'_'+str(pii)

                        ## save the data-generating params
                        for piii, par in enumerate(params_tmp):
                            recovery_trials['gen_'+current_params[piii]] = np.zeros(len(recovery_trials))
                            recovery_trials['gen_'+current_params[piii]] = par


                        ## save simulated trials
                        gen_trials[gen_model] = pd.concat((gen_trials[gen_model], recovery_trials))
                    

    # save sequence
    with open('useful_saves/move/recovery/param_recovery_trials_'+str(n_steps)+'_steps_relu.pkl', 'wb') as f:
        pickle.dump(gen_trials, f)

    ## or, just load an existing dataset
    # print('loading gen trials...')
    # with open('useful_saves/move/recovery/param_recovery_trials_'+str(n_steps)+'_steps.pkl', 'rb') as f:
    #     gen_trials = pickle.load(f)
    # for key in gen_trials.keys():
    #     gen_trials[key] = gen_trials[key].loc[gen_trials[key]['Participant'].isin(participants)]




    ### param recovery loop

    ## for each gen (and hence fitting) model
    for m_s in range(1):
        for m in np.array([1,12]):

            ## get model's param settings 
            current_model = all_models[m_s][m]
            current_params = all_params[param_idx[m_s][m]]
            x0s = [set_0 for i_set_0, set_0 in enumerate(all_x0s) if i_set_0 in param_idx[m_s][m]]
            x0s = list(itertools.product(*x0s))
            ub = all_ub[param_idx[m_s][m]]
            lb = all_lb[param_idx[m_s][m]]
            lb[lb==0] = np.finfo(float).tiny
            bounds = Bounds(lb,ub)
            print()
            print('fitting ', current_model)
            print('current params',current_params)
            print('x0s: ',x0s)
            print('bounds: ',bounds)
            print()
            
            ## get sim_IDs 
            sim_IDs = gen_trials[current_model]['Sim_ID'].unique()
            n_simulations = len(sim_IDs)

            ## unparallelised
            if parallel == 0:
                print("beginning serial fit with ",mini,', n_simulations = ',n_simulations)
                for sim_p_n in tqdm(range(0,n_simulations)):
                    sim_ID = sim_IDs[sim_p_n]
                    df_trials = gen_trials[current_model].loc[gen_trials[current_model]['Sim_ID'] == sim_ID]
                    fit = True
                    recovery = True
                    fit_out = fit_model(m,m_s, current_params, df_trials, sim_ID, x0s, bounds, mini, minimize_method_opts, model_type, fit, recovery)
                    
                    # consolidate p's data 
                    fitting_param[current_model]['Participant'].extend(fit_out['Participant'])
                    fitting_param[current_model]['Direction'].extend(fit_out['Direction'])
                    fitting_param[current_model]['loss'].extend(fit_out['loss'])
                    fitting_param[current_model]['n_trials'].extend(fit_out['n_trials'])
                    fitting_param[current_model]['nfev'].extend(fit_out['nfev'])
                    fitting_param[current_model]['nit'].extend(fit_out['nit'])

                    for i_fit_out in range(len(fit_out['params'])):
                        for pa, par in enumerate(current_params):
                            fitting_param[current_model][par].append(fit_out['params'][i_fit_out][pa]) 
                            fitting_param[current_model][par+'_0'].append(fit_out['x0s'][i_fit_out][pa])
                            fitting_param[current_model]['gen_'+par].append(df_trials['gen_'+par].iloc[0])
                            print(par)
                            print(fit_out['params'][i_fit_out][pa]) 
                            print(df_trials['gen_'+par].iloc[0])


            ## parallelised
            elif parallel == 1:
                    
                ## start pool
                n_cores = 32
                pool = mp.Pool(np.min([n_simulations, n_cores]))
                print("beginning parallel fit with ",mini,', n_simulations = ',n_simulations, ', n_cores = ', n_cores)
                fit = True
                recovery = True

                ## fit to multiple participants at once
                if __name__ == '__main__':
                    pbar = tqdm(total = n_simulations)
                    fit_out = [pool.apply_async(fit_model, args = (m, m_s, current_params, gen_trials[current_model].loc[(gen_trials[current_model]['Sim_ID'] == sim_ID)
                                                                                #  &(gen_trials[gen_model]['Switched']=='pre')
                                                                                # &((gen_trials[gen_model]['Block']<4 )| ((gen_trials[gen_model]['Block']==4) & (gen_trials[gen_model]['Item_distance']<n_items-1)))
                                                                                    ]
                    , sim_ID, x0s, bounds, mini, minimize_method_opts, model_type, fit, recovery), callback=append_param_recovery) for sim_ID in sim_IDs]
                    pool.close()
                    pool.join()

            ## remove empty keys (e.g. for params not used by the current model)
            del_keys = []
            for key in fitting_param[current_model].keys():
                if not bool(fitting_param[current_model][key]):
                    del_keys.append(key)
            for dk in del_keys:
                fitting_param[current_model].pop(dk)

            ## save dictionary as df
            df_param[current_model] = pd.DataFrame.from_dict(fitting_param[current_model])
            with open('useful_saves/move/recovery/param_recovery_fits_relu.pkl', 'wb') as f:
                pickle.dump(df_param, f)



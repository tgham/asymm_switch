import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy.io
import os
import sys
import random
import itertools
from scipy.special import softmax
from functools import partial
from scipy.optimize import Bounds, minimize
from models import TI_RL
from tqdm.auto import tqdm
import warnings 
import importlib
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, LogisticRegression
warnings.filterwarnings('ignore')


### function for generating df of trial sequences 
def generate_sequences(p, n_items, n_blocks, switch_block, switch, switch_type):

    all_trials = np.empty((0,4), int)

    ## set stim directory and file names
    stim_folder = '../expt/gen_trials/stimuli_' + str(n_items)
    stim_IDs = os.listdir(stim_folder)

    ## randomly assign value to each stim
    random.shuffle(stim_IDs)

    ## get all possible pairs of stimuli and their orderings
    pairs = np.array(list(itertools.combinations(np.arange(n_items),2)),dtype=int)
    n_unique = len(pairs)
    pre_rank = np.arange(n_items)

    ## find feedback trials
    adj_pairs = pairs[np.abs(pairs[:,0]-pairs[:,1]) == 1,:]

    ## determine the rankings of items, depending on the type of switch used
    if switch_type == 'move':
        post_rank = move_rank(pre_rank, switch[0],switch[1])
        post_adj_pairs = post_rank[adj_pairs]
        pairs_pre_switch = np.vstack((pairs, adj_pairs))
        pairs_post_switch = np.vstack((pairs, post_adj_pairs))
    elif switch_type == 'swap':
        post_rank = swap_rank(pre_rank, switch[0],switch[1])
        post_adj_pairs = post_rank[adj_pairs]
        pairs_pre_switch = np.vstack((pairs, adj_pairs))
        pairs_post_switch = np.vstack((pairs, post_adj_pairs))
    elif switch_type == 'half_swap':
        post_rank = np.array([4,5,6,7,0,1,2,3])
        post_adj_pairs = post_rank[adj_pairs]
        pairs_pre_switch = np.vstack((pairs, adj_pairs))
        pairs_post_switch = np.vstack((pairs, post_adj_pairs))
    elif switch_type == 'invert':
        post_rank = np.flip(pre_rank)
        post_adj_pairs = post_rank[adj_pairs]
        pairs_pre_switch = np.vstack((pairs, adj_pairs))
        pairs_post_switch = np.vstack((pairs, post_adj_pairs))
    elif switch == None:
        pairs_pre_switch = np.vstack((pairs, adj_pairs))
        pairs_post_switch = np.copy(pairs_pre_switch)
    all_pairs = [pairs_pre_switch, pairs_post_switch]


    ## loop through blocks
    for b in range(n_blocks):

        ## determine whether to use pre or post-switch feedback pairs
        if b < switch_block-1:
            current_pairs = all_pairs[0]
        elif b <= switch_block-1:
            current_pairs = all_pairs[1]

        
        ## create empty array for block
        block_trials = np.zeros((2*len(current_pairs), 4))
        block_trials[:,0] = p
        block_trials[:,-1] = int(b+1)
        
        ## big while loop for checking consecutive repeats for the entire block 
        no_consec_all = 0
        while no_consec_all == 0:


            ### split block into two sub-blocks, shuffling within each (e.g. i1 vs i2, then i2 vs i1)

            ## shuffle first half of the block
            no_consec_1 = 0
            while no_consec_1 == 0:
                current_pairs = current_pairs[np.random.permutation(len(current_pairs)),:]

                ##check for consecutive repeats (e.g. 1v2 then 2v1), in which case reshuffle
                for ip in range(len(current_pairs)-1):
                    if not np.array_equal(current_pairs[ip], current_pairs[ip+1]):
                        no_consec_1 = 1
                    elif np.array_equal(current_pairs[ip], current_pairs[ip+1]):
                        no_consec_1 = 0
                        # print(current_pairs[ip], current_pairs[ip+1], 'redo')
                        break


            ## randomly flip i1 and i2 for half of trials
            flip_idx = np.random.choice(np.arange(len(current_pairs)), len(current_pairs)//2)
            flipped_pairs = np.flip(current_pairs[flip_idx,:],1)
            current_pairs[flip_idx,:] = flipped_pairs

            
            ## check to see if there are any repeats (consecutive or otherwise) within a sub-block of pairs with identical orders (e.g. 1v2 and 1v2 in the same sub-block, rather than 1v2 and 2v1). if so, reflip one of them
            
            #get all unique pairs
            u, i = np.unique(current_pairs, axis=0, return_index=True)
            if len(i) != len(current_pairs):

                #find index and flip non-unique pairs
                reflip_idx = ~np.isin(np.arange(0,len(current_pairs)), i)
                reflipped_pairs = np.flip(current_pairs[reflip_idx,:],1)
                current_pairs[reflip_idx,:] = reflipped_pairs

            ## (check if it worked)
            # u, i = np.unique(current_pairs, axis=0, return_index=True)
            # print(len(i) == len(current_pairs))


            ## flip this first sub-block to create second sub-block
            current_pairs_2 = np.flip(current_pairs, axis=1)

            ## check for consecutive repeats again
            no_consec_2 = 0
            while no_consec_2 == 0:
                current_pairs_2 = current_pairs_2[np.random.permutation(len(current_pairs_2)),:]

                ## temporarily sort each pair in ascending order to check for repeats, independent of flipping
                current_pairs_2_sorted = np.sort(current_pairs_2)
                for ip in range(len(current_pairs_2_sorted)-1):
                    if not np.array_equal(current_pairs_2_sorted[ip], current_pairs_2_sorted[ip+1]):
                        no_consec_2 = 1
                    elif np.array_equal(current_pairs_2_sorted[ip], current_pairs_2_sorted[ip+1]):
                        no_consec_2 = 0
                        # print(current_pairs_2_sorted[ip], current_pairs_2_sorted[ip+1],'redo')
                        break


            ## final check for consecutive repeats (indep of position) once the two subblocks are joined, in which case start again
            joined_pairs = np.vstack((current_pairs, current_pairs_2))
            joined_pairs_sorted = np.sort(joined_pairs)
            for ip in range(len(joined_pairs_sorted)-1):
                if not np.array_equal(joined_pairs_sorted[ip], joined_pairs_sorted[ip+1]):
                    no_consec_all = 1
                elif np.array_equal(joined_pairs_sorted[ip], joined_pairs_sorted[ip+1]):
                    no_consec_all = 0
                    # print(joined_pairs_sorted[ip], joined_pairs_sorted[ip+1], 'redo')
                    break


        ## join sub-blocks together and add block number
        block_trials[:,1:3] = np.vstack((current_pairs, current_pairs_2))
        all_trials = np.vstack((all_trials, block_trials))


    ### compile to dataframe

    ## standard trial info
    df_trials = pd.DataFrame(all_trials, columns=['Participant', 'Item_1', 'Item_2', 'Block'],dtype=int)
    df_trials.insert(loc=0, column='Trial', value=np.arange(1, len(df_trials)+1))

    ## JPG IDs associated with each image
    df_trials['Image_1'] = np.array(stim_IDs)[df_trials['Item_1'].to_numpy()]
    df_trials['Image_2'] = np.array(stim_IDs)[df_trials['Item_2'].to_numpy()]

    ## feedback and winners pre-switch
    df_trials['Winning_Item'] = df_trials[['Item_1','Item_2']].max(axis=1).to_numpy()
    df_trials['Losing_Item'] = df_trials[['Item_1','Item_2']].min(axis=1).to_numpy()
    df_trials['Feedback_on'] = np.zeros(len(df_trials))
    df_trials['InverseFb'] = np.zeros(len(df_trials))
    df_trials.loc[np.abs(df_trials['Item_1']-df_trials['Item_2'])==1, 'Feedback_on'] = 1

    ## ranks of each item (pre-switch, this is trivially just the item number)
    df_trials['Rank_1'] = df_trials['Item_1']
    df_trials['Rank_2'] = df_trials['Item_2']

    ## direction of switch 
    directions = ['down', 'up']
    d = int(switch[0]<switch[1])
    df_trials['Direction'] = np.repeat(directions[d], len(df_trials))

    ## feedback and winners post-switch
    if len(switch)==2:

        ## get trials post-switch 

        # post-block
        post_trials = df_trials.loc[df_trials['Block']>=switch_block, ['Item_1', 'Item_2']].to_numpy()

        # or, post-trial
        post_trials = df_trials.loc[df_trials['Block']>=switch_block, ['Item_1', 'Item_2']].to_numpy()

        #get the new rank positions of all items after the switch
        post_positions = [np.where(post_rank == item)[0][0] for item in post_trials.flatten()]
        post_positions = np.array(post_positions).reshape(post_trials.shape)

        #determine winners under the post-switch ranking
        post_winners = post_rank[np.max(post_positions, axis=1)]
        post_losers = post_rank[np.min(post_positions, axis=1)]
        df_trials.loc[df_trials['Block']>=switch_block, 'Winning_Item'] = post_winners
        df_trials.loc[df_trials['Block']>=switch_block, 'Losing_Item'] = post_losers

        #determine adjacent (and hence feedback) pairs under post-switch ranking
        post_adj = np.abs(np.diff(post_positions))==1
        # df_trials.loc[df_trials['Block']>=switch_block, 'Feedback'] = new_adj.flatten().astype(int)
        df_trials.loc[df_trials['Block']>=switch_block, 'Feedback_on'] = post_adj.flatten().astype(int)

        #save new rankings
        df_trials.loc[df_trials['Block']>=switch_block, 'Rank_1'] = post_positions[:,0]
        df_trials.loc[df_trials['Block']>=switch_block, 'Rank_2'] = post_positions[:,1]

        #mark trials after the first switch trial on which there is feedback
        switch_trial = np.argwhere((df_trials['Winning_Item'] != df_trials[['Item_1','Item_2']].max(axis=1)).to_numpy() & (df_trials['Feedback_on']==1).to_numpy())[0].squeeze() 
        df_trials['Switched'] = np.zeros(len(df_trials))
        df_trials.loc[int(switch_trial):, 'Switched'] = 1

        #revert the winners/losers, ranks, rank distances etc. on trials that come after the switch block, but before the switch could have possibly been detected
        df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), 'Winning_Item'] = df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), ['Item_1', 'Item_2']].max(axis=1).to_numpy()
        df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), 'Losing_Item'] = df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), ['Item_1', 'Item_2']].min(axis=1).to_numpy()
        df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), 'Rank_1'] = df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), 'Item_1'].to_numpy()
        df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), 'Rank_2'] = df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), 'Item_2'].to_numpy()
        df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), 'Rank_distance'] = np.abs(df_trials.loc[(df_trials['Switched'] == 0) & (df_trials['Block']<= switch_block), ['Item_1','Item_2']].diff(axis=1).iloc[:,1].to_numpy())

        ## rename switches
        df_trials.loc[df_trials['Switched']==0, 'Switched'] = 'pre'
        df_trials.loc[df_trials['Switched']==1, 'Switched'] = 'post'

        ## distances
        df_trials['Item_distance'] = np.abs(df_trials['Item_1'] - df_trials['Item_2'])
        df_trials['Rank_distance'] = np.abs(df_trials['Rank_1'] - df_trials['Rank_2'])

        ## winning/losing ranks
        df_trials['Losing_Rank'] = df_trials[['Rank_1','Rank_2']].min(axis=1)
        df_trials['Winning_Rank'] = df_trials[['Rank_1','Rank_2']].max(axis=1)

        ## add column containing comparison as string
        combined = np.sort(df_trials[['Item_1','Item_2']]).astype(int).astype(int)
        comb = ['{}<{}'.format(c[0]+1,c[1]+1) for c in combined]
        df_trials['Comparison'] = comb
        
        #mark trials where the ground truth has changeed
        # df_trials.loc[df_trials[np.max(post_trials, axis=1) != post_winners],'GT switched'] = 1




    ## change item numbers (because we have been using zero-based indexing)
    df_trials['Item_1'] +=1
    df_trials['Item_2'] +=1
    df_trials['Rank_1'] +=1
    df_trials['Rank_2'] +=1
    df_trials['Winning_Item'] +=1
    df_trials['Losing_Item'] +=1

    ## define low, mid and high-cnarciness 
    df_trials = pair_value(df_trials, 'Item')
    df_trials['Combined_value'] = np.zeros(len(df_trials))
    df_trials['Combined_value'] = df_trials[['Item_1','Item_2']].sum(1)

    ## add lowest and highest numbers (useful for plotting)
    df_trials['Smallest_number'] = df_trials[['Item_1','Item_2']].min(axis=1).astype(int)
    df_trials['Largest_number'] = df_trials[['Item_1','Item_2']].max(axis=1).astype(int)

    return df_trials


### functions for changing the ranking of items

## move a single item
def move_rank(pre_rank, to_move, move_to):

    #fix for cases where removing an element from the array changes the index of the desire position
    if to_move < move_to:
        move_to += 1

    post_rank = np.copy(pre_rank)
    post_rank[to_move] = 100
    post_rank = np.insert(post_rank, move_to, to_move)
    post_rank = np.delete(post_rank, np.where(post_rank==100))
    return post_rank

## swap two items
def swap_rank(pre_rank, swap_1, swap_2):
    post_rank = np.copy(pre_rank)
    post_rank[swap_1] = swap_2
    post_rank[swap_2] = swap_1
    return post_rank
    

## define the value of the comparison
def pair_value(df_trials, value_determiner = 'Item'):
    
    n_items = int(np.nanmax(df_trials['Item_1']))
    
    ## define low, mid and high-cnarciness 
    if n_items == 8:
        low = [
            [1,3],
            [1,4],
            [1,5],
            [1,6],
            [2,4],
            [2,5]
        ]
        med = [
            [1,7],
            [1,8],
            [2,6],
            [2,7],
            [2,8],
            [3,5],
            [3,6],
            [3,7],
            [4,6]
        ]
        high = [
            [3,8],
            [4,7],
            [4,8],
            [5,7],
            [5,8],
            [6,8]
        ]
    elif n_items == 7:
        low = [

            # adj
            [1,2],
            [2,3],

            # non-adj
            [1,3],
            [1,4],
            [1,5],
            [2,4],
            [2,5]
        ]
        med = [
            
            # adj
            [3,4],
            [4,5],

            # non-adj
            [1,6],
            [1,7],
            [2,6],
            [2,7],
            [3,5],
        ]

        high = [

            # adj
            [5,6],
            [6,7],

            # non-adj
            [3,6],
            [3,7],
            [4,6],
            [4,7],
            [5,7]

        ]
    df_trials['Pair_value'] = np.zeros((len(df_trials),1))
    pair_value = np.zeros((n_items,n_items))
    for l in low:
        pair_value[l[0]-1, l[1]-1] = 1
        pair_value[l[1]-1, l[0]-1] = 1
    for m in med:
        pair_value[m[0]-1, m[1]-1] = 2
        pair_value[m[1]-1, m[0]-1] = 2
    for h in high:
        pair_value[h[0]-1, h[1]-1] = 3
        pair_value[h[1]-1, h[0]-1] = 3


    ## low mid high
    apv = 0
    all_pair_values = np.zeros((len(df_trials),1))
    for i, row in df_trials.iterrows():
        v1 = row[value_determiner+'_1']
        v2 = row[value_determiner+'_2']
        all_pair_values[apv] = pair_value[int(v1-1), int(v2-1)]
        apv += 1

    df_trials['Pair_value'] = all_pair_values
    df_trials.loc[df_trials['Pair_value'] == 1, 'Pair_value'] = 'Low'
    df_trials.loc[df_trials['Pair_value'] == 2, 'Pair_value'] = 'Med'
    df_trials.loc[df_trials['Pair_value'] == 3, 'Pair_value'] = 'High'

    return df_trials


## saving sequences to excel files
def save_seq(df_trials):


    ## add full path name for stimuli 
    df_trials['Path_1'] = 'expt_move/resources/stim_IDs/' + df_trials['Image_1']
    df_trials['Path_2'] = 'expt_move/resources/stim_IDs/' + df_trials['Image_2']

    ## save xlx file
    file_name = '../expt_move/resources/sequences/euro_p' + str(df_trials['Participant'][0]) + '.xlsx'
    df_trials.to_excel(file_name, index = False)


### fitting functions

## function for fitting all participants to a given model
def fit_model(m, model_set, current_params, df_trials, p, x0s, bounds, minimize_method, minimize_method_opts, model_type, fit = True, recovery=False):
    

    ## init dict
    fit_out = {
            'Participant': [],
            'Direction': [],
            'loss': [],
            'n_trials': [],
            'params': [],
            'x0s': [],
            'success': [],
            'nfev': [],
            'nit': [],
        }

    ## if performing recovery, save the data-generating params
    if recovery == True:
        for param in current_params:
            fit_out['gen_'+param] = []
    
    n_items = int(np.nanmax(df_trials['Item_1']))


    ## add non-changing arguments to function
    kwargs = dict(
        df_trials = df_trials,
        model = m,
        model_set = model_set,
        fit = fit,
        recovery = recovery
    )
    RL = TI_RL(n_items)
    fun = partial(RL.run, **kwargs)


    ### optimise for single initial points

    # fit model
    # res = minimize(
    #     fun = fun,
    #     x0 = x0s,
    #     method = minimize_method,
    #     bounds = bounds,
    #     # options = minimize_method_opts,
    # )


    
    ### optimise for multiple initial points
    for ix0 in range(len(x0s)):

        #differential evolution
        if minimize_method == 'diff_evo':
            res = scipy.optimize.differential_evolution(
                func = fun,
                # x0 = x0s[ix0],
                bounds = bounds,
                maxiter = 500,
                disp = False,
                popsize  = 50,
                recombination = 0.5,
                seed = 1,
                updating = 'deferred',
                mutation = (0.5,1.5),
                workers = 1,
                polish = False
            )

        #deterministic
        else:
            res = minimize(
                fun = fun,
                # x0 = x0s[ix0],
                bounds = bounds,
                method = minimize_method,
                options = minimize_method_opts,
            )

        fit_out['Participant'].append(p)
        fit_out['Direction'].append(df_trials['Direction'].iloc[0])
        fit_out['loss'].append(res.fun)
        fit_out['n_trials'].append(len(df_trials))
        fit_out['params'].append(res.x)
        fit_out['x0s'].append(x0s[ix0])
        fit_out['success'].append(res.success)
        fit_out['nfev'].append(res.nfev)
        fit_out['nit'].append(res.nit)

        if recovery == True:
            for param in current_params:
                fit_out['gen_'+param].append(df_trials['gen_'+param].iloc[0])

        # # consolidate data (inc param initial points)
        # fitting_data[current_model]['Participant'].append(p)
        # fitting_data[current_model]['loss'].append(res.fun)
        # fitting_data[current_model]['ix0'].append(ix0)
        # fitting_data[current_model]['n_trials'].append(len(df_trials))
        # for pa, par in enumerate(current_params):
        #     fitting_data[current_model][par].append(res.x[pa]) 
        #     fitting_data[current_model][par+'_0'].append(x0s[ix0][pa])

    return fit_out 
    

## function for extracting best fits from multi-x0 dataset
def best_x0(df_fits_big, moi):
    df_fits = {}
    for m, model in enumerate(moi):
        df_fits[model] = df_fits_big[model].loc[df_fits_big[model].groupby(
            'Participant')['loss'].idxmin()].reset_index(drop=True)        
    return df_fits
    
## function for renaming models (in case models were fit with one of the previous names)
def rename_models(df_fits):
    new_models = {
        'Q1*': 'Q-symm',
        'Q2*': 'Q-asymm',
        'Q3*': 'Q-adapt',
        'Q3*d':'Q-adapt-d'
    }
    old_models = df_fits.keys()
    rm_models = []
    df_fits_tmp = {}
    for key in old_models:
        if key in new_models.keys():
            df_fits_tmp[new_models[key]] = df_fits[key]
        else:
            df_fits_tmp[key] = df_fits[key]
    return df_fits_tmp


### function for calculating asymmetry metric
def asymm_metric(all_data, model = 'human', adj = False, extremes = True, split = 'halfway'):

    participants = np.unique(all_data['Participant'])
    participants = np.sort(participants)
    n_participants = len(participants)
    n_items = int(np.nanmax(all_data['Item_1']))

    if extremes:
        inc_items = np.arange(1,n_items+1)
    else:
        inc_items = np.arange(2,n_items)


    ## calculate accuracy for each combined value
    if split == 'halfway':
        if extremes:
            if adj:
                asymm = all_data.groupby(['Participant','Direction','Switched','Combined_value'],as_index = False).mean('Accuracy '+model)[['Participant','Direction','Switched','Combined_value','Accuracy '+model]]
            else:
                asymm = all_data.loc[
                    (all_data['Feedback_on']==0)
                    &(all_data['Item_1'].isin(inc_items))
                    &(all_data['Item_2'].isin(inc_items))
                        &(all_data['Item_distance']>1)
                    ].groupby(['Participant','Direction','Switched','Combined_value'],as_index = False).mean('Accuracy '+model)[['Participant','Direction','Switched','Combined_value','Accuracy '+model]]

        else:
            if adj:
                asymm = all_data.loc[
                    (all_data['Item_1'].isin(inc_items))
                    &(all_data['Item_2'].isin(inc_items))
                    # &(all_data['Feedback_on']==0)
                    #     &(all_data['Item_distance']>1)
                    ].groupby(['Participant','Direction','Switched','Combined_value'],as_index = False).mean('Accuracy '+model)[['Participant','Direction','Switched','Combined_value','Accuracy '+model]]
            else:
                asymm = all_data.loc[
                    (all_data['Item_1'].isin(inc_items))
                    &(all_data['Item_2'].isin(inc_items))
                    &(all_data['Feedback_on']==0)
                        &(all_data['Item_distance']>1)
                    ].groupby(['Participant','Direction','Switched','Combined_value'],as_index = False).mean('Accuracy '+model)[['Participant','Direction','Switched','Combined_value','Accuracy '+model]]

        

        ## regress accuracy on diagonal number across all Ps
        directions = asymm['Direction'].unique()
        for di, d in enumerate(directions):
            print(d)
            for hi, half in enumerate(['pre','post']):
                
                ## run regression 
                X = asymm.loc[(asymm['Switched']==half) & (asymm['Direction']==d), 'Combined_value']
                y = asymm.loc[(asymm['Switched']==half) & (asymm['Direction']==d), 'Accuracy '+model]
                X = sm.add_constant(X)
                reg = sm.OLS(y, X).fit()
                print(half+'-switch: ß = ',reg.params[1],', t = ',reg.tvalues[1], ', p = ',reg.pvalues[1])

            print()

        ## In addition, calculate asymmetry metric for each participant (i.e. slope of accuracy vs combined value)
        n_diags = asymm['Combined_value'].nunique()
        slopes = np.zeros((2, n_participants))
        for h, half in enumerate(['pre','post']):
            for pi, p in enumerate(participants):
                x = asymm.loc[(asymm['Participant']==p) & (asymm['Switched']==half), 'Combined_value'].to_numpy().reshape(-1,1)
                y = asymm.loc[(asymm['Participant']==p) & (asymm['Switched']==half), 'Accuracy '+model].to_numpy()
                lin_reg = LinearRegression()
                lin_reg.fit(x, y)
                slopes[h, pi] = lin_reg.coef_

    return asymm, slopes
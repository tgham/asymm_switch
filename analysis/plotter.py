import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from helpers import *
from tqdm.auto import tqdm
import itertools
import statannot
from statannotations.Annotator import Annotator
from matplotlib.animation import FuncAnimation
from IPython.display import Video, HTML
from scipy.ndimage import gaussian_filter1d

### plot Low, Med and High valued comparisons
def low_med_high(all_data, subplot_splits, subplot_dims, value_split = 'lmh', plot_split = False, bin_width=70, step = 1, min_periods = 1, extremes = True, title = None):


    ## init the subplot
    n_rows = subplot_dims[0]
    n_cols = subplot_dims[1]
    figs, axs = plt.subplots(n_rows,n_cols, figsize = (n_cols * 2.5, n_rows * 3), sharey=True, squeeze=0) #rows cols 
    n_items = all_data['Item_1'].max()
    n_trials = int(all_data['Trial'].max())
    inc_items = np.arange(2,n_items)
    n_pre_trials = int(all_data.loc[all_data['Switched']=='pre']['Trial'].max())
    try:
        n_post_trials = int(all_data.loc[all_data['Switched']=='post']['Trial'].max())
    except:
        pass
    lw = []

    ## prepare the splits of the data (e.g. the entire learning curve vs pre/post switch)
    if plot_split:
        plot_splits = [['pre'],['post']]
        trial_ranges = [
            range(1,n_pre_trials+1),
            range(n_pre_trials+1,n_trials+1)
        ]
    else:
        plot_splits = [['pre','post']]
        trial_ranges = [
            range(1,n_trials+1)
            ]


    ## create column for relative trial, i.e. trial relative to the switch
    all_data['Rel_Trial'] = np.zeros(len(all_data))+np.nan
    for p in all_data['Participant'].unique():
        switch_trial = all_data.loc[(all_data['Participant']==p) & (all_data['Switched']=='post')]['Trial'].min()-1
        all_data.loc[(all_data['Participant']==p),'Rel_Trial'] = all_data.loc[(all_data['Participant']==p),'Trial']-switch_trial
    rel_trial_min = np.min(all_data['Rel_Trial'])
    rel_trial_max = np.max(all_data['Rel_Trial'])
    # print(rel_trial_min, rel_trial_max)

    ## loop through models
    for a, ax in enumerate(axs.reshape(-1)):
        current_direction = subplot_splits[a][0]
        current_model = subplot_splits[a][1]

        ## loop through expt splits
        for si, switch in enumerate(plot_splits):

            ## get accuracy for each value
            if value_split == 'lmh':
                
                ## get data according to whether extremes are included or not
                if extremes == True:
                    to_plot_adj = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==1)
                                                &(all_data['Switched'].isin(switch))
                                                ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_low = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &((all_data['Pair_value']=='Low'))
                                                &(all_data['Switched'].isin(switch))
                                                ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_med = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &(all_data['Pair_value']=='Med')
                                                &(all_data['Switched'].isin(switch))
                                                ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_high = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &((all_data['Pair_value']=='High'))
                                                &(all_data['Switched'].isin(switch))
                                                ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                elif extremes == False:
                    to_plot_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==1) &
                                                (all_data['Item_1'].isin(inc_items)) 
                                                &(all_data['Item_2'].isin(inc_items))
                                                &(all_data['Switched'].isin(switch))
                                                    # ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                                                ].groupby(['Rel_Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_low = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &(all_data['Item_distance']>1)
                                                &((all_data['Pair_value']=='Low'))
                                                &(all_data['Item_1'].isin(inc_items)) 
                                                &(all_data['Item_2'].isin(inc_items))
                                                &(all_data['Switched'].isin(switch))
                                                    # ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                                                ].groupby(['Rel_Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_med = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &(all_data['Item_distance']>1)
                                                &((all_data['Pair_value']=='Med'))
                                                &(all_data['Item_1'].isin(inc_items)) 
                                                &(all_data['Item_2'].isin(inc_items))
                                                &(all_data['Switched'].isin(switch))
                                                    # ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                                                ].groupby(['Rel_Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_high = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &(all_data['Item_distance']>1)
                                                &((all_data['Pair_value']=='High'))
                                                &(all_data['Item_1'].isin(inc_items))
                                                &(all_data['Item_2'].isin(inc_items))
                                                &(all_data['Switched'].isin(switch))
                                                    # ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                                                ].groupby(['Rel_Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                elif extremes == 2: ## potentially need to add &(all_data['Item_distance']>1) somewhere here
                    to_plot_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==1)
                                                &(all_data['Item_1'].isin(inc_items))
                                                &(all_data['Item_2'].isin(inc_items))
                                                &(all_data['Switched'].isin(switch))
                                                    ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_low = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &((all_data['Pair_value']=='Low'))
                                                &((all_data['Switched']=='pre')| ((all_data['Switched']=='post') & (all_data['Item_1'].isin(inc_items)) & (all_data['Item_2'].isin(inc_items))))
                                                &(all_data['Switched'].isin(switch))
                                                    ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_med = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &((all_data['Pair_value']=='Med'))
                                                &((all_data['Switched']=='pre')|
                                                ((all_data['Switched']=='post') & (all_data['Item_1'].isin(inc_items)) & (all_data['Item_2'].isin(inc_items))))
                                                &(all_data['Switched'].isin(switch))
                                                    ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_high = all_data.loc[(all_data['Direction'] == current_direction)
                                                &(all_data['Feedback_on']==0)
                                                &((all_data['Pair_value']=='High'))
                                                &((all_data['Switched']=='pre')
                                                | ((all_data['Switched']=='post') & (all_data['Item_1'].isin(inc_items)) & (all_data['Item_2'].isin(inc_items))))
                                                &(all_data['Switched'].isin(switch))
                                                    ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]

                
                ## plot
                    
                # rolling average
                to_plot_adj = to_plot_adj.rolling(
                    window=bin_width,
                    center=True,
                    min_periods=min_periods,
                    step=step,
                ).mean()
                to_plot_low = to_plot_low.rolling(
                    window=bin_width,
                    center=True,
                    min_periods=min_periods,
                    step=step,
                ).mean()
                to_plot_med = to_plot_med.rolling(
                    window=bin_width,
                    center=True,
                    min_periods=min_periods,
                    step=step,
                ).mean()
                to_plot_high = to_plot_high.rolling(
                    window=bin_width,
                    center=True,
                    min_periods=min_periods,
                    step=step,
                ).mean()

                ## or, another smoothing technique using gaussian_filter1d
                # to_plot_adj = pd.Series(gaussian_filter1d(to_plot_adj.values, sigma=bin_width//5), index=to_plot_adj.index)
                # to_plot_low = pd.Series(gaussian_filter1d(to_plot_low.values, sigma=bin_width//5), index=to_plot_low.index)
                # to_plot_med = pd.Series(gaussian_filter1d(to_plot_med.values, sigma=bin_width//5), index=to_plot_med.index)
                # to_plot_high = pd.Series(gaussian_filter1d(to_plot_high.values, sigma=bin_width//5), index=to_plot_high.index)


                
                # reindex
                # to_plot_adj = to_plot_adj.reindex(trial_ranges[si])
                # to_plot_low = to_plot_low.reindex(trial_ranges[si])
                # to_plot_med = to_plot_med.reindex(trial_ranges[si])
                # to_plot_high = to_plot_high.reindex(trial_ranges[si])
                ## if we're plotting relative to the switch, these trial ranges need to be adjusted (i.e. min and max relative trial)
                to_plot_adj = to_plot_adj.reindex(range(int(np.min(all_data['Rel_Trial'])), int(np.max(all_data['Rel_Trial']))+1))
                to_plot_low = to_plot_low.reindex(range(int(np.min(all_data['Rel_Trial'])), int(np.max(all_data['Rel_Trial']))+1))
                to_plot_med = to_plot_med.reindex(range(int(np.min(all_data['Rel_Trial'])), int(np.max(all_data['Rel_Trial']))+1))
                to_plot_high = to_plot_high.reindex(range(int(np.min(all_data['Rel_Trial'])), int(np.max(all_data['Rel_Trial']))+1))
                

                # plot
                l = sns.lineplot(x = to_plot_low.index, y=to_plot_low.values, ax = ax, lw=3.5, label = 'Low', color = 'darkslateblue', legend = False)
                l = sns.lineplot(x = to_plot_med.index, y=to_plot_med.values, ax = ax, lw=3.5, label = 'Med', color = 'darkviolet', legend = False)
                l = sns.lineplot(x = to_plot_high.index, y=to_plot_high.values, ax = ax, lw=3.5, label = 'High', color = 'deeppink', legend = False)
                l.set_xlabel('')
                l.set_ylabel('')

                # get the limits of the split (for the switch line)
                # ax.set_xlim(0-bin_width/2, n_trials+bin_width/2)
                # ax.set_xlim(0, n_trials)
                if plot_split:
                    if si == 0:
                        xmaxs = np.array([
                            to_plot_adj.index[~np.isnan(to_plot_adj.values)][-1],
                            to_plot_low.index[~np.isnan(to_plot_low.values)][-1],
                            to_plot_med.index[~np.isnan(to_plot_med.values)][-1],
                            to_plot_high.index[~np.isnan(to_plot_high.values)][-1]
                        ])
                        lw.append(np.max(xmaxs))
                    else:
                        xmins = np.array([
                            to_plot_adj.index[~np.isnan(to_plot_adj.values)][0],
                            to_plot_low.index[~np.isnan(to_plot_low.values)][0],
                            to_plot_med.index[~np.isnan(to_plot_med.values)][0],
                            to_plot_high.index[~np.isnan(to_plot_high.values)][0]
                        ])
                        lw.append(np.min(xmins))
                    # split_x = np.mean(lw)
                else:
                    xmin, xmax = ax.get_xlim()
                    # print(xmin, xmax)
                    split_x = np.linspace(0, xmax*6/(6+1),6)[3] + (bin_width/4)
                    lw.append(split_x - bin_width/4)
                    lw.append(split_x + bin_width/4)

            ## just do adj and non-adj
            elif value_split == 'adj':

                ## get data according to whether extremes are included or not
                if extremes == True:
                    to_plot_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==1)].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_non_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==0)].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                elif extremes == False:
                    to_plot_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==1) &
                                                (all_data['Item_1'].isin(inc_items)) 
                                                &(all_data['Item_2'].isin(inc_items))
                                                ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_non_adj = all_data.loc[(all_data['Direction'] == current_direction)&
                                                (all_data['Feedback_on']==0) &
                                                (all_data['Item_1'].isin(inc_items)) & 
                                                (all_data['Item_2'].isin(inc_items))
                                                ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                elif extremes == 2:
                    to_plot_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==1)
                                                &(all_data['Item_1'].isin(inc_items))
                                                &(all_data['Item_2'].isin(inc_items))
                                                    ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot_non_adj = all_data.loc[(all_data['Direction'] == current_direction)&
                                                (all_data['Feedback_on']==0) &
                                                (all_data['Item_1'].isin(inc_items)) & 
                                                (all_data['Item_2'].isin(inc_items))
                                                    ].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    
                ## plot
                    
                # rolling average
                to_plot_adj = to_plot_adj.rolling(window=bin_width, center=True, min_periods = min_periods, step=step).mean()
                to_plot_non_adj = to_plot_non_adj.rolling(window=bin_width, center=True, min_periods = min_periods, step=step).mean()

                # reindex
                to_plot_adj = to_plot_adj.reindex(trial_ranges[si])
                to_plot_non_adj = to_plot_non_adj.reindex(trial_ranges[si])

                # plot
                l = sns.lineplot(x = to_plot_adj.index, y=to_plot_adj.values, ax = ax, lw=3, label = 'Adjacent', color = 'springgreen', legend = False)
                l = sns.lineplot(x = to_plot_non_adj.index, y=to_plot_non_adj.values, ax = ax, lw=3, label = 'TI', color = 'blue', legend = False)
                l.set_xlabel('')
                l.set_ylabel('')

                # get the limits of the split (for the switch line)
                if plot_split:
                    if si == 0:
                        xmaxs = np.array([
                            to_plot_adj.index[~np.isnan(to_plot_adj.values)][-1],
                            to_plot_non_adj.index[~np.isnan(to_plot_non_adj.values)][-1]
                        ])
                        lw.append(np.max(xmaxs))
                    else:
                        xmins = np.array([
                            to_plot_adj.index[~np.isnan(to_plot_adj.values)][0],
                            to_plot_non_adj.index[~np.isnan(to_plot_non_adj.values)][0]
                        ])
                        lw.append(np.min(xmins))
                    # split_x = np.mean(lw)
                else:
                    _, xmax = ax.get_xlim()
                    split_x = np.linspace(0, xmax*6/(6+1),6)[3] + (bin_width/4)
                    lw.append(split_x - bin_width/4)
                    lw.append(split_x + bin_width/4)


            ## or plot TI pairs by combined value
            elif value_split == 'comb':

                ## get data according to whether extremes are included or not
                if extremes == True:
                    data = all_data.loc[(all_data['Direction'] == current_direction)
                                        &(all_data['Feedback_on']==0)
                                        &(all_data['Switched'].isin(switch))
                    ]
                    adj_data = all_data.loc[(all_data['Direction'] == current_direction)
                                        &(all_data['Feedback_on']==1)
                                        &(all_data['Item_distance']==1)
                                        &(all_data['Switched'].isin(switch))
                    ]
                elif extremes == False:
                    data = all_data.loc[(all_data['Direction'] == current_direction)
                                        &(all_data['Feedback_on']==0)
                                        &(all_data['Item_distance']>1)
                                        &(all_data['Item_1'].isin(inc_items))
                                        &(all_data['Item_2'].isin(inc_items))
                                        &(all_data['Switched'].isin(switch))
                    ]
                    adj_data = all_data.loc[(all_data['Direction'] == current_direction)
                                        &(all_data['Feedback_on']==1)
                                        &(all_data['Item_distance']==1)
                                        &(all_data['Switched'].isin(switch))
                    ]
                elif extremes == 2:
                    adj_data = all_data.loc[(all_data['Direction'] == current_direction)
                                        &(all_data['Feedback_on']==1)
                                        &(all_data['Item_distance']==1)
                                        &(all_data['Switched'].isin(switch))
                    ]
                    data = all_data.loc[(all_data['Direction'] == current_direction)
                                        &(all_data['Feedback_on']==0)
                                        &((all_data['Switched']=='pre')| ((all_data['Switched']=='post') & (all_data['Item_1'].isin(inc_items)) & (all_data['Item_2'].isin(inc_items))))
                                        &(all_data['Switched'].isin(switch))
                    ]


                comb_max = int(np.max(data['Combined_value']))
                comb_min = int(np.min(data['Combined_value']))

                ## plot each combined value
                colors = plt.cm.magma(np.linspace(0.1,0.7,comb_max-comb_min+1))
                for ci, comb in enumerate(np.arange(comb_min, comb_max+1)):
                    to_plot = data.loc[data['Combined_value']==comb].groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                    to_plot = to_plot.rolling(window=bin_width, center=True, min_periods = min_periods, step=step).mean()
                    to_plot = to_plot.reindex(trial_ranges[si])
                    l = sns.lineplot(x = to_plot.index, y=to_plot.values, ax = ax, lw=3, label = str(int(comb)), color = colors[ci], legend = False)
                    l.set_xlabel('')
                    l.set_ylabel('')
                to_plot_adj = adj_data.groupby(['Trial']).mean('Accuracy '+current_model)['Accuracy '+current_model]
                to_plot_adj = to_plot_adj.rolling(window=bin_width, center=True, min_periods = min_periods, step=step).mean()
                to_plot_adj = to_plot_adj.reindex(trial_ranges[si])
                l = sns.lineplot(x = to_plot_adj.index, y=to_plot_adj.values, ax = ax, lw=3, legend = False)


        ## shade the post-changepoint area
        # xmin, xmax = ax.get_xlim()
        # x_half = np.linspace(xmin, xmax*6/(6+1),6)[3]
        # u = ax.axvspan(xmin = x_half, xmax = xmax, color = 'r', alpha = 0.08)

        ## or, do this using the relative trials, i.e. from rel_trial 0
        xmin, xmax = ax.get_xlim()
        u = ax.axvspan(xmin = 0, xmax = xmax, color = 'r', alpha = 0.08)


        ## axes formatting
        if current_model == 'Q-asymm_m2':
            current_model = "Q-asymm²"
        ax.text(.02,.9,current_model,
            horizontalalignment='left',
            transform=ax.transAxes,
            fontstyle = 'italic',
            fontsize = 15)
        ax.text(.02,.8,current_direction,
            horizontalalignment='left',
            transform=ax.transAxes,
            fontsize = 15)
    y_max = max(ax.get_ylim()[1] for ax in axs.flatten())
    y_min = min(ax.get_ylim()[0] for ax in axs.flatten())
    print(y_min, y_max)
    y_max = np.round(y_max*10)/10
    y_min = np.round(y_min*10)/10
    for ax in axs.flatten():
        # ax.set_ylim([y_min-0.03,y_max+0.03])
        ax.tick_params(axis='y', labelsize=13)
    axes_formatting(figs, axs)


    # ## add legend to mark the two plots, but not the switch line
    handles, labels = ax.get_legend_handles_labels()
    if value_split == 'lmh':
        legend_title = 'TI pair value'
    elif value_split == 'comb':
        legend_title = 'Combined value'
    else:
        legend_title = ''
    axs[0][-1].legend(handles=handles, labels=labels, loc='upper right', bbox_to_anchor=(1.6, 1.025), title = legend_title)
    
    ## overall axes and titles
    # supx = figs.text(0.5, 0.01, 'Block', ha='center', va='center', fontsize=16)
    supx = figs.text(0.5, 0.01, 'Trial', ha='center', va='center', fontsize=16)
    supy = figs.text(0.0, 0.5, 'P(correct)', ha='center', va='center', rotation='vertical', fontsize=16)
    figs.subplots_adjust(wspace=0)
    figs.subplots_adjust(hspace=0)

    return figs, axs


### plot choice ratio for each item
def ratio_plot(all_data, subplot_splits, subplot_dims, bin_width=70, step=1, min_periods=1, title = None):

    n_rows = subplot_dims[0]
    n_cols = subplot_dims[1]
    figs, axs = plt.subplots(n_rows,n_cols, figsize = (n_cols * 3, n_rows * 4), squeeze=0, sharey=True) #rows cols 
    n_items = all_data['Item_1'].max()
    n_trials = all_data['Trial'].max()


    ## loop through models
    for a, ax in enumerate(axs.reshape(-1)):
        current_direction = subplot_splits[a][0]
        current_model = subplot_splits[a][1]

        ## plot choice_ratios (do them in reverse order so that the legend is in the right order)
        for i in np.arange(n_items,0,-1):
            to_plot = all_data.loc[(all_data['Direction']==current_direction)
                                   &(all_data['Feedback_on']==0)
                                   &(all_data['Item_distance']>1)  
                                   &(all_data['Item_1'].isin(np.arange(2,n_items)))
                                      &(all_data['Item_2'].isin(np.arange(2,n_items)))
                                   ].groupby(['Trial']).mean('Item_'+str(int(i))+'_chosen_'+current_model)['Item_'+str(int(i))+'_chosen_'+current_model]
            
            # rolling average
            to_plot = to_plot.rolling(window=bin_width, center=True, min_periods=min_periods, step=step).mean()

            # reindex
            to_plot = to_plot.reindex(range(1, int(n_trials+1)))

            # plot
            l = sns.lineplot(x = to_plot.index, y=to_plot.values, ax = ax, lw=3.5, label = str(int(i)), color = plt.cm.plasma((i-1)/n_items), legend = False)
            l.set_xlabel('')


        ## axes formatting
        ax.set_xlim(0,n_trials)
        ax.tick_params(axis='y', labelsize=13)
        ax.set_ylim([0.08,0.92])
        # ax.set_yticklabels(np.linspace(0.1,0.9,5))
        ax.text(.02,.9,' '.join([current_direction, current_model]),
        horizontalalignment='left',
        transform=ax.transAxes,
        fontsize = 15)

        ## shade the post-changepoint area
        _, xmax = ax.get_xlim()
        x_half = np.linspace(0, xmax*6/(6+1),6)[3]
        u = ax.axvspan(xmin = x_half, xmax = xmax, color = 'r', alpha = 0.08)

    axes_formatting(figs, axs)



    ## overall axes and titles
    figs.supxlabel('Block', fontsize = 18)
    figs.supylabel('% chosen', fontsize = 18)
    figs.tight_layout()
    figs.subplots_adjust(wspace=0)
    figs.subplots_adjust(hspace=0)
    figs.suptitle(title, fontsize = 20, y = 1.05)

    # legend using the 7 plotted curves
    handles, labels = ax.get_legend_handles_labels()
    axs[0][-1].legend(handles=handles, labels=labels, loc='upper right', bbox_to_anchor=(1.5, 1), title = 'Item')


    return figs, axs


### SDE plot
def SDE(all_data, subplot_splits, subplot_dims, extremes = True, title = None):

    n_rows = subplot_dims[0]
    n_cols = subplot_dims[1]
    figs, axs = plt.subplots(n_rows,n_cols, figsize = (n_cols * 2.5, n_rows * 3), squeeze=0) #rows cols 

    
    n_items = all_data['Item_1'].max()

    ## loop through models
    for a, ax in enumerate(axs[0]):

        current_direction = subplot_splits[a][0]
        current_model = subplot_splits[a][1]

        if extremes:
            inc_items = np.arange(1,n_items+1)
            x_ticks = np.arange(1,n_items, dtype = int)
        else:
            inc_items = np.arange(2,n_items)
            x_ticks = np.arange(1,n_items-2, dtype = int)

        ## plot SDE (if human, then do acc and RT in one plot)
        if current_model == 'human':

            ## acc
            p = sns.pointplot(data = all_data.loc[
                (all_data['Direction']==current_direction) &
                (all_data['Item_1'].isin(inc_items)) &
                (all_data['Item_2'].isin(inc_items))
                ], x = 'Rank_distance', y = 'Accuracy '+current_model, hue = 'Switched', errorbar='se', ax = axs[0][a])
            p.set(xlabel = None, ylabel = None)
            handles, labels = ax.get_legend_handles_labels()
            p.legend_.remove()
            ax.set_ylim([0.47,0.93])
            ax.set_yticks(ticks = np.linspace(0.5,0.9,5))
            ax.tick_params(axis='y', labelsize=13)
            ax.text(.02,.9,current_model,
                horizontalalignment='left',
                transform=ax.transAxes,
                fontsize = 15)
            ax.text(.02,.8,current_direction,
                horizontalalignment='left',
                transform=ax.transAxes,
                fontsize = 15)
            
            ## RT
            ax = axs[1][a]
            p = sns.pointplot(data = all_data.loc[
                (all_data['Direction']==current_direction) &
                (all_data['Item_1'].isin(inc_items)) &
                (all_data['Item_2'].isin(inc_items))], x = 'Rank_distance', y = 'RT', hue = 'Switched', errorbar='se', ax = axs[1][a])
            p.set(xlabel = None, ylabel = None)
            handles, labels = ax.get_legend_handles_labels()
            p.legend_.remove()
            
            ## axes formatting
            ax.set_ylim([0.90,1.2])
            ax.set_yticks(ticks = np.linspace(0.95,1.15,5))
            ax.tick_params(axis='y', labelsize=13)
            ax.text(.02,.9,current_model,
                horizontalalignment='left',
                transform=ax.transAxes,
                fontsize = 15)
            ax.text(.02,.8,current_direction,
                horizontalalignment='left',
                transform=ax.transAxes,
                fontsize = 15)

        elif current_model != 'human':
            p = sns.pointplot(data = all_data.loc[
                (all_data['Direction']==current_direction) &
                (all_data['Item_1'].isin(inc_items)) &
                (all_data['Item_2'].isin(inc_items))
                ], x = 'Rank_distance', y = 'Accuracy '+current_model, hue = 'Switched', errorbar='se', ax = ax)
            p.set(xlabel = None, ylabel = None)
            handles, labels = ax.get_legend_handles_labels()
            p.legend_.remove()
            
            ## axes formatting
            ax.set_ylim([0.47,0.93])
            ax.set_yticks(ticks = np.linspace(0.5,0.9,5))
            ax.tick_params(axis='y', labelsize=13)
            ax.text(.02,.9,current_model,
                horizontalalignment='left',
                transform=ax.transAxes,
                fontsize = 15)
            ax.text(.02,.8,current_direction,
                horizontalalignment='left',
                transform=ax.transAxes,
                fontsize = 15)
    axes_formatting(figs, axs, x_ticks)

    ## add one legend 
    axs[1][0].legend(handles=handles, labels=labels, loc='upper right', bbox_to_anchor=(0.46, 0.25))
    
    ## overall axes and titles
    supx = figs.text(0.5, 0.02, 'Rank distance', ha='center', va='center', fontsize=16)
    supy = figs.text(0.0, 0.7, 'P(correct)', ha='center', va='center', rotation='vertical', fontsize=16)
    supy = figs.text(0.0, 0.3, 'RT (ms)', ha='center', va='center', rotation='vertical', fontsize=16)
    figs.subplots_adjust(wspace=0)
    figs.subplots_adjust(hspace=0)

    return figs, axs


### plot each and every pair
def all_comparisons(all_data, model = 'human', extremes = True, title = None):

    n_items = 7
    if extremes:
        inc_items= np.arange(1,n_items+1)
        n_distances = n_items-1
    else:
        inc_items= np.arange(2,n_items)
        n_distances = n_items-3
    n_rows = 2
    n_cols = int(n_distances) #i.e. number of distances
    figs, axs = plt.subplots(n_rows,n_cols, figsize = (n_cols * 2.5, n_rows * 3), squeeze=0) #rows cols 

    ## loop through distances
    for d in range(axs.shape[1]):

        ax1 = axs[0][d]
        ax2 = axs[1][d]

        ## plot all pair accs for current distance
        try:
            p1 = sns.pointplot(data = all_data.loc[(all_data['Direction']=='down') 
                                                & (all_data['Rank_distance'] == d+1)
                                                & (all_data['Item_1'].isin(inc_items))
                                                & (all_data['Item_2'].isin(inc_items))
                                                & ((all_data['Block'] >= 3))
                                                # & ((all_data['Block'] == 3) | (all_data['Block']==6))
                                                ], x = 'Losing_Item', y = 'Accuracy '+model, hue = 'Switched', errorbar='se', ax = ax1)#, order=sorted_order)
            p2 = sns.pointplot(data = all_data.loc[(all_data['Direction']=='up') 
                                                & (all_data['Rank_distance'] == d+1)
                                                & (all_data['Item_1'].isin(inc_items))
                                                & (all_data['Item_2'].isin(inc_items))
                                                & ((all_data['Block'] >= 3))
                                                # & ((all_data['Block'] == 3) | (all_data['Block']==6))
                                                ], x = 'Losing_Item', y = 'Accuracy '+model, hue = 'Switched', errorbar='se', ax = ax2)#, order=sorted_order)
        except:
            continue
        p1.set(xlabel = None, ylabel = None)
        p2.set(xlabel = None, ylabel = None)
        p1.set_title('Rank distance = '+str(d+1))
        handles, labels = ax1.get_legend_handles_labels()
        handles, labels = ax2.get_legend_handles_labels()
        p1.legend_.remove()
        p2.legend_.remove()
        
        ## axes formatting (switching some labels where the GT changes, e.g. 7<1)
        xticks = np.array(ax1.get_xticks())+1
        if extremes:
            new_xticks_1 = [str(x)+'<'+str(x+d+1) if x+d+1<8 else str(7)+'<'+str(7-x+1) for x in xticks]
            ax1.set_xticklabels(new_xticks_1, rotation=45)
            new_xticks_2 = [str(x)+'<'+str(x+d+1) if x+d+1<8 else str(x)+'<'+str(1) for x in xticks]
            ax2.set_xticklabels(new_xticks_2, rotation=45)
        else:
            xticks+=1
            new_xticks_1 = [str(x)+'<'+str(x+d+1) if x+d+1<8 else str(7)+'<'+str(7-x+1) for x in xticks]
            ax1.set_xticklabels(new_xticks_1, rotation=45)
            new_xticks_2 = [str(x)+'<'+str(x+d+1) if x+d+1<8 else str(x)+'<'+str(1) for x in xticks]
            ax2.set_xticklabels(new_xticks_2, rotation=45)

        ## make y-axis visible for left-most column only
        for ax in [ax1,ax2]:
            ax.set_ylim([0.37,0.93])
    for ax in axs[:,1:].reshape(-1):
        ax.yaxis.set_visible(False)
    axs[0,0].set_yticks(ticks = np.linspace(0.4,0.9,6))
    axs[1,0].set_yticks(ticks = np.linspace(0.4,0.9,6))
    
    ## overall axes and titles
    axs[0,0].set_ylabel('down', fontsize = 18)
    axs[1,0].set_ylabel('up', fontsize = 18)
    figs.supxlabel('Comparison', fontsize = 18)
    figs.supylabel('P(correct)', fontsize = 18)
    figs.tight_layout()
    figs.subplots_adjust(wspace=0)
    figs.suptitle(model, fontsize = 20, y = 1.05)

    return figs, axs


### plot RTs for adj and non-adj trials
def RT_plot(all_data, subplot_splits, subplot_dims, bin_width, title = None):

    n_rows = subplot_dims[0]
    n_cols = subplot_dims[1]
    figs, axs = plt.subplots(n_rows,n_cols, figsize = (n_cols * 2.5, n_rows * 3), squeeze=0) #rows cols     
    n_items = all_data['Item_1'].max()
    n_trials = all_data['Trial'].max()


    ## loop through models
    for a, ax in enumerate(axs.reshape(-1)):

        current_direction = subplot_splits[a][0]
        current_model = subplot_splits[a][1]

        ## get accuracy for each pair type
        to_plot_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==1)].groupby(['Trial']).mean('RT')['RT']
        to_plot_non_adj = all_data.loc[(all_data['Direction'] == current_direction)&(all_data['Feedback_on']==0)].groupby(['Trial']).mean('RT')['RT']
        
        ## plot
        ax.plot(scipy.ndimage.uniform_filter1d(to_plot_adj, bin_width), lw=3, label = 'Neighb.', color = 'springgreen')
        ax.plot(scipy.ndimage.uniform_filter1d(to_plot_non_adj, bin_width), lw=3, label = 'Non-neighb.', color = 'blue')

        ## axes formatting
        ax.set_xlim(0,n_trials)
        ax.set_ylim([0.9,1.15])
        ax.tick_params(axis='y', labelsize=13)
        ax.text(.02,.9,[current_model,current_direction],
            horizontalalignment='left',
            transform=ax.transAxes,
            fontsize = 15)

    axes_formatting(figs, axs)
    
    ## overall axes and titles
    figs.supxlabel('Block', fontsize = 18)
    figs.supylabel('RT', fontsize = 18)
    figs.tight_layout()
    figs.subplots_adjust(wspace=0)
    figs.subplots_adjust(hspace=0)
    figs.suptitle(title, fontsize = 20, y = 1.05)

    return figs, axs


### plot Q-values
def Q_plot(all_data, subplot_splits, subplot_dims, bin_width=70, step=1, min_periods=1, title = None):

    n_rows = subplot_dims[0]
    n_cols = subplot_dims[1]
    figs, axs = plt.subplots(n_rows,n_cols, figsize = (n_cols * 3, n_rows * 3), squeeze=0) #rows cols 
    n_items = all_data['Item_1'].max()
    n_trials = all_data['Trial'].max()



    ## loop through models
    for a, ax in enumerate(axs.reshape(-1)):
        current_direction = subplot_splits[a][0]
        current_model = subplot_splits[a][1]
        Q_maxs = []
        Q_mins = []

        ## loop through items (do them in reverse order so that the legend is in the right order)
        for Q in np.arange(n_items-1,-1,-1):
            
            ## if human, plot choice ratios
            if current_model == 'human':
                to_plot_Q = all_data.loc[(all_data['Direction']==current_direction)
                                    #    &(all_data['Feedback_on']==0)
                                    ].groupby(['Trial']).mean('Item_'+str(int(Q+1))+'_chosen')['Item_'+str(int(Q+1))+'_chosen']
                to_plot_Q = to_plot_Q.rolling(window=70, center=True, min_periods=min_periods, step=step).mean()
            
            ## if model, plot Q-values 
            else:
                to_plot_Q = all_data.loc[all_data['Direction'] == current_direction].groupby(['Trial']).mean(current_model + ' item ' + str(int(Q+1)))[current_model + ' item ' + str(int(Q+1))]
                to_plot_Q = to_plot_Q.rolling(window=bin_width, center=True, min_periods=min_periods, step=step).mean()
                Q_maxs.append(to_plot_Q.max())
                Q_mins.append(to_plot_Q.min())

            # plot
            l = sns.lineplot(x = to_plot_Q.index, y=to_plot_Q.values, ax = ax, lw=3.5, label = str(int(Q+1)), color = plt.cm.plasma(Q/n_items), legend = False)
            l.set_xlabel('')


        ## axes formatting
        ax.set_xlim(0,n_trials)
        ax.tick_params(axis='y', labelsize=13)
        if current_model == 'human':
            ax.set_yticks(ticks = np.linspace(0.1,0.9,5))
        else:
            first_Q = to_plot_Q.iloc[0]
            if to_plot_Q.iloc[0]<-0.2:
                ax.set_yticks(ticks = np.linspace(-0.75,0.75,5), labels = np.linspace(-0.5,1.5,5))
            else:
                ax.set_yticks(ticks = np.linspace(-0.9,0.9,5), labels = np.linspace(-1,1,5))
        ax.text(.02,.9,current_model,
            horizontalalignment='left',
            transform=ax.transAxes,
            fontsize = 15,
            fontstyle='italic')
        ax.text(.02,.8,current_direction,
            horizontalalignment='left',
            transform=ax.transAxes,
            fontsize = 15)

        ## shade the post-changepoint area
        _, xmax = ax.get_xlim()
        x_half = np.linspace(0, xmax*6/(6+1),6)[3]
        u = ax.axvspan(xmin = x_half, xmax = xmax, color = 'r', alpha = 0.08)

    axes_formatting(figs, axs)



    ## overall axes and titles
    supx = figs.text(0.57, -0.03, 'Block', ha='center', va='center', fontsize=18)
    figs.supylabel('Q value (a.u.)', fontsize = 18)
    figs.tight_layout()
    figs.subplots_adjust(wspace=0)
    figs.subplots_adjust(hspace=0)
    figs.suptitle(title, fontsize = 20, y = 1.05)

    # legend using the 7 plotted curves
    handles, labels = ax.get_legend_handles_labels()
    axs[0][-1].legend(handles=handles, labels=labels, loc='upper right', bbox_to_anchor=(1.3, 1.025), title = 'Item')


    return figs, axs


## violin plot of model evidence
def plot_evidence(evidence, evidence_name = 'AIC'):
    
    ## prepare data
    moi = list(evidence.keys())
    collapse_evidence = evidence[moi].melt(var_name = 'model',value_name = evidence_name, ignore_index = False)
    collapse_evidence['Participant'] = collapse_evidence.index.get_level_values('Participant')
    collapse_evidence['Direction'] = collapse_evidence.index.get_level_values('Direction')

    ## get each possible pair of models within each direction
    moi_pairs = list(itertools.combinations(moi, 2))
    moi_pairs = [list(pair) for pair in moi_pairs]
    box_pairs = []
    for d in ['down','up']:
        for pair in moi_pairs:
            box_pairs.append(((d,pair[0]), (d,pair[1])))

    ## plot
    fig = plt.figure(figsize = (5,8))
    p = sns.violinplot(data=collapse_evidence.loc[collapse_evidence['model'].isin(moi)], x='Direction', y=evidence_name, hue='model', inner='quartile', palette = 'rocket', linewidth=2)
    p.set_xlabel('Direction', fontsize = 18)
    p.set_xticklabels(['Up','Down'], fontsize = 16)
    p.set_ylabel(evidence_name, fontsize = 18)
    p.set_ylim([0, p.get_ylim()[1]])
    p.set_yticks(ticks = np.linspace(0,500,6), labels = np.linspace(0,500,6, dtype=int),fontsize = 16)
    legend = p.legend(title='Model', loc='lower center', fontsize=10, bbox_to_anchor=(0.6, 0))

    ## formatting (useful if using old version of sns??)
    for artist in p.collections:
        artist.set_alpha(0.85)
    for line in p.lines:
        # line.set_color("white")
        line.set_linewidth(2)  # Adjust the linewidth if necessary
    for text in legend.get_texts():
        if text.get_text() == "Q-asymm_m2":
            text.set_text("Q-asymm²")
        text.set_fontstyle('italic')

    # add stars for significance
    annotator = Annotator(p, box_pairs, data=collapse_evidence.loc[collapse_evidence['model'].isin(moi)], x='Direction', y=evidence_name, hue='model')
    annotator.configure(test='Wilcoxon', text_format='star', loc='outside', comparisons_correction='bonferroni',
                        line_height=0.005,  
                        line_offset_to_group=0.001,
                        # pvalue_thresholds=[(0.05, "*"), (0.01, "**"), (0.001, "***")], 
                        hide_non_significant=True
                        )
    annotator.apply_and_annotate()
    
    return fig, p

## plot pxp
def plot_pxp(df_pxp):
    directions = ['up','down']
    figs_pxp, ax = plt.subplots(1,1, figsize = (5,8))
    sns.barplot(data = df_pxp, x = 'Direction', y = 'pxp', hue = 'model',order =directions, ax = ax, alpha=1,  linewidth = 2, palette = 'rocket')
    sns.swarmplot(data = df_pxp, x = 'Direction', y = 'freq', hue = 'model',order =directions, ax = ax, alpha=1, marker = 'd', size=13, color = 'black', dodge = True, legend = False)
    ax.set_ylim(0,1)
    ax.set_ylabel('')
    ax.set_yticks([])
    ax.set_xlabel('Direction', fontsize = 18)
    ax.set_xticklabels(['Up','Down'], fontsize = 14)
    plt.figure()
    sns.barplot(data = df_pxp, x = 'model', y = 'pxp', hue = 'model', alpha=1,  linewidth = 2, palette = 'rocket', legend = True)
    ax.set_yticks(ticks = np.linspace(0,1,5), labels = np.linspace(0,1,5),fontsize = 12)
    ax.set_ylabel('pxp', fontsize = 16)
    legend = ax.legend(loc='upper left',  fontsize = 10, title = 'Model')
    for text in legend.get_texts():
        if text.get_text() == "Q-asymm_m2":
            text.set_text("Q-asymm²")
        text.set_fontstyle('italic')

    return figs_pxp, ax

### make axes visible/invisible
def axes_formatting(figs, axs, x_tick_labels = np.arange(1,7)):

    ## make x-axis visible for bottom row only
    for ax in axs[-1, :]:
        xmin, xmax = ax.get_xlim()
        if xmin>=0:
            n_xticks = len(x_tick_labels)
            tick_starts = np.linspace(0, xmax*n_xticks/(n_xticks+1),n_xticks)
            ax.set_xticks(ticks = tick_starts, labels = x_tick_labels, fontsize = 13)

        ## HACKY FOR REL TRIALS: ticks from -150, 0, 150
        elif xmin<0:
            x_tick_labels = np.round(np.linspace(-150, 150, 3)).astype(int)
            n_xticks = len(x_tick_labels)
            tick_starts = x_tick_labels
            ax.set_xticks(ticks = tick_starts, labels = x_tick_labels, fontsize = 12)

    try:
        for ax in axs[:-1, :].squeeze():
            ax.xaxis.set_visible(False)
    except:
        pass

    ## make y-axis visible for left-most column only
    for ax in axs[:,1:].reshape(-1):
        ax.yaxis.set_visible(False)

## calculate and plot choice matrices
def plot_cm(all_data, split_method, vmin = 0.1, vmax = 0.9, plot_setting = 1, type = 'acc', current_model = 'human'):
    
    """
    plot setting determines how the data is divided up
    1: plot a 2x2 set of subplots, pre x post and up x down
    2: plot up and down pre-data all together, and then split the post data by direction
    3: plot the change in choice probabilities from pre vs post for each direction
    """

    ## init
    pre_post = ['Pre','Post']
    directions = ['up','down']
    n_items = int(all_data['Item_1'].max())
    alphabet = np.array(['A','B','C','D','E','F','G','H'])
    alphabet = alphabet[:int(n_items)]
        
    ## split pre-switch data by direction, creating one large 2x2 plot
    if plot_setting == 1:
        if split_method == 'halfway':
            figs, axs = plt.subplots(2,2, figsize = (2*3,2*3), squeeze=0) #rows cols

            ## loop through directions
            for di, d in enumerate(directions):

                ## loop through splits
                for si, switch in enumerate(['pre','post']):
                    ax = axs[si,di]
                    if type == 'acc':
                        toplot = all_data.loc[(all_data['Direction']==d)
                                            &(all_data['Switched']==switch)].pivot_table(index='Largest_number', columns='Smallest_number', values='Accuracy '+current_model, aggfunc='mean', fill_value=0)
                    elif type == 'prob':
                        toplot = all_data.loc[(all_data['Direction']==d)
                                            &(all_data['Switched']==switch)].pivot_table(index='Largest_number', columns='Smallest_number', values='Largest_chosen_'+current_model, aggfunc='mean', fill_value=0)
                    toplot = toplot.replace(0, np.nan)
                    print(np.nanmin(toplot), np.nanmax(toplot))

                    ## imshow
                    pos = ax.imshow(toplot, extent=[0, 1, 0, 1], vmin = vmin, vmax = vmax)#, cmap = 'plasma')
                    ax.set_xticks(ticks = np.linspace(1/(n_items*2), (n_items*2-1)/(n_items*2), n_items),labels = np.arange(1,n_items+1))
                    ax.set_yticks(ticks = np.linspace((n_items*2-1)/(n_items*2), 1/(n_items*2),n_items),labels = np.arange(1,n_items+1))
                    ax.set_xlabel('Item x', fontsize = 12)
                    ax.set_ylabel('Item y', fontsize = 12)
                    
                    #remove axis outline
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)
                    ax.spines['left'].set_visible(False)
                    ax.spines['bottom'].set_visible(False)
                    
                    ## heatmap option...
                    
                    #flip the colors
                    # toplot *= -1 
                    # vmax *= -1
                    # vmin *= -1
                    # print(si, len(splits-1))
                    # if si == len(splits)-1:
                    #     cbar_on = True
                    #     print('hell')
                    # else:
                    #     cbar_on = False
                    # cbar_on = False
                    # pos = sns.heatmap(toplot, ax=ax, vmin = vmin, vmax = vmax, annot=False, square = True, cbar = cbar_on, xticklabels = np.arange(1,n_items+1),yticklabels = np.arange(1,n_items+1),
                    #                 #   cbar_kws={'label': 'P(i<j)', 'orientation': 'vertical', 'shrink': 1, 'ticks': np.linspace(vmin,vmax,5)}
                    # )
                    # ax.set_xlabel('Item i', fontsize = 12)
                    # ax.set_ylabel('Item j', fontsize = 12)
                
                

                ## titles for top row
                for i, ax in enumerate(axs[0,:]):
                    ax.set_title(''.join([pre_post[i], '-changepoint']), fontsize = 13, pad = 10)

        ## more formatting    
        plt.tight_layout()
        plt.figure()
        c = figs.colorbar(pos, ax=axs.ravel().tolist(), shrink = 0.4)
        c.mappable.set_clim(vmin=vmin,vmax=vmax) 
        if type == 'acc':
            c.ax.set_title('P(correct)', fontsize = 12, pad = 10)
        else:
            c.ax.set_title('P(i<j)', fontsize = 12, pad = 10)
        n_labels = 4
        c.ax.set_yticks(ticks = np.linspace(vmin,vmax,n_labels), labels = np.round(np.linspace(vmin,vmax,n_labels), 2))
        
        # set direction title in the middle of the x-length of this row
        figs.text(0.45, 1, ' '.join([current_model, directions[0]]), ha='center', va='center', fontsize=16)

        return figs, axs


    ## create two plots: one containing pre-switch data across both groups, and another 2x1 plot containing post-switch data separated by group
    elif plot_setting == 2:
        figs, axs = plt.subplots(2,2, figsize = (8,8), squeeze=0) #rows cols

        ### plot pre-switch data across both groups
        if type == 'acc':
            toplot = all_data.loc[
                                (all_data['Switched']=='pre')].pivot_table(index='Largest_number', columns='Smallest_number', values='Accuracy '+current_model, aggfunc='mean', fill_value=0)
        elif type == 'prob':
            if current_model == 'human':
                toplot = all_data.loc[
                                (all_data['Switched']=='pre')].pivot_table(index='Largest_number', columns='Smallest_number', values='Largest_chosen_'+current_model, aggfunc='mean', fill_value=0)
            else:
                toplot = all_data.loc[
                                (all_data['Switched']=='pre')].pivot_table(index='Largest_number', columns='Smallest_number', values='Largest_CP_'+current_model, aggfunc='mean', fill_value=0)
        toplot = toplot.replace(0, np.nan)
        print(np.nanmin(toplot), np.nanmax(toplot))
        ax = axs[0,0]


        ## imshow option...
        # pos = ax.imshow(toplot, extent=[0, 1, 0, 1], vmin = vmin, vmax = vmax)#, cmap = 'plasma')
        # ax.set_xticks(ticks = np.linspace(1/(n_items*2), (n_items*2-1)/(n_items*2), n_items),labels = np.arange(1,n_items+1),fontsize = 12)
        # ax.set_yticks(ticks = np.linspace((n_items*2-1)/(n_items*2), 1/(n_items*2),n_items),labels = np.arange(1,n_items+1),fontsize = 12)
        # ax.set_xlabel('Item x', fontsize = 15)
        # ax.set_ylabel('Item y', fontsize = 15)

        ##sns heatmap
        cbar=False
        pos = sns.heatmap(toplot, ax=ax, vmin = vmin, vmax = vmax, annot=False, square = True, cbar = cbar, fmt='.2f', cmap='viridis',
                        #   annot_kws={'weight': 'bold', 'fontsize': 'small'},
                        #   cbar_kws={'label': 'Pre vs post change in P(x<y)', 'orientation': 'vertical', 'ticks': np.linspace(vmin,vmax,5)}
            )
        
        ## formatting
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.set_xticks(ticks = np.arange(1,n_items)-0.5, labels = np.arange(1,n_items), fontsize = 12)
        ax.set_yticks(ticks = np.arange(1,n_items)-0.5, labels = np.arange(2,n_items+1), fontsize = 12)
        ax.set_xlabel('Item x', fontsize = 14)
        ax.set_ylabel('Item y', fontsize = 14)
        ax.set_title('Pre-changepoint \nall participants', fontsize = 18, pad = 10, loc = 'left')
        


        ### plot post-switch data separated by group
        for di, d in enumerate(directions):
            if type == 'acc':
                toplot = all_data.loc[(all_data['Direction']==d)
                                    &(all_data['Switched']=='post')].pivot_table(index='Largest_number', columns='Smallest_number', values='Accuracy '+current_model, aggfunc='mean', fill_value=0)
            elif type == 'prob':
                if current_model == 'human':
                    toplot = all_data.loc[(all_data['Direction']==d)
                                        &(all_data['Switched']=='post')].pivot_table(index='Largest_number', columns='Smallest_number', values='Largest_chosen_'+current_model, aggfunc='mean', fill_value=0)
                else:
                    toplot = all_data.loc[(all_data['Direction']==d)
                                        &(all_data['Switched']=='post')].pivot_table(index='Largest_number', columns='Smallest_number', values='Largest_CP_'+current_model, aggfunc='mean', fill_value=0)
            toplot = toplot.replace(0, np.nan)
            print(np.nanmin(toplot), np.nanmax(toplot))
            ax = axs[1,di]

            ## imshow option...
            # pos = ax.imshow(toplot, extent=[0, 1, 0, 1], vmin = vmin, vmax = vmax)
            # ax.set_xticks(ticks = np.linspace(1/(n_items*2), (n_items*2-1)/(n_items*2), n_items),labels = np.arange(1,n_items+1), fontsize = 12)
            # ax.set_yticks(ticks = np.linspace((n_items*2-1)/(n_items*2), 1/(n_items*2),n_items),labels = np.arange(1,n_items+1), fontsize = 12)
            # ax.set_xlabel('Item x', fontsize = 15)
            # ax.set_ylabel('Item y', fontsize = 15)

            ##sns heatmap
            cbar=False
            pos = sns.heatmap(toplot, ax=ax, vmin = vmin, vmax = vmax, annot=False, square = True, cbar = cbar, fmt='.2f', cmap='viridis',
                            #   annot_kws={'weight': 'bold', 'fontsize': 'small'},
                            #   cbar_kws={'label': 'Pre vs post change in P(x<y)', 'orientation': 'vertical', 'ticks': np.linspace(vmin,vmax,5)}
                )
            
            # cbar title
            

            ## formatting
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.set_xticks(ticks = np.arange(1,n_items)-0.5, labels = np.arange(1,n_items), fontsize = 12)
            ax.set_yticks(ticks = np.arange(1,n_items)-0.5, labels = np.arange(2,n_items+1), fontsize = 12)
            ax.set_xlabel('Item x', fontsize = 14)
            ax.set_ylabel('Item y', fontsize = 14)
            ax.set_title('Post-changepoint \n'+d, fontsize = 18, pad = 10, loc = 'left')

        
        ## hide the top right plot
        axs[0,1].axis('off')
        plt.tight_layout()
        plt.figure()
        
        ## suptitle 
        if current_model == 'Q-asymm_m2':
            title = 'Q-asymm²'
        else:
            title = current_model
        figs.suptitle(title, fontsize = 20, y = 1.05, fontstyle = 'italic')

        ## colorbar if using imshow
        # c = figs.colorbar(pos, ax=axs.ravel().tolist(), shrink = 0.4)
        # c = figs.colorbar(pos, ax=axs[0,1], shrink = 1)
        # c.mappable.set_clim(vmin=vmin,vmax=vmax) 
        # c = figs.colorbar(pos, ax=axs[0,1], shrink = 1, location = 'left')
        # c.mappable.set_clim(vmin=vmin,vmax=vmax) 
        # if type == 'acc':
        #     # c.ax.set_title('Pre vs post \nchange in P(x<y)', fontsize = 15, pad = 10)
        #     c.ax.set_title('P(correct)', fontsize = 15, pad = 10)
        # else:
        #     c.ax.set_title('P(x<y)', fontsize = 15, pad = 10)
        # n_labels = 4
        # c.ax.set_yticks(ticks = np.linspace(vmin,vmax,n_labels), labels = np.round(np.linspace(vmin,vmax,n_labels), 2))

        plt.subplots_adjust(hspace = 0.5, wspace = 0.5)

        return figs, axs
    

    elif plot_setting==3:
        figs, axs = plt.subplots(2,2, figsize = (8,8), squeeze=0)
        
        ## loop through directions
        for di, d in enumerate(directions):

            ## loop through human and then model
            for mi, model in enumerate(['human', current_model]):
                ax = axs[mi,di]

                ## get average of pre vs post difference
                pre_block = 0
                if type =='prob':
                    if model == 'human':
                        toplot_pre = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='pre')
                                                &(all_data['Block']>=pre_block)
                                                ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Largest_chosen_'+model, aggfunc=np.nanmean, fill_value=0)
                        toplot_post = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='post')
                                                #   &(all_data['Block']==6)
                                                    ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Largest_chosen_'+model, aggfunc=np.nanmean, fill_value=0)
                    else:
                        toplot_pre = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='pre')
                                                &(all_data['Block']>=pre_block)
                                                ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Largest_CP_'+model, aggfunc=np.nanmean, fill_value=0)
                        toplot_post = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='post')
                                                #   &(all_data['Block']==6)
                                                    ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Largest_CP_'+model, aggfunc=np.nanmean, fill_value=0)
                elif type == 'acc':
                    if model == 'human':
                        toplot_pre = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='pre')
                                                &(all_data['Block']>=pre_block)
                                                ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Accuracy '+model, aggfunc=np.nanmean, fill_value=0)
                        toplot_post = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='post')
                                                #   &(all_data['Block']==6)
                                                    ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Accuracy '+model, aggfunc=np.nanmean, fill_value=0)
                    else:
                        toplot_pre = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='pre')
                                                &(all_data['Block']>=pre_block)
                                                ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Accuracy '+model, aggfunc=np.nanmean, fill_value=0)
                        toplot_post = all_data.loc[(all_data['Direction']==d)
                                                &(all_data['Switched']=='post')
                                                #   &(all_data['Block']==6)
                                                    ].pivot_table(index='Participant', columns=['Largest_number', 'Smallest_number'], values='Accuracy '+model, aggfunc=np.nanmean, fill_value=0)
                differences = toplot_post - toplot_pre
                differences = differences.replace(0, np.nan)
                toplot = pd.DataFrame(np.nan, index = np.arange(1,8), columns = np.arange(1,8))
                for i1 in np.arange(1,8):
                    for i2 in np.arange(1,8):
                        if (i1,i2) in differences.columns:
                            toplot.loc[i1,i2] = differences[(i1,i2)].mean()
                print(np.nanmin(toplot), np.nanmax(toplot))
                ## remove top row and last column
                toplot = toplot.iloc[1:, :-1]

                ## plot
                cbar = True
                cbar = False
                pos = sns.heatmap(toplot, ax=ax, vmin = vmin, vmax = vmax, annot=True, square = True, cbar = cbar, fmt='.2f',
                            annot_kws={'weight': 'bold', 'fontsize': 'medium', 'color': 'black'},
                            cmap='coolwarm_r'
                            #   cbar_kws={'label': 'Pre vs post change in P(x<y)', 'orientation': 'vertical', 'ticks': np.linspace(vmin,vmax,5)}
                )
                print(vmin, vmax)
                for text in pos.texts:
                    color, weight = text_color_and_weight(float(text.get_text()))
                    text.set_color(color)
                    text.set_weight(weight)
                ax.set_xticks(ticks = np.arange(1,n_items)-0.5, labels = np.arange(1,n_items), fontsize = 12)
                ax.set_yticks(ticks = np.arange(1,n_items)-0.5, labels = np.arange(2,n_items+1), fontsize = 12)
                ax.set_xlabel('Item x', fontsize = 14)
                ax.set_ylabel('Item y', fontsize = 14)
                # ax.set_title(model+'\n('+d+')', fontsize=18, pad=10, loc='left')#, fontstyle = 'italic')
                ax.set_title(d, fontsize=18, pad=10, loc='left')#, fontstyle = 'italic')

            
        # plt.suptitle(current_model, fontsize = 18, fontstyle = 'italic', x = 0.4)


    plt.tight_layout()
    if current_model == 'Q-asymm_m2':
        title = 'Q-asymm²'
    else:
        title = current_model
    plt.suptitle(title, fontsize = 20, y = 1.05, fontstyle = 'italic')
    # plt.suptitle(current_model)
    plt.figure()

    return figs, axs
    
def text_color_and_weight(val):
    if val >= 0:
        return 'black', 'normal'
    else:
        return 'white', 'bold'
    
## another method of calculating and plotting CMs...
def plot_pivot_cm(all_data, vmin = 0.1, vmax = 0.9, type = 'acc', current_model = 'human'):

    directions = all_data['Direction'].unique()
    n_items = all_data['Item_1'].max()

    # alphabet = np.array(['A','B','C','D','E','F','G','H'])
    # alphabet = alphabet[:n_items]
    figs, axs = plt.subplots(2,2, figsize = (10,20), squeeze=0) #rows cols

    ## loop through switches
    for si, switch in enumerate(['pre','post']):

        ## loop through directions
        for di, d in enumerate(directions):
        
            #pivot data
            toplot = all_data.loc[(all_data['Direction']==d)
                                   &(all_data['Switched']==switch)].pivot_table(index='Largest_number', columns='Smallest_number', values='Largest_chosen_'+current_model, aggfunc='mean', fill_value=0)
            toplot = toplot.replace(0, np.nan)

            print(np.nanmin(toplot), np.nanmax(toplot))
            ax = axs[si,di]
            cbar_on = True
            pos = sns.heatmap(toplot, ax=ax, vmin = vmin, vmax = vmax, annot=True, square = True, cbar = cbar_on, xticklabels = np.arange(1,n_items+1),yticklabels = np.arange(1,n_items+1), fmt='.2f',
                            annot_kws={'weight': 'bold', },
                            cbar_kws={'label': 'P(i<j)', 'orientation': 'vertical', 'shrink': 0.1, 'ticks': np.linspace(vmin,vmax,5)}
            )
            for text in pos.texts:
                color, weight = text_color_and_weight(float(text.get_text()))
                text.set_color(color)
                text.set_weight(weight)
            ax.set_xlabel('Item i', fontsize = 12)
            ax.set_ylabel('Item j', fontsize = 12)
    


        ax.set_title(d, fontsize = 13, pad = 10)

        
    plt.tight_layout()
    plt.figure()


### param boxplots
def param_boxplot(df_fits, current_model, current_params, title = None):
        n_params = len(current_params)
        fig, axs = plt.subplots(1, n_params, figsize = (n_params+5,5)) #can also use int(np.ceil(n_params/2)) for
        fig.suptitle(current_model)
        par_n = 0
        to_plot = df_fits[current_model][np.append(current_params, 'Direction')].melt(var_name = 'param', id_vars = 'Direction')
        for par, param in enumerate(current_params):
            ax = axs[par]
            p = sns.boxplot(data = to_plot.loc[to_plot['param'] == param], x = 'param', y = 'value', hue = 'Direction', hue_order=['down','up'], ax=ax, boxprops=dict(alpha=.3))
            sns.swarmplot(data = to_plot.loc[to_plot['param'] == param], x = 'param', y = 'value', hue = 'Direction', hue_order=['down','up'], ax=ax, size = 5, dodge=True)
            # ax.set_title(param)
            par_n += 1
            if param == 'a1' or param == 'a2':
                min = np.min(np.array([to_plot.loc[to_plot['param'] == param, 'value'].min(),-0.02]))
                ax.set_ylim([min,0.5])

            # remove x axis label
            ax.set_xlabel(param)
            ax.set_xticklabels([])
            ax.set_xticks([])
            
            ## plot and print significance (depends on sns version...!)
            # test_results = statannot.add_stat_annotation(p, data=to_plot.loc[to_plot['param'] == param], x='param', y='value', hue='Direction',
            #                        box_pairs=[((param, "down"), (param, "up"))],
            #                        test='t-test_ind', text_format='star',
            #                        loc='outside', verbose=0)            

            if par == n_params-1:
                handles, labels = ax.get_legend_handles_labels()
                ax.legend(handles[0:2], labels[0:2], frameon=False, loc=(1,0.8))
            else:
                ax.get_legend().remove()

            
        print()
        plt.tight_layout()

## plot changes in preference for anchor items
def pref_change(all_data, model = 'human', df_prefs = None, plot = False):

    ## init
    participants = np.unique(all_data['Participant'])
    blocks = np.unique(all_data['Block'])
    directions = np.unique(all_data['Direction'])
    if df_prefs is None:
        prefs = {}
        prefs['Participant'] = []
        prefs['Direction'] = []
        prefs['Block'] = []
        prefs[model+' 1'] = []
        prefs[model+' 7'] = []
    
    ## calculate preferences
    for p in participants:
        for b in blocks:
            data = all_data.loc[(all_data['Participant']==p) & (all_data['Block']==b)]
            prefs['Participant'].append(p)
            prefs['Direction'].append(data['Direction'].iloc[0])
            prefs['Block'].append(b)
            for i in [1,7]:
                if model == 'human':
                    prefs[model+ ' '+str(i)].append(np.mean(data.loc[
                        ((data['Item_1']==i) | (data['Item_2']==i))
                        & (data['Item_distance']<6)
                        # & (data['Feedback_on']==0)
                        ]['Chosen_Item']==i))
                else:
                    prefs[model+ ' '+str(i)].append(np.mean(
                        np.concatenate([
                            1-data.loc[(data['Item_1']==i)& (data['Item_distance']<6)
                                    #    & (data['Feedback_on']==0)
                                       ]['CP '+model],
                            data.loc[(data['Item_2']==i)& (data['Item_distance']<6)
                                    #  & (data['Feedback_on']==0)
                                     ]['CP '+model]
                        ])
                        )
                    )
        for switch in ['pre','post']:
            data = all_data.loc[(all_data['Participant']==p) & (all_data['Switched']==switch)]
            prefs['Participant'].append(p)
            prefs['Direction'].append(data['Direction'].iloc[0])
            prefs['Block'].append(switch)
            for i in [1,7]:
                if model == 'human':
                    prefs[model+ ' '+str(i)].append(np.mean(data.loc[
                        ((data['Item_1']==i) | (data['Item_2']==i))
                        &(data['Item_distance']<6)
                        & (data['Feedback_on']==0)
                        ]['Chosen_Item']==i))
                else:
                    prefs[model+ ' '+str(i)].append(np.mean(
                        np.concatenate([
                            1-data.loc[(data['Item_1']==i)
                                       & (data['Item_distance']<6)
                                        # & (data['Feedback_on']==0)
                                       ]['CP '+model],
                            data.loc[(data['Item_2']==i)
                                     & (data['Item_distance']<6)
                                        # & (data['Feedback_on']==0)
                                     ]['CP '+model]
                        ])
                        )
                    )
                

    #convert to df
    df_prefs = pd.DataFrame.from_dict(prefs)

    ## single plot, where hue gives the colour, and linestyle gives the item. to do this, we need to melt the df, so that we have a column for the item number
    df_prefs_melted = df_prefs.melt(id_vars = ['Participant','Direction','Block'], var_name = 'Item', value_name = 'Preference')
    df_prefs_melted['Item'] = df_prefs_melted['Item'].str.split(' ').str[1].astype(int)
    if plot:
        fig, ax = plt.subplots(1,1, figsize = (4,4))
        toplot = df_prefs_melted.loc[df_prefs_melted['Block'].isin(np.arange(1,7))]
        sns.lineplot(data = toplot, x = 'Block', y = 'Preference', hue = 'Direction', style = 'Item', ax = ax)
        ax.set_ylim([0,1])
        ax.set_xticks(ticks = np.arange(1,7), labels = np.arange(1,7), fontsize = 13)
        ax.set_yticks(ticks = np.linspace(0,1,6), labels = np.round(np.linspace(0,1,6),2), fontsize = 13)
        ax.set_xlabel('Block', fontsize = 15)
        ax.set_ylabel('P(item chosen)', fontsize = 15)

        ## legend
        legend = ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1.03), fontsize=12)
        for text in legend.get_texts():
            if text.get_text() == 'Direction' or text.get_text() == 'Item':
                pass
            else:
                text.set_fontstyle('italic')
                text.set_fontsize(10)

        ## repeat, but for pre vs post
        fig, ax = plt.subplots(1,1, figsize = (4,4))
        toplot = df_prefs_melted.loc[(df_prefs_melted['Block']=='pre') | (df_prefs_melted['Block']=='post')]
        sns.lineplot(data =toplot, x = 'Block', y = 'Preference', hue = 'Direction', style = 'Item', ax = ax)
        ax.set_ylim([0,1])
        ax.set_xticks(ticks = np.arange(0,2), labels = ['Pre','Post'], fontsize = 13)
        ax.set_yticks(ticks = np.linspace(0,1,6), labels = np.round(np.linspace(0,1,6),2), fontsize = 13)
        ax.set_xlabel('Block', fontsize = 15)
        ax.set_ylabel('P(item chosen)', fontsize = 15)

        ## legend
        legend = ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1.03), fontsize=12)
        for text in legend.get_texts():
            if text.get_text() == 'Direction' or text.get_text() == 'Item':
                pass
            else:
                text.set_fontstyle('italic')
                text.set_fontsize(10)

        
        ## repeat, but for all trials with rolling average
        if model == 'human':
            fig, ax = plt.subplots(1,1, figsize = (4,4))
            hues = sns.color_palette('tab10', n_colors = 2)
            linestyles = ['solid','dashed']
            for di, d in enumerate(directions):
                for ii, i in enumerate([1,7]):
                    to_plot = all_data.loc[((all_data['Item_1']==i) | (all_data['Item_2']==i))
                                        & (all_data['Item_distance']<6)
                                        & (all_data['Direction']==d)]
                    to_plot['anchor_chosen'] = to_plot['Chosen_Item'] == i
                    to_plot = to_plot.groupby(['Trial']).mean('anchor_chosen')['anchor_chosen']
                    to_plot = to_plot.rolling(window=100).mean()
                    to_plot = to_plot.reindex(np.arange(1,all_data['Trial'].max()+1))
                    sns.lineplot(x = to_plot.index, y = to_plot.values, ax = ax, lw=3.5,label = i, color = hues[di], linestyle = linestyles[ii])
            ax.set_ylim([0,1])

        




    

        

    ## add another column that indicates whether the anchor was moved or unmoved, depending on the direction
    df_prefs[model+' moved'] = np.zeros(len(df_prefs))
    df_prefs[model+' unmoved'] = np.zeros(len(df_prefs))
    df_prefs.loc[df_prefs['Direction'] == 'up', model+' moved'] = df_prefs.loc[df_prefs['Direction'] == 'up', model+' 1']
    df_prefs.loc[df_prefs['Direction'] == 'down', model+' moved'] = 1-df_prefs.loc[df_prefs['Direction'] == 'down', model+' 7']
    df_prefs.loc[df_prefs['Direction'] == 'up', model+' unmoved'] = df_prefs.loc[df_prefs['Direction'] == 'up', model+' 7']
    df_prefs.loc[df_prefs['Direction'] == 'down', model+' unmoved'] = df_prefs.loc[df_prefs['Direction'] == 'down', model+' 1']

    ## calculate changes in preference for a) block 3 vs post-switch, or b) pre-switch vs post-switch, or c) block 3 vs each post-switch block   
    df_prefs[model+ ' 1 change 3 vs post'] = np.zeros(len(df_prefs))
    df_prefs[model+ ' 7 change 3 vs post'] = np.zeros(len(df_prefs))
    df_prefs[model+ ' 1 change pre vs post'] = np.zeros(len(df_prefs))
    df_prefs[model+ ' 7 change pre vs post'] = np.zeros(len(df_prefs))
    df_prefs[model + ' moved anchor change 3 vs post'] = np.zeros(len(df_prefs))
    df_prefs[model + ' unmoved anchor change 3 vs post'] = np.zeros(len(df_prefs))
    df_prefs[model + ' moved anchor change pre vs post'] = np.zeros(len(df_prefs))
    df_prefs[model + ' unmoved anchor change pre vs post'] = np.zeros(len(df_prefs))
    for p in participants:

        #halfway
        df_prefs.loc[(df_prefs['Participant']==p), model+ ' 1 change pre vs post'] = df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']=='post'), model+ ' 1'].iloc[0] - df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']=='pre'), model+ ' 1'].iloc[0]
        df_prefs.loc[(df_prefs['Participant']==p), model+ ' 7 change pre vs post'] = df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']=='post'), model+ ' 7'].iloc[0] - df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']=='pre'), model+ ' 7'].iloc[0]
        df_prefs.loc[(df_prefs['Participant']==p), model+ ' 1 change 3 vs post'] = df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']=='post'), model+ ' 1'].iloc[0] - df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']==3), model+ ' 1'].iloc[0]
        df_prefs.loc[(df_prefs['Participant']==p), model+ ' 7 change 3 vs post'] = df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']=='post'), model+ ' 7'].iloc[0] - df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']==3), model+ ' 7'].iloc[0]

        #blockwise
        for bi, b in enumerate([4,5,6]):
            df_prefs.loc[(df_prefs['Participant']==p), model+ ' 1 change '+str(b)+' vs 3'] = df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']==b), model+ ' 1'].iloc[0] - df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']==3), model+ ' 1'].iloc[0]
            df_prefs.loc[(df_prefs['Participant']==p), model+ ' 7 change '+str(b)+' vs 3'] = df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']==b), model+ ' 7'].iloc[0] - df_prefs.loc[(df_prefs['Participant']==p)&(df_prefs['Block']==3), model+ ' 7'].iloc[0]
    
    df_prefs.loc[df_prefs['Direction'] == 'down', model + ' moved anchor change pre vs post'] = df_prefs.loc[df_prefs['Direction'] == 'down', model + ' 7 change pre vs post']
    df_prefs.loc[df_prefs['Direction'] == 'up', model + ' moved anchor change pre vs post'] = df_prefs.loc[df_prefs['Direction'] == 'up', model + ' 1 change pre vs post']
    df_prefs.loc[df_prefs['Direction'] == 'down', model + ' unmoved anchor change pre vs post'] = df_prefs.loc[df_prefs['Direction'] == 'down', model + ' 1 change pre vs post']
    df_prefs.loc[df_prefs['Direction'] == 'up', model + ' unmoved anchor change pre vs post'] = df_prefs.loc[df_prefs['Direction'] == 'up', model + ' 7 change pre vs post']
    df_prefs.loc[df_prefs['Direction'] == 'down', model + ' moved anchor change 3 vs post'] = df_prefs.loc[df_prefs['Direction'] == 'down', model + ' 7 change 3 vs post']
    df_prefs.loc[df_prefs['Direction'] == 'up', model + ' moved anchor change 3 vs post'] = df_prefs.loc[df_prefs['Direction'] == 'up', model + ' 1 change 3 vs post']
    df_prefs.loc[df_prefs['Direction'] == 'down', model + ' unmoved anchor change 3 vs post'] = df_prefs.loc[df_prefs['Direction'] == 'down', model + ' 1 change 3 vs post']
    df_prefs.loc[df_prefs['Direction'] == 'up', model + ' unmoved anchor change 3 vs post'] = df_prefs.loc[df_prefs['Direction'] == 'up', model + ' 7 change 3 vs post']




    ## summarise changes 
    print('Changes in selection of item 1 in post-switch relative to pre-switch')
    for d in directions:
        mean_pref = np.mean(df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 1 change pre vs post'])
        se_pref = scipy.stats.sem(df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 1 change pre vs post'])
        t = scipy.stats.ttest_1samp(df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 1 change pre vs post'], 0)
        print(d+': ',mean_pref, ', SE = ', se_pref, ', t = ', t.statistic, ', p = ', t.pvalue)
        
        ## effsizes
        data1 = df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='pre'), model+ ' 1'].to_numpy()
        data2 = df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 1'].to_numpy()
        paired_ttest_extras(data1, data2)


    print()
    print('Changes in selection of item 7 in post-switch relative to pre-switch')
    for d in directions:
        mean_pref = np.mean(df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 7 change pre vs post'])
        se_pref = scipy.stats.sem(df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 7 change pre vs post'])
        t = scipy.stats.ttest_1samp(df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 7 change pre vs post'], 0)
        print(d+': ',mean_pref, ', SE = ', se_pref,', t = ', t.statistic, ', p = ', t.pvalue)

        ## effsizes
        data1 = df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='pre'), model+ ' 7'].to_numpy()
        data2 = df_prefs.loc[(df_prefs['Direction']==d)&(df_prefs['Block']=='post'), model+ ' 7'].to_numpy()
        paired_ttest_extras(data1, data2)

    print()

    ## ttest to see if changes in selection of item 1 in up participants are significantly different from changes in selection of item 7 in down participants
    t = scipy.stats.ttest_ind(df_prefs.loc[(df_prefs['Direction']=='up')&(df_prefs['Block']=='post'), model+ ' 1 change pre vs post'], -1*df_prefs.loc[(df_prefs['Direction']=='down')&(df_prefs['Block']=='post'), model+ ' 7 change pre vs post'])
    print('ttest of moved item preference change (down-7 vs up-1): t = ',t.statistic, ', p = ',t.pvalue)
    indep_sample_ttest_extras(df_prefs.loc[(df_prefs['Direction']=='up')&(df_prefs['Block']=='post'), model+ ' 1 change pre vs post'], -1*df_prefs.loc[(df_prefs['Direction']=='down')&(df_prefs['Block']=='post'), model+ ' 7 change pre vs post'])


    ## repeat, but with the unmoved item
    t = scipy.stats.ttest_ind(df_prefs.loc[(df_prefs['Direction']=='up')&(df_prefs['Block']=='post'), model+ ' 7 change pre vs post'], -1*df_prefs.loc[(df_prefs['Direction']=='down')&(df_prefs['Block']=='post'), model+ ' 1 change pre vs post'])
    print('ttest of unmoved item preference change (down-1 vs up-7): t = ',t.statistic, ', p = ',t.pvalue)
    indep_sample_ttest_extras(df_prefs.loc[(df_prefs['Direction']=='up')&(df_prefs['Block']=='post'), model+ ' 7 change pre vs post'], -1*df_prefs.loc[(df_prefs['Direction']=='down')&(df_prefs['Block']=='post'), model+ ' 1 change pre vs post'])

    
    return df_prefs


## Qvalue video
def Q_vid(all_data, moi, sim_ps, switch = 'pre'):


    ## loop through participants
    for p in sim_ps:

        ## initialise trial info
        n_models = len(moi)
        n_trials = all_data.loc[all_data['Participant']==p].shape[0]
        n_items = all_data['Item_1'].nunique()

        ## pre or post-switch data
        if switch == 'pre':
            data = all_data.loc[(all_data['Participant']==p) & (all_data['Switched']=='pre')]
            direction = ''
            interval = 150
        elif switch == 'post':

            #start the post-switch a little earlier to show the buildup to the switch
            switch_trial = all_data.loc[(all_data['Participant']==p)&(all_data['Switched']=='post'), 'Trial'].iloc[0]
            switch_trial -=10
            data = all_data.loc[(all_data['Participant']==p)&(all_data['Trial']>=switch_trial)]
            interval = 250
            direction = data['Direction'].iloc[0]
            
        ## get Qvals
        n_trials = data.shape[0]
        Qvals = np.zeros((n_models, n_trials, n_items))
        frames = range(n_trials)
        for m, model in enumerate(moi):
            for i in range(n_items):
                Qvals[m,:,i] = data[f'{model} item {i+1}'].to_numpy()

        ## axes formatting
        fig, axs = plt.subplots(1, n_models, figsize=(n_models*6, 6))
        if n_models == 1:
            axs = [axs]

        # plt.subplots_adjust(wspace=0.3)
        # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.3, hspace=0.3)
        animations = []
        animation = FuncAnimation(fig, Q_frame_update, fargs=(Qvals, moi, axs, switch, direction), frames=frames, interval=150, repeat=True)
        # fig.tight_layout()
        animations.append(animation)

        HTML(animation.to_html5_video())

        ## save video to google drive
        animation.save('../../../../../../Google Drive/My Drive/MPSCog/Qvals_{}_{}.mp4'.format(switch, direction), writer='ffmpeg', fps=10)




## frame_update function for the Q_vid
def Q_frame_update(frame, Qvals, moi, axs, switch = 'pre', direction = None):

    ## model titles
    # model_titles = ['Symm learning', 'Asymm learning']
    model_titles = {
        'Q1*': 'Symm learning (Q1*)',
        'Q2*': 'Asymm learning (Q2*)',
        'Q3*': 'Adaptive asymm (Q3*)',
    }

    ## loop through models
    for m, model in enumerate(moi):
        axs[m].clear()

        # Plot the markers as 'o' with different colors
        markers = axs[m].scatter(range(Qvals.shape[2]), Qvals[m, frame, :], c=np.arange(Qvals.shape[2]), cmap='plasma', marker='o', edgecolors = 'white',s=500, zorder = 2)

        # Plot the line in black
        line, = axs[m].plot(Qvals[m, frame, :], color='black', zorder = 1)

        if switch == 'pre':
            axs[m].set_ylim([-0.7,0.7])
        else:
            ymin = np.min(Qvals[m, :, :]) - 0.1
            ymax = np.max(Qvals[m, :, :]) + 0.1
            axs[m].set_ylim([ymin,ymax])

        if direction is not None:
            axs[m].set_title(model_titles[model]+'\n'+direction, fontsize = 20)
        else:
            axs[m].set_title(model_titles[model], fontsize = 20)
        axs[m].set_xlabel('Item', fontsize = 18)
        axs[m].set_xticks(ticks = np.arange(0, Qvals.shape[2]), labels = np.arange(1, Qvals.shape[2]+1), fontsize = 18)
        axs[m].set_yticklabels([])

        

    ## y labelling
    axs[0].set_ylabel('Q value (a.u.)', fontsize = 18)
    if len(moi) > 1:
        axs[-1].set_ylabel('')


## plot asymmetry curve
def plot_asymm(asymms, df_metrics, model = 'human', switches = ['pre']):
    directions = asymms['Direction'].unique()
    # asymms = asymms.loc[asymms['Direction']=='down']

    for switch in switches:
        figs_asymm, ax = plt.subplots(1,1,figsize=(7,4))
        sns.lineplot(data = asymms.loc[(asymms['Switched']==switch)
                                    ], x = 'Combined_value', y = 'Accuracy '+model, hue = 'Direction', hue_order = ['down','up'], errorbar=("se", 2), legend = True)
        max_val = np.max(asymms['Combined_value'])
        min_val = np.min(asymms['Combined_value'])

        ## plot percentage of participants with negative slope
        percentages = []
        for d in ['down','up']:
            n_wb = len(df_metrics.loc[(df_metrics['Direction']==d) & (df_metrics[model + ' pre-switch asymm slope']<0)])
            n_lb = len(df_metrics.loc[(df_metrics['Direction']==d) & (df_metrics[model + ' pre-switch asymm slope']>0)])
            percentage = np.round(n_wb/(n_wb+n_lb)*100,1)
            percentages.append(f'{d} (winner-biased: {percentage}%)')
            # texts.append(f'{d}: {percentage}%')
        # text = f'{directions[0]}: {percentages[0]}%,\n{directions[1]}: {percentages[1]}%'
        # ax.text(max_val+0.5, 0.9, text, fontsize = 15)

        ## increase size of legend title
        ax.get_legend().set_title('Direction')
        ax.get_legend().get_title().set_fontsize('12')
        ## left-align legend title
        
        #replace blue and orange lines with labels from labels
        labels = ax.get_legend().get_texts()
        for i, d in enumerate(directions):
            labels[i].set_text(percentages[i])
            labels[i].set_fontsize(12)



        # plt.ylim([0.6, 0.9])
        # plt.yticks(ticks = np.linspace(0.6,0.9,5), labels = np.round(np.linspace(0.6,0.9,5),2))
        plt.xticks(labels = np.arange(min_val,max_val+1, dtype = int), ticks = np.arange(min_val,max_val+1))
        plt.xlabel('Combined pair value', fontsize = 15)
        plt.ylabel('P(correct)', fontsize = 15)
        plt.title('Model-agnostic\n(pre-changepoint)', fontsize = 18)


    return figs_asymm


## save fig to folder
def save_fig(fig, name):
    fig.savefig('figures/'+name+'.png', dpi=300, bbox_inches='tight')
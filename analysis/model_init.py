# import models
# importlib.reload(models)
# from models import TI_SMC, TI_RL
# import helpers
# importlib.reload(helpers)
# from helpers import *
import numpy as np


### initialise everything for the fit

model_type = 'RL'
parallel = 1


# fit which participants?
# fit_ps = participants
# fit_participants = np.array([54,30,51])
# fit_participants = participants[:3]
# fit_participants = participants
# print(fit_participants)

## set minimisation method
# mini = 'Nelder-Mead'
# mini = 'trust-constr'
# mini = 'Powell'
mini = 'diff_evo'

minimize_method_opts = {
    mini: dict(
        maxiter=2000,
        ),
    "L-BFGS-B": dict(
        maxiter=2000, eps=1e-4
        ),  # https://stats.stackexchange.com/a/167199/148275
    "Powell": dict(
        maxiter=1000,
    ),
}[mini]


## set names of models and params
if model_type == 'RL':
        ### set the params of interest for each model
    all_params = np.array(['a1','a2','a0','eta','tauI','tauP','gam','lam','eps','omi1','omi2','meta','beta','evo_var', 'lmbda', 'kappa', 'coef'])
    # all_models = np.array((['Q1*','Q2*','Q3*', 'Q1*P','Q2*P','Q3*P','Q1*Pi','Q2*Pi', 'Q3*Pi', 'Q1','Q2','Q3','Q3*d','Q1*_conf','Q2*_conf','Q3*_conf',], 
    all_models = np.array((
        ['Q-symm','Q-asymm','Q-adapt-entropy', 'Q-symm-P','Q-asymm-P','Q-adapt-P' ,'Q1*Pi','Q2*Pi', 'Q3*Pi', 'Q1','Q2','Q3','Q-adapt','Q-adapt-d-P','Q1*_conf','Q2*_conf','Q3*_conf','Q-PH'], 
        ['Q-symm_m1','Q-asymm_m1','Q-adapt_m1', 'Q-symm-P_m1','Q-asymm-P_m1','Q-adapt-P_m1' ,'Q1*Pi_m1','Q2*Pi_m1', 'Q3*Pi_m1', 'Q1_m1','Q2_m1','Q3_m1','Q-adapt-d_m1','Q-adapt-d-P_m1','Q1*_conf_m1','Q2*_conf_m1','Q3*_conf_m1','Q-PH_m1'], 
        ['Q-symm_m2','Q-asymm_m2','Q-adapt_m2', 'Q-symm-P_m2','Q-asymm-P_m2','Q-adapt-P_m2' ,'Q1*Pi_m2','Q2*Pi_m2', 'Q3*Pi_m2', 'Q1_m2','Q2_m2','Q3_m2','Q-adapt-d_m2','Q-adapt-d-P_m2','Q1*_conf_m2','Q2*_conf_m2','Q3*_conf_m2','Q-PH_m2'], 
                            # ['Q1*_m1','Q2*_m1','Q3*_m1', 'Q1*P_m1','Q2*P_m1','Q3*P_m1','Q1*Pi_m1','Q2*Pi_m1', 'Q3*Pi_m1', 'Q1_m1','Q2_m1','Q3_m1','Q3*d_m1'],
                            # ['Q1*_m2','Q2*_m2','Q3*_m2', 'Q1*P_m2','Q2*P_m2','Q3*P_m2','Q1*Pi_m2','Q2*Pi_m2', 'Q3*Pi_m2', 'Q1_m2','Q2_m2','Q3_m2','Q3*d_m2']
                            ))

    n_models = len(all_models[0])

    #set the indices of params required by each model 
    param_idx = list((
        #standard (ADD 7 BACK IN FOR EPS)
        (
        [0,3,4], #Q1*
        [0,1,3,4], #Q2*
        [2,3,4], #Q3*
        [0,3,4,6], #Q1*P
        [0,1,3,4,6], #Q2*P
        [2,3,4,6], #Q3*P
        [0,3,4,5,6,7], #Q1*Pi
        [0,1,3,4,5,6,7], #Q2*Pi
        [2,3,4,5,6,7], #Q3*Pi
        [0,4], #Q1
        [0,1,4], #Q2
        [2,4], #Q3
        [2,3,4,11], #Q3*d
        [2,3,4,6,11], #Q3*dP
        [0,3,4,11], #Q1*_conf
        [0,1,3,4,11], #Q2*_conf
        [2,3,4,11], #Q3*_conf
        [0,1,3,4,11] # gershman/pearce hall etc.
        ), 
        (
        [0,3,4,9], #Q1*_m1
        [0,1,3,4,9], #Q2*_m1
        [2,3,4,9], #Q3*_m1
        [0,3,4,5,6,9], #Q1*P_m1
        [0,1,3,4,5,6,9], #Q2*P_m1
        [2,3,4,5,6,9], #Q3*P_m1
        [0,3,4,5,6,7,9], #Q1*Pi_m1
        [0,1,3,4,5,6,7,9], #Q2*Pi_m1
        [2,3,4,5,6,7,9], #Q3*Pi_m1
        [0,4,9], #Q1_m1
        [0,1,4,9], #Q2_m1
        [2,4,9], #Q3_m1
        [2,3,4,9], #Q3*d_m1
        [2,3,4,9,11], #Q3*dP_m1
        [0,3,4,9,11], #Q1*_conf
        [0,1,3,4,9,11], #Q2*_conf
        [2,3,4,9,11], #Q3*_conf
        [0,1,4,9,11] # gershman/pearce hall etc.
        ), 
        (
        [0,3,4,9,10], #Q1*_m2
        [0,1,3,4,9,10], #Q2*_m2
        [2,3,4,9,10], #Q3*_m2
        [0,3,4,5,6,9,10], #Q1*P_m2
        [0,1,3,4,5,6,9,10], #Q2*P_m2
        [2,3,4,5,6,9,10], #Q3*P_m2
        [0,3,4,5,6,7,9,10], #Q1*Pi_m2
        [0,1,3,4,5,6,7,9,10], #Q2*Pi_m2
        [2,3,4,5,6,7,9,10], #Q3*Pi_m2
        [0,4,9,10], #Q1_m2
        [0,1,4,9,10], #Q2_m2
        [2,4,9,10], #Q3_m2
        [2,3,4,9,10], #Q3*d_m2
        [2,3,4,9,10,11], #Q3*dP_m2
        [0,3,4,9,10,11], #Q1*_conf
        [0,1,3,4,9,10,11], #Q2*_conf
        [2,3,4,9,10,11], #Q3*_conf
        [0,1,3,4,9,10,11] # gershman/pearce hall etc.
        ), 
    ))

    #get names of params for each model
    model_params = {}
    for model_set in range(3):
        for m in range(n_models):
            model_params[all_models[model_set][m]] = all_params[param_idx[model_set][m]]

    model_params['SMC'] = ['evo_var', 'kappa']
    # model_params['SMC'] = ['beta', 'evo_var', 'kappa', 'coef']
    
    ## assemble relevant parameters (single initial point per param)
    a1 = 0.025
    # asymm = 0.5
    a2 = 0.025
    eta = 0.1
    tauI = 0.125
    gam = 0.125
    lam = 1
    tauP = 0.125
    eps = 0.01
    omi1 = 0.025
    omi2 = 0.025
    omi_a = 0.01
    omi_asymm = 0.5
    a0 = 0.025
    meta = 1


    #multiple initial points
    a1_0s = np.array([0.01])
    a2_0s = a1_0s.copy()
    # asymm_0s = np.array([0.5,2])
    eta_0s = np.array([0.1])
    # tauI_0s = np.array([0.1,0.3])
    tauI_0s = np.array([0.125])
    tauP_0s = np.array([0.125])
    lam_0s = np.array([1])
    gam_0s = np.array([0.1])
    eps_0s = np.array([0.01])
    omi1_0s = a1_0s.copy()
    omi2_0s = a2_0s.copy()
    a0_0s = np.array([0.01])
    meta_0s = np.array([1])
    all_x0s = np.array((a1_0s, a2_0s, a0_0s, eta_0s, tauI_0s, tauP_0s, gam_0s, lam_0s, eps_0s, omi1_0s, omi2_0s, meta_0s), dtype = object)

    #set bounds for all params
    all_params_0 = np.array([a1, a2,    a0, eta, tauI, tauP, gam,lam,  eps, omi1, omi2, meta])
    all_lb = np.array(      [0,   0,   -0.5, 0,  0,    0,    0,   0,   0,    -0.5,     0,  0])
    all_ub = np.array(      [0.5, 0.5,  0.5, 1,  1,    1,    1,   10,  0.2,  0.5,  0.5,    1])

    ## set number of free params
    n_free = {}
    for model in model_params.keys():
        n_free[model] = len(model_params[model])

#SMC
elif model_type == 'SMC':
    all_params = np.array(['beta', 'evo_var', 'kappa','coef'])
    # all_params = np.array(['beta', 'evo_var', 'ESSrmin'])
    # all_params = np.array(['beta', 'evo_var', 'beta_circle', 'blend'])
    all_models = np.array([['SMC']])
    
    param_idx = list((
        # standard SMC
        [0,1],
    ))

    #single initial point
    beta = 1
    evo_var = 0.05
    ESSrmin = 0.25
    beta_circle = 1
    blend = 0.25

    #multiple initial points
    beta_0s = np.array([4])
    evo_var_0s = np.array([0.05])
    ESSrmin_0s = np.array([0.25])
    beta_circle_0s = np.copy(beta_0s)
    blend_0s = np.array([0.25])
    all_x0s = np.array((beta_0s, evo_var_0s), dtype = object)
    # all_x0s = np.array((beta_0s, evo_var_0s, ESSrmin_0s), dtype = object)
    # all_x0s = np.array((beta_0s, evo_var_0s, beta_circle_0s, blend_0s), dtype = object)

    #free params
    n_free = {}
    n_free['SMC'] = len(all_params)

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
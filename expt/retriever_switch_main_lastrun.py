#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on Wed Aug 10 11:19:59 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from imagesSlides
#Assign participant to expt 1,2 or 3
import random
expt_n = random.choice((1,2,3))

if expt_n == 1:
    n_instructions1 = 14
    n_instructions2 = 19
elif expt_n ==2:
    n_instructions1 = 13
    n_instructions2 = 18
elif expt_n ==3:
    n_instructions1 = 13
    n_instructions2 = 17
# Run 'Before Experiment' code from codePracStart
conditions_practice = (("expt_" + str(expt_n) + "/resources/conditions_practice.xlsx"))


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'Retriever'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/graham/Dropbox/Work/MPIB/Uroboros/Online/main/client/public/retriever_switch_main_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "instructions" ---
instr1 = visual.ImageStim(
    win=win,
    name='instr1', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
keyNext = keyboard.Keyboard()
# Run 'Begin Experiment' code from imagesSlides
img_no = 1

current_img = 'expt_' + str(expt_n) + '/resources/instructions/Slide' + str(img_no) + '.jpg'


# --- Initialize components for Routine "practiceBlocks" ---
# Run 'Begin Experiment' code from codePracStart
# Counter for the practice blocks
practiceBlock = 0

# Message to be updated before every block
msgStartPractice = 'message shown before a practice Block'

# Highest stimulus value

stim_num_max = 8
key_startPrac = keyboard.Keyboard()
practiceMessage = visual.TextStim(win=win, name='practiceMessage',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fixation_2" ---
fixcross = visual.ShapeStim(
    win=win, name='fixcross', vertices='cross',units='pix', 
    size=(20, 20),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[-1.000,-1.000,-1.000],
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "practice" ---
practiceP1 = visual.ImageStim(
    win=win,
    name='practiceP1', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-250, 0), size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practiceP2 = visual.ImageStim(
    win=win,
    name='practiceP2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(250, 0), size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
practiceKey = keyboard.Keyboard()
# Run 'Begin Experiment' code from practiceFeedb
# Feedback message
msgPractice = 'Feedback msg after practice trial'

# Acc_practice to save code for accuracy
acc_practice = []
prac_trial = 0
tprac = []
durationBlank = 0.0
crossPractice = visual.ShapeStim(
    win=win, name='crossPractice', vertices='cross',units='pix', 
    size=(20, 20),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[-1,-1,-1],
    opacity=1.0, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "PracFeedb_2" ---
practiceFeedback = visual.TextStim(win=win, name='practiceFeedback',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
screenAfterFB = visual.TextStim(win=win, name='screenAfterFB',
    text='Any text\n\nincluding line breaks',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "attentionCheckPrac" ---
key_respAC_prac = keyboard.Keyboard()
# Run 'Begin Experiment' code from run_check_prac
# List storing the accuracy as 1 or 0 
AC_acc = []
hits_in_attention = 0
abortMsg = ''
Pos1_prac = visual.TextStim(win=win, name='Pos1_prac',
    text='',
    font='Sans Serif',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Pos2_prac = visual.TextStim(win=win, name='Pos2_prac',
    text='',
    font='Sans Serif',
    pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Pos3_prac = visual.TextStim(win=win, name='Pos3_prac',
    text='',
    font='Sans Serif',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Pos4_prac = visual.TextStim(win=win, name='Pos4_prac',
    text='',
    font='Sans Serif',
    pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
taskAC_prac = visual.TextStim(win=win, name='taskAC_prac',
    text='Use arrow keys to pick the number shown in the center',
    font='Sans Serif',
    pos=(0, 0.40), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ac_stim_prac = visual.TextStim(win=win, name='ac_stim_prac',
    text='',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "disturbance" ---
disturbed = visual.TextStim(win=win, name='disturbed',
    text="Were things around you quiet during the last block?\n\nPress '1' if you were disturbed and '0' if you were NOT disturbed.\n\nPlease do NOT use the NumPad.",
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyDisturbed = keyboard.Keyboard()

# --- Initialize components for Routine "ContinueOrEnd" ---
# Run 'Begin Experiment' code from AccuracyCheck
blockRepetitions = 0
numberQuits = 0
messageChecks = visual.TextStim(win=win, name='messageChecks',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_endFail = keyboard.Keyboard()

# --- Initialize components for Routine "quitExperiment" ---

# --- Initialize components for Routine "LoopControl_2" ---
# Run 'Begin Experiment' code from LoopContr
# Counter for the blocks
thisBlock = 0
numberACresults = 0
# Message shown before each block, to be updated
msgBlockNumber = 'which block we say we starting'

main_task_blocks = (("expt_" + str(expt_n) + "/resources/sequences/retriever_switch_conditions_expt_" + str(expt_n) + "_" + str(expInfo["participant"])) + ".xlsx")
beginBlock = visual.TextStim(win=win, name='beginBlock',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_respStart = keyboard.Keyboard()

# --- Initialize components for Routine "fixation_main" ---
fixcross_2 = visual.ShapeStim(
    win=win, name='fixcross_2', vertices='cross',units='pix', 
    size=(20, 20),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[-1.000,-1.000,-1.000],
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "trial" ---
imageP1 = visual.ImageStim(
    win=win,
    name='imageP1', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-250, 0), size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imageP2 = visual.ImageStim(
    win=win,
    name='imageP2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(250, 0), size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from Feedb
# Message that will be updated with specific feedback
msg = 'Feedback msg after trial'

# Counter for the trials 
ntrial = 0 
trialReal = []

# Coding the feedback message - add to output file
acc_real = []
acc_feedback = []

# Counter for hits per block for feedback and real accuracy
hits_per_block = 0
hits_per_block_real = 0

# Counter for the bonus
bonus_accuracies = []
cross_objects = visual.ShapeStim(
    win=win, name='cross_objects', vertices='cross',units='pix', 
    size=(20, 20),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "feedback" ---
Feedback = visual.TextStim(win=win, name='Feedback',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
blankScreen2 = visual.TextStim(win=win, name='blankScreen2',
    text='Any text\n\nincluding line breaks',
    font='Calibri',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "attentionCheck" ---
key_respAC = keyboard.Keyboard()
# Run 'Begin Experiment' code from run_check
AC_acc = []
hits_in_attention2 = 0

Pos1 = visual.TextStim(win=win, name='Pos1',
    text='',
    font='Sans Serif',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Pos2 = visual.TextStim(win=win, name='Pos2',
    text='',
    font='Sans Serif',
    pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Pos3 = visual.TextStim(win=win, name='Pos3',
    text='',
    font='Sans Serif',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Pos4 = visual.TextStim(win=win, name='Pos4',
    text='',
    font='Sans Serif',
    pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
shapeInstructions = visual.TextStim(win=win, name='shapeInstructions',
    text='Use arrow keys to pick the number shown in the center',
    font='Sans Serif',
    pos=(0, 0.40), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
ac_stim = visual.TextStim(win=win, name='ac_stim',
    text='',
    font='Calibri',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "ContinueOrEnd2" ---
# Run 'Begin Experiment' code from code_3
numberQuits2 = 0
msgEndExperiment = 'text after attention checks'
textEndExperiment = visual.TextStim(win=win, name='textEndExperiment',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
pressToEndExp = keyboard.Keyboard()

# --- Initialize components for Routine "quitExperiment2" ---

# --- Initialize components for Routine "BlockFeedback" ---
# Run 'Begin Experiment' code from fbBlock
# Message will be updated every block
msgBlock = 'fb after Block'
feedbBlocks = visual.TextStim(win=win, name='feedbBlocks',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keynextBlock = keyboard.Keyboard()

# --- Initialize components for Routine "disturbance" ---
disturbed = visual.TextStim(win=win, name='disturbed',
    text="Were things around you quiet during the last block?\n\nPress '1' if you were disturbed and '0' if you were NOT disturbed.\n\nPlease do NOT use the NumPad.",
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyDisturbed = keyboard.Keyboard()

# --- Initialize components for Routine "uro_instructions" ---
instr1_2 = visual.ImageStim(
    win=win,
    name='instr1_2', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
keyNext_3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from imagesSlides_2
uro_img_no = n_instructions1+1

current_uro_img = 'expt_'+str(expt_n)+'/resources/instructions/Slide' + str(uro_img_no) + '.jpg'

# --- Initialize components for Routine "bonus" ---
# Run 'Begin Experiment' code from bonusCode
msgBonus = 'Feedback msg to say if participant gets bonus'
get_bonus = []
key_resp2 = keyboard.Keyboard()
presentBonus = visual.TextStim(win=win, name='presentBonus',
    text='',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "finishExperiment" ---
finalText = visual.TextStim(win=win, name='finalText',
    text='Great! You finished the task. Thank you! \nPress space to exit and please wait until you get redirected back to Prolific. ',
    font='Sans Serif',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_respEnd = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructionsLoop = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructionsLoop')
thisExp.addLoop(instructionsLoop)  # add the loop to the experiment
thisInstructionsLoop = instructionsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop.rgb)
if thisInstructionsLoop != None:
    for paramName in thisInstructionsLoop:
        exec('{} = thisInstructionsLoop[paramName]'.format(paramName))

for thisInstructionsLoop in instructionsLoop:
    currentLoop = instructionsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop.rgb)
    if thisInstructionsLoop != None:
        for paramName in thisInstructionsLoop:
            exec('{} = thisInstructionsLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    instr1.setImage(current_img)
    keyNext.keys = []
    keyNext.rt = []
    _keyNext_allKeys = []
    # Run 'Begin Routine' code from imagesSlides
    current_img = 'expt_' + str(expt_n) + '/resources/instructions/Slide' + str(img_no) + '.jpg'
    
    # keep track of which components have finished
    instructionsComponents = [instr1, keyNext]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr1* updates
        if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr1.frameNStart = frameN  # exact frame index
            instr1.tStart = t  # local t and not account for scr refresh
            instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
            instr1.setAutoDraw(True)
        
        # *keyNext* updates
        waitOnFlip = False
        if keyNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyNext.frameNStart = frameN  # exact frame index
            keyNext.tStart = t  # local t and not account for scr refresh
            keyNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyNext, 'tStartRefresh')  # time at next scr refresh
            keyNext.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyNext.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyNext.status == STARTED and not waitOnFlip:
            theseKeys = keyNext.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _keyNext_allKeys.extend(theseKeys)
            if len(_keyNext_allKeys):
                keyNext.keys = _keyNext_allKeys[-1].name  # just the last key pressed
                keyNext.rt = _keyNext_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from imagesSlides
    # if the participant pressed the left key, decrease the image
    # number by one (e. g. going from "image 2" to "image 1"),
    # and if they pressed the right key, increase the image number
    # by one ("image 2" -> "image 3")
    if (img_no > 1) and ((keyNext.keys == str('left')) or (keyNext.keys == 'left')):
        img_no -= 1
    elif (img_no < n_instructions1) and ((keyNext.keys == str('right')) or (keyNext.keys == 'right')):
        img_no += 1
    elif (img_no == n_instructions1) and ((keyNext.keys == 'space') or (keyNext.keys == str('space'))):
        instructionsLoop.finished = True
    current_img = 'expt_' + str(expt_n) + '/resources/instructions/Slide' + str(img_no) + '.jpg'
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 100 repeats of 'instructionsLoop'

# get names of stimulus parameters
if instructionsLoop.trialList in ([], [None], None):
    params = []
else:
    params = instructionsLoop.trialList[0].keys()
# save data for this loop
instructionsLoop.saveAsText(filename + 'instructionsLoop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
repPractice = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repPractice')
thisExp.addLoop(repPractice)  # add the loop to the experiment
thisRepPractice = repPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepPractice.rgb)
if thisRepPractice != None:
    for paramName in thisRepPractice:
        exec('{} = thisRepPractice[paramName]'.format(paramName))

for thisRepPractice in repPractice:
    currentLoop = repPractice
    # abbreviate parameter names if possible (e.g. rgb = thisRepPractice.rgb)
    if thisRepPractice != None:
        for paramName in thisRepPractice:
            exec('{} = thisRepPractice[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "practiceBlocks" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codePracStart
    # First time we enter the loop, we are in block 1
    
    practiceBlock +=1
    
    # Update message before blocks
    if practiceBlock == 1:
        myIndices = "0:8"
        msgStartPractice = 'Let\'s start practicing this task.\nDon\'t worry about making mistakes, just try to understand the goal for this task.\n[Press space bar to continue]'
    else: 
        myIndices = "8:16"
        msgStartPractice = 'This is the second practice block. \nAgain, relax and try to get familiar with the task and the timing, don\'t worry about mistakes.\n[Press space bar to start]'
    key_startPrac.keys = []
    key_startPrac.rt = []
    _key_startPrac_allKeys = []
    practiceMessage.setText(msgStartPractice)
    # keep track of which components have finished
    practiceBlocksComponents = [key_startPrac, practiceMessage]
    for thisComponent in practiceBlocksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practiceBlocks" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_startPrac* updates
        waitOnFlip = False
        if key_startPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_startPrac.frameNStart = frameN  # exact frame index
            key_startPrac.tStart = t  # local t and not account for scr refresh
            key_startPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_startPrac, 'tStartRefresh')  # time at next scr refresh
            key_startPrac.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_startPrac.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_startPrac.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_startPrac.status == STARTED and not waitOnFlip:
            theseKeys = key_startPrac.getKeys(keyList=['space'], waitRelease=False)
            _key_startPrac_allKeys.extend(theseKeys)
            if len(_key_startPrac_allKeys):
                key_startPrac.keys = _key_startPrac_allKeys[-1].name  # just the last key pressed
                key_startPrac.rt = _key_startPrac_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *practiceMessage* updates
        if practiceMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practiceMessage.frameNStart = frameN  # exact frame index
            practiceMessage.tStart = t  # local t and not account for scr refresh
            practiceMessage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceMessage, 'tStartRefresh')  # time at next scr refresh
            practiceMessage.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceBlocksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceBlocks" ---
    for thisComponent in practiceBlocksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practiceBlocks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceTrials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conditions_practice, selection=myIndices),
        seed=None, name='practiceTrials')
    thisExp.addLoop(practiceTrials)  # add the loop to the experiment
    thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    for thisPracticeTrial in practiceTrials:
        currentLoop = practiceTrials
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                exec('{} = thisPracticeTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fixcross_prac_duration
        # Jitter the timing of fixation cross 0.5 to 1.5 seconds
        
        #jitter = 30 + randint(0, 60)
        # keep track of which components have finished
        fixation_2Components = [fixcross]
        for thisComponent in fixation_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            if fixcross.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross.started')
                fixcross.setAutoDraw(True)
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixcross.stopped')
                    fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_2" ---
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixation_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        practiceP1.setImage(LocItem1)
        practiceP2.setImage(LocItem2)
        practiceKey.keys = []
        practiceKey.rt = []
        _practiceKey_allKeys = []
        # Run 'Begin Routine' code from practiceFeedb
        # Update trial number and add it to outputfile
        prac_trial += 1
        tprac = prac_trial
        thisExp.addData('tprac', tprac)
        crossDisappear = 1
        
        # keep track of which components have finished
        practiceComponents = [practiceP1, practiceP2, practiceKey, crossPractice]
        for thisComponent in practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice" ---
        while continueRoutine and routineTimer.getTime() < 2.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practiceP1* updates
            if practiceP1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceP1.frameNStart = frameN  # exact frame index
                practiceP1.tStart = t  # local t and not account for scr refresh
                practiceP1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceP1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practiceP1.started')
                practiceP1.setAutoDraw(True)
            if practiceP1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceP1.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceP1.tStop = t  # not accounting for scr refresh
                    practiceP1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practiceP1.stopped')
                    practiceP1.setAutoDraw(False)
            
            # *practiceP2* updates
            if practiceP2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceP2.frameNStart = frameN  # exact frame index
                practiceP2.tStart = t  # local t and not account for scr refresh
                practiceP2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceP2, 'tStartRefresh')  # time at next scr refresh
                practiceP2.setAutoDraw(True)
            if practiceP2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceP2.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceP2.tStop = t  # not accounting for scr refresh
                    practiceP2.frameNStop = frameN  # exact frame index
                    practiceP2.setAutoDraw(False)
            
            # *practiceKey* updates
            waitOnFlip = False
            if practiceKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceKey.frameNStart = frameN  # exact frame index
                practiceKey.tStart = t  # local t and not account for scr refresh
                practiceKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceKey, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practiceKey.started')
                practiceKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practiceKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practiceKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practiceKey.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceKey.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceKey.tStop = t  # not accounting for scr refresh
                    practiceKey.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practiceKey.stopped')
                    practiceKey.status = FINISHED
            if practiceKey.status == STARTED and not waitOnFlip:
                theseKeys = practiceKey.getKeys(keyList=['left','right'], waitRelease=False)
                _practiceKey_allKeys.extend(theseKeys)
                if len(_practiceKey_allKeys):
                    practiceKey.keys = _practiceKey_allKeys[0].name  # just the first key pressed
                    practiceKey.rt = _practiceKey_allKeys[0].rt
            # Run 'Each Frame' code from practiceFeedb
            if (practiceKey.keys == 'left') or (practiceKey.keys == 'right'): 
                crossDisappear = 0
            
            # *crossPractice* updates
            if crossPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crossPractice.frameNStart = frameN  # exact frame index
                crossPractice.tStart = t  # local t and not account for scr refresh
                crossPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crossPractice, 'tStartRefresh')  # time at next scr refresh
                crossPractice.setAutoDraw(True)
            if crossPractice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crossPractice.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    crossPractice.tStop = t  # not accounting for scr refresh
                    crossPractice.frameNStop = frameN  # exact frame index
                    crossPractice.setAutoDraw(False)
            if crossPractice.status == STARTED:  # only update if drawing
                crossPractice.setOpacity(crossDisappear, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice" ---
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if practiceKey.keys in ['', [], None]:  # No response was made
            practiceKey.keys = None
        practiceTrials.addData('practiceKey.keys',practiceKey.keys)
        if practiceKey.keys != None:  # we had a response
            practiceTrials.addData('practiceKey.rt', practiceKey.rt)
        # Run 'End Routine' code from practiceFeedb
        ### Practice feedback
        # Catching response and calculating value; > 0 means correct
        
        if practiceKey.keys == 'left': 
            valueDiff = P1 - P2
        if practiceKey.keys == 'right':
            valueDiff = P2 - P1
        if practiceKey.keys is None:
            valueDiff = None
        
        # Calculating if items are neighbors or not 
        
        value_dist = P1 - P2
        value_dist_abs = abs(value_dist) 
        
        # Loop for giving accurate feedback after every trial
        # Participant doesn't respond on time
        if practiceKey.keys is None: 
            msgPractice = 'TRY TO RESPOND FASTER'
        elif value_dist_abs > 1:
            msgPractice = ''
            durationBlank = 0
        elif value_dist_abs == 1:
            durationBlank = 0.5
            if valueDiff > 0:
                msgPractice = 'Correct'
            elif valueDiff < 0:
                msgPractice = 'Incorrect'
        
        # Loop for saving feedback and hits
        if valueDiff is None:
            acc_practice = 2
        elif valueDiff > 0:
            acc_practice = 1  
        elif valueDiff < 0:
            acc_practice = 0
        
        thisExp.addData('acc_practice', acc_practice)
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.500000)
        
        # --- Prepare to start Routine "PracFeedb_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        practiceFeedback.setText(msgPractice)
        # keep track of which components have finished
        PracFeedb_2Components = [practiceFeedback, screenAfterFB]
        for thisComponent in PracFeedb_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PracFeedb_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practiceFeedback* updates
            if practiceFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceFeedback.frameNStart = frameN  # exact frame index
                practiceFeedback.tStart = t  # local t and not account for scr refresh
                practiceFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceFeedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practiceFeedback.started')
                practiceFeedback.setAutoDraw(True)
            if practiceFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceFeedback.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceFeedback.tStop = t  # not accounting for scr refresh
                    practiceFeedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practiceFeedback.stopped')
                    practiceFeedback.setAutoDraw(False)
            
            # *screenAfterFB* updates
            if screenAfterFB.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                screenAfterFB.frameNStart = frameN  # exact frame index
                screenAfterFB.tStart = t  # local t and not account for scr refresh
                screenAfterFB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(screenAfterFB, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'screenAfterFB.started')
                screenAfterFB.setAutoDraw(True)
            if screenAfterFB.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > screenAfterFB.tStartRefresh + durationBlank-frameTolerance:
                    # keep track of stop time/frame for later
                    screenAfterFB.tStop = t  # not accounting for scr refresh
                    screenAfterFB.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'screenAfterFB.stopped')
                    screenAfterFB.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracFeedb_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracFeedb_2" ---
        for thisComponent in PracFeedb_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "PracFeedb_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'practiceTrials'
    
    # get names of stimulus parameters
    if practiceTrials.trialList in ([], [None], None):
        params = []
    else:
        params = practiceTrials.trialList[0].keys()
    # save data for this loop
    practiceTrials.saveAsText(filename + 'practiceTrials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    Attentions = data.TrialHandler(nReps=1, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('expt_1/resources/attentionChecks.xlsx', selection='0:4'),
        seed=None, name='Attentions')
    thisExp.addLoop(Attentions)  # add the loop to the experiment
    thisAttention = Attentions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAttention.rgb)
    if thisAttention != None:
        for paramName in thisAttention:
            exec('{} = thisAttention[paramName]'.format(paramName))
    
    for thisAttention in Attentions:
        currentLoop = Attentions
        # abbreviate parameter names if possible (e.g. rgb = thisAttention.rgb)
        if thisAttention != None:
            for paramName in thisAttention:
                exec('{} = thisAttention[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "attentionCheckPrac" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_respAC_prac.keys = []
        key_respAC_prac.rt = []
        _key_respAC_prac_allKeys = []
        Pos1_prac.setText(Loc1)
        Pos2_prac.setText(Loc2)
        Pos3_prac.setText(Loc3)
        Pos4_prac.setText(Loc4)
        ac_stim_prac.setText(Stim)
        # keep track of which components have finished
        attentionCheckPracComponents = [key_respAC_prac, Pos1_prac, Pos2_prac, Pos3_prac, Pos4_prac, taskAC_prac, ac_stim_prac]
        for thisComponent in attentionCheckPracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "attentionCheckPrac" ---
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_respAC_prac* updates
            waitOnFlip = False
            if key_respAC_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respAC_prac.frameNStart = frameN  # exact frame index
                key_respAC_prac.tStart = t  # local t and not account for scr refresh
                key_respAC_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respAC_prac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_respAC_prac.started')
                key_respAC_prac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respAC_prac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respAC_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respAC_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_respAC_prac.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    key_respAC_prac.tStop = t  # not accounting for scr refresh
                    key_respAC_prac.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_respAC_prac.stopped')
                    key_respAC_prac.status = FINISHED
            if key_respAC_prac.status == STARTED and not waitOnFlip:
                theseKeys = key_respAC_prac.getKeys(keyList=['up','down','left','right'], waitRelease=False)
                _key_respAC_prac_allKeys.extend(theseKeys)
                if len(_key_respAC_prac_allKeys):
                    key_respAC_prac.keys = _key_respAC_prac_allKeys[0].name  # just the first key pressed
                    key_respAC_prac.rt = _key_respAC_prac_allKeys[0].rt
                    # was this correct?
                    if (key_respAC_prac.keys == str(CorrAns)) or (key_respAC_prac.keys == CorrAns):
                        key_respAC_prac.corr = 1
                    else:
                        key_respAC_prac.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *Pos1_prac* updates
            if Pos1_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos1_prac.frameNStart = frameN  # exact frame index
                Pos1_prac.tStart = t  # local t and not account for scr refresh
                Pos1_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos1_prac, 'tStartRefresh')  # time at next scr refresh
                Pos1_prac.setAutoDraw(True)
            if Pos1_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos1_prac.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos1_prac.tStop = t  # not accounting for scr refresh
                    Pos1_prac.frameNStop = frameN  # exact frame index
                    Pos1_prac.setAutoDraw(False)
            
            # *Pos2_prac* updates
            if Pos2_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos2_prac.frameNStart = frameN  # exact frame index
                Pos2_prac.tStart = t  # local t and not account for scr refresh
                Pos2_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos2_prac, 'tStartRefresh')  # time at next scr refresh
                Pos2_prac.setAutoDraw(True)
            if Pos2_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos2_prac.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos2_prac.tStop = t  # not accounting for scr refresh
                    Pos2_prac.frameNStop = frameN  # exact frame index
                    Pos2_prac.setAutoDraw(False)
            
            # *Pos3_prac* updates
            if Pos3_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos3_prac.frameNStart = frameN  # exact frame index
                Pos3_prac.tStart = t  # local t and not account for scr refresh
                Pos3_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos3_prac, 'tStartRefresh')  # time at next scr refresh
                Pos3_prac.setAutoDraw(True)
            if Pos3_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos3_prac.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos3_prac.tStop = t  # not accounting for scr refresh
                    Pos3_prac.frameNStop = frameN  # exact frame index
                    Pos3_prac.setAutoDraw(False)
            
            # *Pos4_prac* updates
            if Pos4_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos4_prac.frameNStart = frameN  # exact frame index
                Pos4_prac.tStart = t  # local t and not account for scr refresh
                Pos4_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos4_prac, 'tStartRefresh')  # time at next scr refresh
                Pos4_prac.setAutoDraw(True)
            if Pos4_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos4_prac.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos4_prac.tStop = t  # not accounting for scr refresh
                    Pos4_prac.frameNStop = frameN  # exact frame index
                    Pos4_prac.setAutoDraw(False)
            
            # *taskAC_prac* updates
            if taskAC_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                taskAC_prac.frameNStart = frameN  # exact frame index
                taskAC_prac.tStart = t  # local t and not account for scr refresh
                taskAC_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taskAC_prac, 'tStartRefresh')  # time at next scr refresh
                taskAC_prac.setAutoDraw(True)
            if taskAC_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taskAC_prac.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    taskAC_prac.tStop = t  # not accounting for scr refresh
                    taskAC_prac.frameNStop = frameN  # exact frame index
                    taskAC_prac.setAutoDraw(False)
            
            # *ac_stim_prac* updates
            if ac_stim_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ac_stim_prac.frameNStart = frameN  # exact frame index
                ac_stim_prac.tStart = t  # local t and not account for scr refresh
                ac_stim_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ac_stim_prac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ac_stim_prac.started')
                ac_stim_prac.setAutoDraw(True)
            if ac_stim_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ac_stim_prac.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ac_stim_prac.tStop = t  # not accounting for scr refresh
                    ac_stim_prac.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ac_stim_prac.stopped')
                    ac_stim_prac.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in attentionCheckPracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "attentionCheckPrac" ---
        for thisComponent in attentionCheckPracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_respAC_prac.keys in ['', [], None]:  # No response was made
            key_respAC_prac.keys = None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               key_respAC_prac.corr = 1;  # correct non-response
            else:
               key_respAC_prac.corr = 0;  # failed to respond (incorrectly)
        # store data for Attentions (TrialHandler)
        Attentions.addData('key_respAC_prac.keys',key_respAC_prac.keys)
        Attentions.addData('key_respAC_prac.corr', key_respAC_prac.corr)
        if key_respAC_prac.keys != None:  # we had a response
            Attentions.addData('key_respAC_prac.rt', key_respAC_prac.rt)
        # Run 'End Routine' code from run_check_prac
        # Add accuracy to output file 
        if key_respAC_prac.corr:
            AC_acc = 1
            hits_in_attention += 1
        else:
            AC_acc = 0
            
        thisExp.addData('AC_acc', AC_acc)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Attentions'
    
    # get names of stimulus parameters
    if Attentions.trialList in ([], [None], None):
        params = []
    else:
        params = Attentions.trialList[0].keys()
    # save data for this loop
    Attentions.saveAsText(filename + 'Attentions.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "disturbance" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyDisturbed.keys = []
    keyDisturbed.rt = []
    _keyDisturbed_allKeys = []
    # keep track of which components have finished
    disturbanceComponents = [disturbed, keyDisturbed]
    for thisComponent in disturbanceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "disturbance" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *disturbed* updates
        if disturbed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disturbed.frameNStart = frameN  # exact frame index
            disturbed.tStart = t  # local t and not account for scr refresh
            disturbed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disturbed, 'tStartRefresh')  # time at next scr refresh
            disturbed.setAutoDraw(True)
        
        # *keyDisturbed* updates
        if keyDisturbed.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyDisturbed.frameNStart = frameN  # exact frame index
            keyDisturbed.tStart = t  # local t and not account for scr refresh
            keyDisturbed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyDisturbed, 'tStartRefresh')  # time at next scr refresh
            keyDisturbed.status = STARTED
            # keyboard checking is just starting
            keyDisturbed.clock.reset()  # now t=0
            keyDisturbed.clearEvents(eventType='keyboard')
        if keyDisturbed.status == STARTED:
            theseKeys = keyDisturbed.getKeys(keyList=['1', '0'], waitRelease=False)
            _keyDisturbed_allKeys.extend(theseKeys)
            if len(_keyDisturbed_allKeys):
                keyDisturbed.keys = _keyDisturbed_allKeys[-1].name  # just the last key pressed
                keyDisturbed.rt = _keyDisturbed_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in disturbanceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "disturbance" ---
    for thisComponent in disturbanceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyDisturbed.keys in ['', [], None]:  # No response was made
        keyDisturbed.keys = None
    repPractice.addData('keyDisturbed.keys',keyDisturbed.keys)
    if keyDisturbed.keys != None:  # we had a response
        repPractice.addData('keyDisturbed.rt', keyDisturbed.rt)
    # the Routine "disturbance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2 repeats of 'repPractice'


# --- Prepare to start Routine "ContinueOrEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from AccuracyCheck
#Calculate accuracy in AC and end experiment if acc belor 50%
check_AC_acc = float(hits_in_attention)/8.0

if check_AC_acc < 0.50:
    # Skip whole real task
    blockRepetitions = 0
    repsBonus = 0
    abortMsg = 'Your accuracy in the attention checks is too low. \nYou have reached the end of the experiment. \nPress space to quit the experiment. Thank you!'
    numberQuits = 1
else:
    # Next line tells how many real blocks 
    blockRepetitions = 6
    repsBonus = 1
    abortMsg = 'You passed the attention checks. \nYou are about to start the real task with entirely new images. \nHere, both your accuracy and speed matter for the experiment. \n[ Press space bar to START ]'
    numberQuits = 0
messageChecks.setText(abortMsg
)
key_endFail.keys = []
key_endFail.rt = []
_key_endFail_allKeys = []
# keep track of which components have finished
ContinueOrEndComponents = [messageChecks, key_endFail]
for thisComponent in ContinueOrEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ContinueOrEnd" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *messageChecks* updates
    if messageChecks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        messageChecks.frameNStart = frameN  # exact frame index
        messageChecks.tStart = t  # local t and not account for scr refresh
        messageChecks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(messageChecks, 'tStartRefresh')  # time at next scr refresh
        messageChecks.setAutoDraw(True)
    
    # *key_endFail* updates
    waitOnFlip = False
    if key_endFail.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_endFail.frameNStart = frameN  # exact frame index
        key_endFail.tStart = t  # local t and not account for scr refresh
        key_endFail.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_endFail, 'tStartRefresh')  # time at next scr refresh
        key_endFail.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_endFail.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_endFail.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_endFail.status == STARTED and not waitOnFlip:
        theseKeys = key_endFail.getKeys(keyList=['space'], waitRelease=False)
        _key_endFail_allKeys.extend(theseKeys)
        if len(_key_endFail_allKeys):
            key_endFail.keys = _key_endFail_allKeys[-1].name  # just the last key pressed
            key_endFail.rt = _key_endFail_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ContinueOrEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ContinueOrEnd" ---
for thisComponent in ContinueOrEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ContinueOrEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
quitExpLoop = data.TrialHandler(nReps=numberQuits, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='quitExpLoop')
thisExp.addLoop(quitExpLoop)  # add the loop to the experiment
thisQuitExpLoop = quitExpLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuitExpLoop.rgb)
if thisQuitExpLoop != None:
    for paramName in thisQuitExpLoop:
        exec('{} = thisQuitExpLoop[paramName]'.format(paramName))

for thisQuitExpLoop in quitExpLoop:
    currentLoop = quitExpLoop
    # abbreviate parameter names if possible (e.g. rgb = thisQuitExpLoop.rgb)
    if thisQuitExpLoop != None:
        for paramName in thisQuitExpLoop:
            exec('{} = thisQuitExpLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "quitExperiment" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from quitExpCode
    core.quit()
    # keep track of which components have finished
    quitExperimentComponents = []
    for thisComponent in quitExperimentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "quitExperiment" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quitExperimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "quitExperiment" ---
    for thisComponent in quitExperimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "quitExperiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed numberQuits repeats of 'quitExpLoop'

# get names of stimulus parameters
if quitExpLoop.trialList in ([], [None], None):
    params = []
else:
    params = quitExpLoop.trialList[0].keys()
# save data for this loop
quitExpLoop.saveAsText(filename + 'quitExpLoop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
repBlocks = data.TrialHandler(nReps=blockRepetitions, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repBlocks')
thisExp.addLoop(repBlocks)  # add the loop to the experiment
thisRepBlock = repBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepBlock.rgb)
if thisRepBlock != None:
    for paramName in thisRepBlock:
        exec('{} = thisRepBlock[paramName]'.format(paramName))

for thisRepBlock in repBlocks:
    currentLoop = repBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisRepBlock.rgb)
    if thisRepBlock != None:
        for paramName in thisRepBlock:
            exec('{} = thisRepBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "LoopControl_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from LoopContr
    # First time we enter the loop, we are in block 1
    thisBlock +=1
    
    # A slice between two specific rows - trials for the block
    #myIndices = slice(startItem, endItem+1)
    if expt_n == 1:
        if thisBlock == 1:
            MyIndicesMain = "0:70"
        elif thisBlock == 2: 
            MyIndicesMain = "70:140"
        elif thisBlock == 3:
            MyIndicesMain = "140:210"
        elif thisBlock == 4:
            MyIndicesMain = "210:282"
        elif thisBlock == 5:
            MyIndicesMain = "282:354"
        elif thisBlock == 6:
            MyIndicesMain = "354:426"
    elif expt_n == 2:
        if thisBlock == 1:
            MyIndicesMain = "0:54"
        elif thisBlock == 2: 
            MyIndicesMain = "54:108"
        elif thisBlock == 3:
            MyIndicesMain = "108:162"
        elif thisBlock == 4:
            MyIndicesMain = "162:234"
        elif thisBlock == 5:
            MyIndicesMain = "234:306"
        elif thisBlock == 6:
            MyIndicesMain = "306:378"
    elif expt_n == 3:
        if thisBlock == 1:
            MyIndicesMain = "0:54"
        elif thisBlock == 2: 
            MyIndicesMain = "54:108"
        elif thisBlock == 3:
            MyIndicesMain = "108:162"
        elif thisBlock == 4:
            MyIndicesMain = "162:232"
        elif thisBlock == 5:
            MyIndicesMain = "232:302"
        elif thisBlock == 6:
            MyIndicesMain = "302:372"
    # Update message before every new block
    msgBlockNumber = 'You will start block ' + str(thisBlock) + ' out of 6. \nRemember that both accuracy and speed matter. \n[Press space bar to begin.]'
    
    # After block 3 we do the attention checks and introduce uro instructions
    if thisBlock == 3:
        uroInstructions = 1
        repsAC = 1
        numberACresults = 1
    else: 
        uroInstructions = 0
        repsAC = 0
        numberACresults = 0
    beginBlock.setText(msgBlockNumber)
    key_respStart.keys = []
    key_respStart.rt = []
    _key_respStart_allKeys = []
    # keep track of which components have finished
    LoopControl_2Components = [beginBlock, key_respStart]
    for thisComponent in LoopControl_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LoopControl_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *beginBlock* updates
        if beginBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            beginBlock.frameNStart = frameN  # exact frame index
            beginBlock.tStart = t  # local t and not account for scr refresh
            beginBlock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(beginBlock, 'tStartRefresh')  # time at next scr refresh
            beginBlock.setAutoDraw(True)
        
        # *key_respStart* updates
        waitOnFlip = False
        if key_respStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_respStart.frameNStart = frameN  # exact frame index
            key_respStart.tStart = t  # local t and not account for scr refresh
            key_respStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_respStart, 'tStartRefresh')  # time at next scr refresh
            key_respStart.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_respStart.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_respStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_respStart.status == STARTED and not waitOnFlip:
            theseKeys = key_respStart.getKeys(keyList=['space'], waitRelease=False)
            _key_respStart_allKeys.extend(theseKeys)
            if len(_key_respStart_allKeys):
                key_respStart.keys = _key_respStart_allKeys[-1].name  # just the last key pressed
                key_respStart.rt = _key_respStart_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LoopControl_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LoopControl_2" ---
    for thisComponent in LoopControl_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LoopControl_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(main_task_blocks, selection=MyIndicesMain),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation_main" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        # Jitter the timing of fixation cross 0.5 to 1.5 seconds
        
        #jitter = 30 + randint(0, 60)
        # keep track of which components have finished
        fixation_mainComponents = [fixcross_2]
        for thisComponent in fixation_mainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation_main" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross_2* updates
            if fixcross_2.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                fixcross_2.frameNStart = frameN  # exact frame index
                fixcross_2.tStart = t  # local t and not account for scr refresh
                fixcross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross_2.started')
                fixcross_2.setAutoDraw(True)
            if fixcross_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross_2.tStop = t  # not accounting for scr refresh
                    fixcross_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixcross_2.stopped')
                    fixcross_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_mainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_main" ---
        for thisComponent in fixation_mainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixation_main" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        imageP1.setImage(P1Loc)
        imageP2.setImage(P2Loc)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from Feedb
        # Counter for which trial we are in right now
        ntrial += 1
        trialReal = ntrial
        thisExp.addData('trialNumber', trialReal)
        crossDisappear = 1
        #mainStart = core.monotonicClock.getTime()
        # keep track of which components have finished
        trialComponents = [imageP1, imageP2, key_resp, cross_objects]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        while continueRoutine and routineTimer.getTime() < 2.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *imageP1* updates
            if imageP1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageP1.frameNStart = frameN  # exact frame index
                imageP1.tStart = t  # local t and not account for scr refresh
                imageP1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageP1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageP1.started')
                imageP1.setAutoDraw(True)
            if imageP1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imageP1.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    imageP1.tStop = t  # not accounting for scr refresh
                    imageP1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'imageP1.stopped')
                    imageP1.setAutoDraw(False)
            
            # *imageP2* updates
            if imageP2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imageP2.frameNStart = frameN  # exact frame index
                imageP2.tStart = t  # local t and not account for scr refresh
                imageP2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageP2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageP2.started')
                imageP2.setAutoDraw(True)
            if imageP2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imageP2.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    imageP2.tStop = t  # not accounting for scr refresh
                    imageP2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'imageP2.stopped')
                    imageP2.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
            # Run 'Each Frame' code from Feedb
            if key_resp.keys == 'left' or key_resp.keys == 'right': 
                crossDisappear = 0
            
            
            # *cross_objects* updates
            if cross_objects.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_objects.frameNStart = frameN  # exact frame index
                cross_objects.tStart = t  # local t and not account for scr refresh
                cross_objects.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_objects, 'tStartRefresh')  # time at next scr refresh
                cross_objects.setAutoDraw(True)
            if cross_objects.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_objects.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_objects.tStop = t  # not accounting for scr refresh
                    cross_objects.frameNStop = frameN  # exact frame index
                    cross_objects.setAutoDraw(False)
            if cross_objects.status == STARTED:  # only update if drawing
                cross_objects.setOpacity(crossDisappear, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # Run 'End Routine' code from Feedb
        # Catch responses
        if key_resp.keys == 'left': 
            valueDiff = ValueP1 - ValueP2
            thisExp.addData('item_chosen_name', P1name)
            thisExp.addData('item_chosen_value', ValueP1)
            thisExp.addData('item_chosen_ID', P1id)
        elif key_resp.keys == 'right':
            valueDiff = ValueP2 - ValueP1
            thisExp.addData('item_chosen_name', P2name)
            thisExp.addData('item_chosen_value', ValueP2)
            thisExp.addData('item_chosen_ID', P2id)
        elif key_resp.keys == None:
            valueDiff = None
            thisExp.addData('item_chosen_name', None)
            thisExp.addData('item_chosen_value', None)
            thisExp.addData('item_chosen_ID', None)
            
        # Calculating if items are neighbors or not 
        
        value_dist = ValueP1 - ValueP2
        value_dist_abs = abs(value_dist) 
        
        # Preparing feedback messages
                
        if key_resp.keys == None: 
            msg = 'TRY TO RESPOND FASTER'
            acc_feedback = 2
            acc_real = 2
            durationBlank = 0.5
        elif Feedback_On == 0:
            msg = ''
            durationBlank = 0.0
            acc_feedback = 3
        elif Feedback_On == 1:
            durationBlank = 0.5
            if InverseFb == 1:
                if valueDiff > 0:
                    msg = 'Incorrect'
                    acc_feedback = 0
                elif valueDiff < 0:
                    msg = 'Correct'
                    acc_feedback = 1 
            elif InverseFb == 0:
                if valueDiff > 0:
                    msg = 'Correct'
                    acc_feedback = 1
                elif valueDiff < 0:
                    msg = 'Incorrect'
                    acc_feedback = 0
        
        # Loop for saving the real feedback and hits
        if valueDiff is None: 
            acc_real = 2
        elif (valueDiff > 0 and InverseFb == 0) or (valueDiff < 0 and InverseFb == 1):
            acc_real = 1
            hits_per_block_real = hits_per_block_real + 1
        elif (valueDiff > 0 and InverseFb == 1) or (valueDiff < 0 and InverseFb == 0):
            acc_real = 0 
            
        # Add data to output file
        thisExp.addData('diff_chosen_minus_reject', valueDiff)
        thisExp.addData('acc_real', acc_real)
        thisExp.addData('acc_feedback', acc_feedback)
        thisExp.addData('expt_n', expt_n)
        
        # Add acc from this trial to an array for later
        bonus_accuracies.append(acc_real)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.500000)
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Feedback.setText(msg)
        # keep track of which components have finished
        feedbackComponents = [Feedback, blankScreen2]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Feedback* updates
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                Feedback.setAutoDraw(True)
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    Feedback.setAutoDraw(False)
            
            # *blankScreen2* updates
            if blankScreen2.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                blankScreen2.frameNStart = frameN  # exact frame index
                blankScreen2.tStart = t  # local t and not account for scr refresh
                blankScreen2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankScreen2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blankScreen2.started')
                blankScreen2.setAutoDraw(True)
            if blankScreen2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blankScreen2.tStartRefresh + durationBlank-frameTolerance:
                    # keep track of stop time/frame for later
                    blankScreen2.tStop = t  # not accounting for scr refresh
                    blankScreen2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blankScreen2.stopped')
                    blankScreen2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsText(filename + 'trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_AC = data.TrialHandler(nReps=repsAC, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('expt_1/resources/attentionChecks.xlsx'),
        seed=None, name='trials_AC')
    thisExp.addLoop(trials_AC)  # add the loop to the experiment
    thisTrials_AC = trials_AC.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_AC.rgb)
    if thisTrials_AC != None:
        for paramName in thisTrials_AC:
            exec('{} = thisTrials_AC[paramName]'.format(paramName))
    
    for thisTrials_AC in trials_AC:
        currentLoop = trials_AC
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_AC.rgb)
        if thisTrials_AC != None:
            for paramName in thisTrials_AC:
                exec('{} = thisTrials_AC[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "attentionCheck" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_respAC.keys = []
        key_respAC.rt = []
        _key_respAC_allKeys = []
        Pos1.setText(Loc1)
        Pos2.setText(Loc2)
        Pos3.setText(Loc3)
        Pos4.setText(Loc4)
        ac_stim.setText(Stim)
        # keep track of which components have finished
        attentionCheckComponents = [key_respAC, Pos1, Pos2, Pos3, Pos4, shapeInstructions, ac_stim]
        for thisComponent in attentionCheckComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "attentionCheck" ---
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_respAC* updates
            waitOnFlip = False
            if key_respAC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respAC.frameNStart = frameN  # exact frame index
                key_respAC.tStart = t  # local t and not account for scr refresh
                key_respAC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respAC, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_respAC.started')
                key_respAC.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respAC.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respAC.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respAC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_respAC.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    key_respAC.tStop = t  # not accounting for scr refresh
                    key_respAC.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_respAC.stopped')
                    key_respAC.status = FINISHED
            if key_respAC.status == STARTED and not waitOnFlip:
                theseKeys = key_respAC.getKeys(keyList=['up','down','left','right'], waitRelease=False)
                _key_respAC_allKeys.extend(theseKeys)
                if len(_key_respAC_allKeys):
                    key_respAC.keys = _key_respAC_allKeys[0].name  # just the first key pressed
                    key_respAC.rt = _key_respAC_allKeys[0].rt
                    # was this correct?
                    if (key_respAC.keys == str(CorrAns)) or (key_respAC.keys == CorrAns):
                        key_respAC.corr = 1
                    else:
                        key_respAC.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *Pos1* updates
            if Pos1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos1.frameNStart = frameN  # exact frame index
                Pos1.tStart = t  # local t and not account for scr refresh
                Pos1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos1, 'tStartRefresh')  # time at next scr refresh
                Pos1.setAutoDraw(True)
            if Pos1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos1.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos1.tStop = t  # not accounting for scr refresh
                    Pos1.frameNStop = frameN  # exact frame index
                    Pos1.setAutoDraw(False)
            
            # *Pos2* updates
            if Pos2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos2.frameNStart = frameN  # exact frame index
                Pos2.tStart = t  # local t and not account for scr refresh
                Pos2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos2, 'tStartRefresh')  # time at next scr refresh
                Pos2.setAutoDraw(True)
            if Pos2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos2.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos2.tStop = t  # not accounting for scr refresh
                    Pos2.frameNStop = frameN  # exact frame index
                    Pos2.setAutoDraw(False)
            
            # *Pos3* updates
            if Pos3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos3.frameNStart = frameN  # exact frame index
                Pos3.tStart = t  # local t and not account for scr refresh
                Pos3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos3, 'tStartRefresh')  # time at next scr refresh
                Pos3.setAutoDraw(True)
            if Pos3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos3.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos3.tStop = t  # not accounting for scr refresh
                    Pos3.frameNStop = frameN  # exact frame index
                    Pos3.setAutoDraw(False)
            
            # *Pos4* updates
            if Pos4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pos4.frameNStart = frameN  # exact frame index
                Pos4.tStart = t  # local t and not account for scr refresh
                Pos4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pos4, 'tStartRefresh')  # time at next scr refresh
                Pos4.setAutoDraw(True)
            if Pos4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pos4.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Pos4.tStop = t  # not accounting for scr refresh
                    Pos4.frameNStop = frameN  # exact frame index
                    Pos4.setAutoDraw(False)
            
            # *shapeInstructions* updates
            if shapeInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                shapeInstructions.frameNStart = frameN  # exact frame index
                shapeInstructions.tStart = t  # local t and not account for scr refresh
                shapeInstructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(shapeInstructions, 'tStartRefresh')  # time at next scr refresh
                shapeInstructions.setAutoDraw(True)
            if shapeInstructions.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > shapeInstructions.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    shapeInstructions.tStop = t  # not accounting for scr refresh
                    shapeInstructions.frameNStop = frameN  # exact frame index
                    shapeInstructions.setAutoDraw(False)
            
            # *ac_stim* updates
            if ac_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ac_stim.frameNStart = frameN  # exact frame index
                ac_stim.tStart = t  # local t and not account for scr refresh
                ac_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ac_stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ac_stim.started')
                ac_stim.setAutoDraw(True)
            if ac_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ac_stim.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ac_stim.tStop = t  # not accounting for scr refresh
                    ac_stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ac_stim.stopped')
                    ac_stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in attentionCheckComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "attentionCheck" ---
        for thisComponent in attentionCheckComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_respAC.keys in ['', [], None]:  # No response was made
            key_respAC.keys = None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               key_respAC.corr = 1;  # correct non-response
            else:
               key_respAC.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_AC (TrialHandler)
        trials_AC.addData('key_respAC.keys',key_respAC.keys)
        trials_AC.addData('key_respAC.corr', key_respAC.corr)
        if key_respAC.keys != None:  # we had a response
            trials_AC.addData('key_respAC.rt', key_respAC.rt)
        # Run 'End Routine' code from run_check
        if key_respAC.corr:
            AC_acc = 1
            hits_in_attention2 += 1
        else:
            AC_acc = 0
            
        thisExp.addData('AC_acc', AC_acc)
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        thisExp.nextEntry()
        
    # completed repsAC repeats of 'trials_AC'
    
    # get names of stimulus parameters
    if trials_AC.trialList in ([], [None], None):
        params = []
    else:
        params = trials_AC.trialList[0].keys()
    # save data for this loop
    trials_AC.saveAsText(filename + 'trials_AC.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    presentACresults = data.TrialHandler(nReps=numberACresults, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='presentACresults')
    thisExp.addLoop(presentACresults)  # add the loop to the experiment
    thisPresentACresult = presentACresults.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPresentACresult.rgb)
    if thisPresentACresult != None:
        for paramName in thisPresentACresult:
            exec('{} = thisPresentACresult[paramName]'.format(paramName))
    
    for thisPresentACresult in presentACresults:
        currentLoop = presentACresults
        # abbreviate parameter names if possible (e.g. rgb = thisPresentACresult.rgb)
        if thisPresentACresult != None:
            for paramName in thisPresentACresult:
                exec('{} = thisPresentACresult[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ContinueOrEnd2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        # Force end of loop if subjects fail AC
        check_AC_acc_2 = float(hits_in_attention2)/8.0
        if check_AC_acc_2 < 0.50:
            msgEndExperiment = 'Your accuracy in the attention checks is too low. \nYou have reached the end of the experiment. \nPress the space to quit the experiment. Thank you!'
            numberQuits2 = 1
        else:
            msgEndExperiment = 'You passed the attention checks. \nPress space to see your feedback for the block.'
            numberQuits2 = 0
        textEndExperiment.setText(msgEndExperiment)
        pressToEndExp.keys = []
        pressToEndExp.rt = []
        _pressToEndExp_allKeys = []
        # keep track of which components have finished
        ContinueOrEnd2Components = [textEndExperiment, pressToEndExp]
        for thisComponent in ContinueOrEnd2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ContinueOrEnd2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textEndExperiment* updates
            if textEndExperiment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textEndExperiment.frameNStart = frameN  # exact frame index
                textEndExperiment.tStart = t  # local t and not account for scr refresh
                textEndExperiment.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textEndExperiment, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textEndExperiment.started')
                textEndExperiment.setAutoDraw(True)
            
            # *pressToEndExp* updates
            waitOnFlip = False
            if pressToEndExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pressToEndExp.frameNStart = frameN  # exact frame index
                pressToEndExp.tStart = t  # local t and not account for scr refresh
                pressToEndExp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pressToEndExp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pressToEndExp.started')
                pressToEndExp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(pressToEndExp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(pressToEndExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if pressToEndExp.status == STARTED and not waitOnFlip:
                theseKeys = pressToEndExp.getKeys(keyList=['space'], waitRelease=False)
                _pressToEndExp_allKeys.extend(theseKeys)
                if len(_pressToEndExp_allKeys):
                    pressToEndExp.keys = _pressToEndExp_allKeys[-1].name  # just the last key pressed
                    pressToEndExp.rt = _pressToEndExp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ContinueOrEnd2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ContinueOrEnd2" ---
        for thisComponent in ContinueOrEnd2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "ContinueOrEnd2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed numberACresults repeats of 'presentACresults'
    
    
    # set up handler to look after randomisation of conditions etc
    quitExpLoop2 = data.TrialHandler(nReps=numberQuits2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='quitExpLoop2')
    thisExp.addLoop(quitExpLoop2)  # add the loop to the experiment
    thisQuitExpLoop2 = quitExpLoop2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQuitExpLoop2.rgb)
    if thisQuitExpLoop2 != None:
        for paramName in thisQuitExpLoop2:
            exec('{} = thisQuitExpLoop2[paramName]'.format(paramName))
    
    for thisQuitExpLoop2 in quitExpLoop2:
        currentLoop = quitExpLoop2
        # abbreviate parameter names if possible (e.g. rgb = thisQuitExpLoop2.rgb)
        if thisQuitExpLoop2 != None:
            for paramName in thisQuitExpLoop2:
                exec('{} = thisQuitExpLoop2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "quitExperiment2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from quitExpCode_2
        core.quit()
        # keep track of which components have finished
        quitExperiment2Components = []
        for thisComponent in quitExperiment2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "quitExperiment2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in quitExperiment2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "quitExperiment2" ---
        for thisComponent in quitExperiment2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "quitExperiment2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numberQuits2 repeats of 'quitExpLoop2'
    
    # get names of stimulus parameters
    if quitExpLoop2.trialList in ([], [None], None):
        params = []
    else:
        params = quitExpLoop2.trialList[0].keys()
    # save data for this loop
    quitExpLoop2.saveAsText(filename + 'quitExpLoop2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "BlockFeedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fbBlock
    # Calculating accuracy in the block
    previous_block_acc = float(hits_per_block_real)/ntrial
    
    
    # Present message depending on percentage of correct answers
    if previous_block_acc >= 0.80: 
        msgBlock = 'Amazing, your accuracy in the block was really high!\nRemember, the number of correct trials will determine the chance to get the bonus payment.\nPress SPACE to continue.'
    elif previous_block_acc < 0.80 and previous_block_acc >= 0.60: 
        msgBlock = 'Your accuracy in the block was great! You are doing an excellent job!\nRemember, the number of correct trials will determine the chance to get the bonus payment.\nPress SPACE to continue.' 
    elif previous_block_acc < 0.60 and previous_block_acc >= 0.50: 
        msgBlock = 'Your accuracy in the block was good. However, there is still room for improvement!\nRemember, the number of correct trials will determine the chance to get the bonus payment.\nPress SPACE to continue.'
    elif previous_block_acc <= 0.50: 
        msgBlock = 'Your accuracy in the block was a bit low. \nDon\'t give up! You will surely improve it.\nRemember, the number of correct trials will determine the chance to get the bonus payment.\nPress SPACE to continue.'
        
    
    feedbBlocks.setText(msgBlock)
    keynextBlock.keys = []
    keynextBlock.rt = []
    _keynextBlock_allKeys = []
    # keep track of which components have finished
    BlockFeedbackComponents = [feedbBlocks, keynextBlock]
    for thisComponent in BlockFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlockFeedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbBlocks* updates
        if feedbBlocks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbBlocks.frameNStart = frameN  # exact frame index
            feedbBlocks.tStart = t  # local t and not account for scr refresh
            feedbBlocks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbBlocks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbBlocks.started')
            feedbBlocks.setAutoDraw(True)
        
        # *keynextBlock* updates
        waitOnFlip = False
        if keynextBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keynextBlock.frameNStart = frameN  # exact frame index
            keynextBlock.tStart = t  # local t and not account for scr refresh
            keynextBlock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keynextBlock, 'tStartRefresh')  # time at next scr refresh
            keynextBlock.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keynextBlock.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keynextBlock.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keynextBlock.status == STARTED and not waitOnFlip:
            theseKeys = keynextBlock.getKeys(keyList=['space'], waitRelease=False)
            _keynextBlock_allKeys.extend(theseKeys)
            if len(_keynextBlock_allKeys):
                keynextBlock.keys = _keynextBlock_allKeys[-1].name  # just the last key pressed
                keynextBlock.rt = _keynextBlock_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlockFeedback" ---
    for thisComponent in BlockFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "BlockFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "disturbance" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyDisturbed.keys = []
    keyDisturbed.rt = []
    _keyDisturbed_allKeys = []
    # keep track of which components have finished
    disturbanceComponents = [disturbed, keyDisturbed]
    for thisComponent in disturbanceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "disturbance" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *disturbed* updates
        if disturbed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disturbed.frameNStart = frameN  # exact frame index
            disturbed.tStart = t  # local t and not account for scr refresh
            disturbed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disturbed, 'tStartRefresh')  # time at next scr refresh
            disturbed.setAutoDraw(True)
        
        # *keyDisturbed* updates
        if keyDisturbed.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyDisturbed.frameNStart = frameN  # exact frame index
            keyDisturbed.tStart = t  # local t and not account for scr refresh
            keyDisturbed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyDisturbed, 'tStartRefresh')  # time at next scr refresh
            keyDisturbed.status = STARTED
            # keyboard checking is just starting
            keyDisturbed.clock.reset()  # now t=0
            keyDisturbed.clearEvents(eventType='keyboard')
        if keyDisturbed.status == STARTED:
            theseKeys = keyDisturbed.getKeys(keyList=['1', '0'], waitRelease=False)
            _keyDisturbed_allKeys.extend(theseKeys)
            if len(_keyDisturbed_allKeys):
                keyDisturbed.keys = _keyDisturbed_allKeys[-1].name  # just the last key pressed
                keyDisturbed.rt = _keyDisturbed_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in disturbanceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "disturbance" ---
    for thisComponent in disturbanceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyDisturbed.keys in ['', [], None]:  # No response was made
        keyDisturbed.keys = None
    repBlocks.addData('keyDisturbed.keys',keyDisturbed.keys)
    if keyDisturbed.keys != None:  # we had a response
        repBlocks.addData('keyDisturbed.rt', keyDisturbed.rt)
    # the Routine "disturbance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    uro_instr_reps = data.TrialHandler(nReps=uroInstructions, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='uro_instr_reps')
    thisExp.addLoop(uro_instr_reps)  # add the loop to the experiment
    thisUro_instr_rep = uro_instr_reps.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisUro_instr_rep.rgb)
    if thisUro_instr_rep != None:
        for paramName in thisUro_instr_rep:
            exec('{} = thisUro_instr_rep[paramName]'.format(paramName))
    
    for thisUro_instr_rep in uro_instr_reps:
        currentLoop = uro_instr_reps
        # abbreviate parameter names if possible (e.g. rgb = thisUro_instr_rep.rgb)
        if thisUro_instr_rep != None:
            for paramName in thisUro_instr_rep:
                exec('{} = thisUro_instr_rep[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        uro_instructionsLoop = data.TrialHandler(nReps=100.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='uro_instructionsLoop')
        thisExp.addLoop(uro_instructionsLoop)  # add the loop to the experiment
        thisUro_instructionsLoop = uro_instructionsLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisUro_instructionsLoop.rgb)
        if thisUro_instructionsLoop != None:
            for paramName in thisUro_instructionsLoop:
                exec('{} = thisUro_instructionsLoop[paramName]'.format(paramName))
        
        for thisUro_instructionsLoop in uro_instructionsLoop:
            currentLoop = uro_instructionsLoop
            # abbreviate parameter names if possible (e.g. rgb = thisUro_instructionsLoop.rgb)
            if thisUro_instructionsLoop != None:
                for paramName in thisUro_instructionsLoop:
                    exec('{} = thisUro_instructionsLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "uro_instructions" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            instr1_2.setImage(current_uro_img)
            keyNext_3.keys = []
            keyNext_3.rt = []
            _keyNext_3_allKeys = []
            # Run 'Begin Routine' code from imagesSlides_2
            current_uro_img = 'expt_'+str(expt_n)+'/resources/instructions/Slide' + str(uro_img_no) + '.jpg'
            # keep track of which components have finished
            uro_instructionsComponents = [instr1_2, keyNext_3]
            for thisComponent in uro_instructionsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "uro_instructions" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *instr1_2* updates
                if instr1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instr1_2.frameNStart = frameN  # exact frame index
                    instr1_2.tStart = t  # local t and not account for scr refresh
                    instr1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instr1_2, 'tStartRefresh')  # time at next scr refresh
                    instr1_2.setAutoDraw(True)
                
                # *keyNext_3* updates
                waitOnFlip = False
                if keyNext_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    keyNext_3.frameNStart = frameN  # exact frame index
                    keyNext_3.tStart = t  # local t and not account for scr refresh
                    keyNext_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(keyNext_3, 'tStartRefresh')  # time at next scr refresh
                    keyNext_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(keyNext_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(keyNext_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if keyNext_3.status == STARTED and not waitOnFlip:
                    theseKeys = keyNext_3.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
                    _keyNext_3_allKeys.extend(theseKeys)
                    if len(_keyNext_3_allKeys):
                        keyNext_3.keys = _keyNext_3_allKeys[-1].name  # just the last key pressed
                        keyNext_3.rt = _keyNext_3_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in uro_instructionsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "uro_instructions" ---
            for thisComponent in uro_instructionsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from imagesSlides_2
            
            # if the participant pressed the left key, decrease the image
            # number by one (e. g. going from "image 2" to "image 1"),
            # and if they pressed the right key, increase the image number
            # by one ("image 2" -> "image 3")
            if (uro_img_no > n_instructions1 + 1) and ((keyNext_3.keys == str('left')) or (keyNext_3.keys == 'left')):
                uro_img_no -= 1
            elif (uro_img_no < n_instructions2) and ((keyNext_3.keys == str('right')) or (keyNext_3.keys == 'right')):
                uro_img_no += 1
            elif (uro_img_no == n_instructions2) and ((keyNext_3.keys == 'space') or (keyNext_3.keys == str('space'))):
                uro_instructionsLoop.finished = True
            current_uro_img = 'expt_'+str(expt_n)+'/resources/instructions/Slide' + str(uro_img_no) + '.jpg'
            # the Routine "uro_instructions" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 100.0 repeats of 'uro_instructionsLoop'
        
        # get names of stimulus parameters
        if uro_instructionsLoop.trialList in ([], [None], None):
            params = []
        else:
            params = uro_instructionsLoop.trialList[0].keys()
        # save data for this loop
        uro_instructionsLoop.saveAsText(filename + 'uro_instructionsLoop.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed uroInstructions repeats of 'uro_instr_reps'
    
    # get names of stimulus parameters
    if uro_instr_reps.trialList in ([], [None], None):
        params = []
    else:
        params = uro_instr_reps.trialList[0].keys()
    # save data for this loop
    uro_instr_reps.saveAsText(filename + 'uro_instr_reps.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed blockRepetitions repeats of 'repBlocks'


# set up handler to look after randomisation of conditions etc
BonusLoop = data.TrialHandler(nReps=repsBonus, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='BonusLoop')
thisExp.addLoop(BonusLoop)  # add the loop to the experiment
thisBonusLoop = BonusLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBonusLoop.rgb)
if thisBonusLoop != None:
    for paramName in thisBonusLoop:
        exec('{} = thisBonusLoop[paramName]'.format(paramName))

for thisBonusLoop in BonusLoop:
    currentLoop = BonusLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBonusLoop.rgb)
    if thisBonusLoop != None:
        for paramName in thisBonusLoop:
            exec('{} = thisBonusLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "bonus" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from bonusCode
    # Pick 10 random number from the accuracy counter
    import random as random
    sampled_accuracies = random.sample(bonus_accuracies, 10)
    
    # Display bonus message
    if sampled_accuracies.count(1) > 5:
        msgBonus = 'CONGRATULATIONS! The randomly picked responses were correct. You will receive the BONUS!\nPress SPACE to continue'
        get_bonus = 1
        thisExp.addData('Bonus', get_bonus)
    else: 
        msgBonus = 'Sorry! Unfortunately, the randomly picked responses were not correct. You cannot not receive the bonus\nPress SPACE to continue'
        
    key_resp2.keys = []
    key_resp2.rt = []
    _key_resp2_allKeys = []
    presentBonus.setText(msgBonus)
    # keep track of which components have finished
    bonusComponents = [key_resp2, presentBonus]
    for thisComponent in bonusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "bonus" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp2* updates
        waitOnFlip = False
        if key_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp2.frameNStart = frameN  # exact frame index
            key_resp2.tStart = t  # local t and not account for scr refresh
            key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
            key_resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp2_allKeys.extend(theseKeys)
            if len(_key_resp2_allKeys):
                key_resp2.keys = _key_resp2_allKeys[-1].name  # just the last key pressed
                key_resp2.rt = _key_resp2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *presentBonus* updates
        if presentBonus.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            presentBonus.frameNStart = frameN  # exact frame index
            presentBonus.tStart = t  # local t and not account for scr refresh
            presentBonus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentBonus, 'tStartRefresh')  # time at next scr refresh
            presentBonus.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bonusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bonus" ---
    for thisComponent in bonusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "bonus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed repsBonus repeats of 'BonusLoop'


# --- Prepare to start Routine "finishExperiment" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_respEnd.keys = []
key_respEnd.rt = []
_key_respEnd_allKeys = []
# keep track of which components have finished
finishExperimentComponents = [finalText, key_respEnd]
for thisComponent in finishExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finishExperiment" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finalText* updates
    if finalText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalText.frameNStart = frameN  # exact frame index
        finalText.tStart = t  # local t and not account for scr refresh
        finalText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finalText.started')
        finalText.setAutoDraw(True)
    
    # *key_respEnd* updates
    waitOnFlip = False
    if key_respEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_respEnd.frameNStart = frameN  # exact frame index
        key_respEnd.tStart = t  # local t and not account for scr refresh
        key_respEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_respEnd, 'tStartRefresh')  # time at next scr refresh
        key_respEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_respEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_respEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_respEnd.status == STARTED and not waitOnFlip:
        theseKeys = key_respEnd.getKeys(keyList=['space', 'Escape'], waitRelease=False)
        _key_respEnd_allKeys.extend(theseKeys)
        if len(_key_respEnd_allKeys):
            key_respEnd.keys = _key_respEnd_allKeys[-1].name  # just the last key pressed
            key_respEnd.rt = _key_respEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finishExperiment" ---
for thisComponent in finishExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "finishExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

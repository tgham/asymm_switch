/****************************** 
 * Euro Move *
 ******************************/

import { core, data, util, visual, hardware } from './lib/psychojs-2022.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// store info about the experiment session:
let expName = 'euro_move';  // from the Builder filename that created this script
let expInfo = {'PROLIFIC_PID': ''};
// let expInfo = {'Participant': '', 'PROLIFIC_PID': ''};
// let participant = expInfo["Participant"].toString()


// Load participant ID from Lou server
let input = await fetch("https://retriever-twist.exp.arc.mpib.org/api/inputs/by-group/ID").then(r => r.json());
let participant = input.ID;
// let participant = 1



// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from imagesSlides
var n_instructions, n_instructions_quick, n_instructions2, n_stim;

// use n_instructions to determine number of slides to use
n_instructions = 15;
n_instructions_quick = 3;
n_stim = 7;
n_instructions2 = 17;

// Run 'Before Experiment' code from codePracStart
var conditions_practice;
conditions_practice = ("expt_move/resources/conditions_practice.xlsx");


// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});
// psychoJS.experiment.addData("Participant", participant);

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);

// instructions
const instructionsLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(instructionsLoopLoopBegin(instructionsLoopLoopScheduler));
flowScheduler.add(instructionsLoopLoopScheduler);
flowScheduler.add(instructionsLoopLoopEnd);

// practice
const repPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(repPracticeLoopBegin(repPracticeLoopScheduler));
flowScheduler.add(repPracticeLoopScheduler);
flowScheduler.add(repPracticeLoopEnd);
flowScheduler.add(ContinueOrEndRoutineBegin());
flowScheduler.add(ContinueOrEndRoutineEachFrame());
flowScheduler.add(ContinueOrEndRoutineEnd());

// post-practice instructions
const quick_instructionsLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(quick_instructionsLoopLoopBegin(quick_instructionsLoopLoopScheduler));
flowScheduler.add(quick_instructionsLoopLoopScheduler);
flowScheduler.add(quick_instructionsLoopLoopEnd);

// main expt
const quitExpLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(quitExpLoopLoopBegin(quitExpLoopLoopScheduler));
flowScheduler.add(quitExpLoopLoopScheduler);
flowScheduler.add(quitExpLoopLoopEnd);
const repBlocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(repBlocksLoopBegin(repBlocksLoopScheduler));
flowScheduler.add(repBlocksLoopScheduler);
flowScheduler.add(repBlocksLoopEnd);


// post-expt dragging/selecting
flowScheduler.add(dragRoutineBegin());
flowScheduler.add(dragRoutineEachFrame());
flowScheduler.add(dragRoutineEnd());
flowScheduler.add(selectRoutineBegin());
flowScheduler.add(selectRoutineEachFrame());
flowScheduler.add(selectRoutineEnd());

// post-expt free-text
flowScheduler.add(textBoxRoutineBegin());
flowScheduler.add(textBoxRoutineEachFrame());
flowScheduler.add(textBoxRoutineEnd());

// finish expt
const BonusLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BonusLoopLoopBegin(BonusLoopLoopScheduler));
flowScheduler.add(BonusLoopLoopScheduler);
flowScheduler.add(BonusLoopLoopEnd);
flowScheduler.add(finishExperimentRoutineBegin());
flowScheduler.add(finishExperimentRoutineEachFrame());
flowScheduler.add(finishExperimentRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // {'name': ("expt_move/resources/sequences/euro_p" + participant.toString()) + ".xlsx", 'path': ("expt_move/resources/sequences/euro_p" + participant.toString()) + ".xlsx"},

    // stimuli and instructions
    {'name': "expt_move/resources/stim_IDs/07_phone.jpg", 'path': "expt_move/resources/stim_IDs/07_phone.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/01_rabbit.jpg", 'path': "expt_move/resources/stimuli_practice_decision/01_rabbit.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/05_glasses.jpg", 'path': "expt_move/resources/stimuli_practice_decision/05_glasses.jpg"},
    {'name': "expt_move/resources/stim_IDs/08_calculator.jpg", 'path': "expt_move/resources/stim_IDs/08_calculator.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/03_squirrel.jpg", 'path': "expt_move/resources/stimuli_practice_decision/03_squirrel.jpg"},
    {'name': "expt_move/resources/stim_IDs/03_dress.jpg", 'path': "expt_move/resources/stim_IDs/03_dress.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/08_handmixer.jpg", 'path': "expt_move/resources/stimuli_practice_decision/08_handmixer.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/07_sock.jpg", 'path': "expt_move/resources/stimuli_practice_decision/07_sock.jpg"},
    {'name': "expt_move/resources/stim_IDs/01_scarf.jpg", 'path': "expt_move/resources/stim_IDs/01_scarf.jpg"},
    {'name': "expt_move/resources/stim_IDs/04_satellite_dish.jpg", 'path': "expt_move/resources/stim_IDs/04_satellite_dish.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/02_canary.jpg", 'path': "expt_move/resources/stimuli_practice_decision/02_canary.jpg"},
    {'name': "expt_move/resources/stim_IDs/05_hat.jpg", 'path': "expt_move/resources/stim_IDs/05_hat.jpg"},
    {'name': "expt_move/resources/stim_IDs/06_slipper.jpg", 'path': "expt_move/resources/stim_IDs/06_slipper.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/04_beetle.jpg", 'path': "expt_move/resources/stimuli_practice_decision/04_beetle.jpg"},
    {'name': "expt_move/resources/stimuli_practice_decision/06_pullover.jpg", 'path': "expt_move/resources/stimuli_practice_decision/06_pullover.jpg"},
    {'name': "expt_move/resources/attentionChecks.xlsx", 'path': "expt_move/resources/attentionChecks.xlsx"},
    {'name': "expt_move/resources/conditions_practice.xlsx", 'path': "expt_move/resources/conditions_practice.xlsx"},
    {'name': "expt_move/resources/stim_IDs/02_radio.jpg", 'path': "expt_move/resources/stim_IDs/02_radio.jpg"},

    // instructions
    {'name': "expt_move/resources/instructions/Slide8.jpg", 'path': "expt_move/resources/instructions/Slide8.jpg"},
    {'name': "expt_move/resources/instructions/Slide6.jpg", 'path': "expt_move/resources/instructions/Slide6.jpg"},
    {'name': "expt_move/resources/instructions/Slide2.jpg", 'path': "expt_move/resources/instructions/Slide2.jpg"},
    {'name': "expt_move/resources/instructions/Slide10.jpg", 'path': "expt_move/resources/instructions/Slide10.jpg"},
    {'name': "expt_move/resources/instructions/Slide11.jpg", 'path': "expt_move/resources/instructions/Slide11.jpg"},
    {'name': "expt_move/resources/instructions/Slide12.jpg", 'path': "expt_move/resources/instructions/Slide12.jpg"},
    {'name': "expt_move/resources/instructions/Slide15.jpg", 'path': "expt_move/resources/instructions/Slide15.jpg"},
    {'name': "expt_move/resources/instructions/Slide9.jpg", 'path': "expt_move/resources/instructions/Slide9.jpg"},
    {'name': "expt_move/resources/instructions/Slide4.jpg", 'path': "expt_move/resources/instructions/Slide4.jpg"},
    {'name': "expt_move/resources/instructions/Slide14.jpg", 'path': "expt_move/resources/instructions/Slide14.jpg"},
    {'name': "expt_move/resources/instructions/Slide5.jpg", 'path': "expt_move/resources/instructions/Slide5.jpg"},
    {'name': "expt_move/resources/instructions/Slide13.jpg", 'path': "expt_move/resources/instructions/Slide13.jpg"},
    {'name': "expt_move/resources/instructions/Slide1.jpg", 'path': "expt_move/resources/instructions/Slide1.jpg"},
    {'name': "expt_move/resources/instructions/Slide3.jpg", 'path': "expt_move/resources/instructions/Slide3.jpg"},
    {'name': "expt_move/resources/instructions/Slide7.jpg", 'path': "expt_move/resources/instructions/Slide7.jpg"},
    {'name': "expt_move/resources/instructions/Slide8.jpg", 'path': "expt_move/resources/instructions/Slide8.jpg"},
    {'name': "expt_move/resources/instructions/Slide6.jpg", 'path': "expt_move/resources/instructions/Slide6.jpg"},
    {'name': "expt_move/resources/instructions/Slide2.jpg", 'path': "expt_move/resources/instructions/Slide2.jpg"},


    {'name': "expt_move/resources/quick_instructions/Slide1.jpg", 'path': "expt_move/resources/quick_instructions/Slide1.jpg"},
    {'name': "expt_move/resources/quick_instructions/Slide3.jpg", 'path': "expt_move/resources/quick_instructions/Slide3.jpg"},
    {'name': "expt_move/resources/quick_instructions/Slide2.jpg", 'path': "expt_move/resources/quick_instructions/Slide2.jpg"},


    // conditions files
    // {'name': "expt_move/resources/sequences/euro_p1.xlsx", 'path': "expt_move/resources/sequences/euro_p1.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p2.xlsx", 'path': "expt_move/resources/sequences/euro_p2.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p3.xlsx", 'path': "expt_move/resources/sequences/euro_p3.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p4.xlsx", 'path': "expt_move/resources/sequences/euro_p4.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p5.xlsx", 'path': "expt_move/resources/sequences/euro_p5.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p6.xlsx", 'path': "expt_move/resources/sequences/euro_p6.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p7.xlsx", 'path': "expt_move/resources/sequences/euro_p7.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p8.xlsx", 'path': "expt_move/resources/sequences/euro_p8.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p9.xlsx", 'path': "expt_move/resources/sequences/euro_p9.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p10.xlsx", 'path': "expt_move/resources/sequences/euro_p10.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p11.xlsx", 'path': "expt_move/resources/sequences/euro_p11.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p12.xlsx", 'path': "expt_move/resources/sequences/euro_p12.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p13.xlsx", 'path': "expt_move/resources/sequences/euro_p13.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p14.xlsx", 'path': "expt_move/resources/sequences/euro_p14.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p15.xlsx", 'path': "expt_move/resources/sequences/euro_p15.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p16.xlsx", 'path': "expt_move/resources/sequences/euro_p16.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p17.xlsx", 'path': "expt_move/resources/sequences/euro_p17.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p18.xlsx", 'path': "expt_move/resources/sequences/euro_p18.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p19.xlsx", 'path': "expt_move/resources/sequences/euro_p19.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p20.xlsx", 'path': "expt_move/resources/sequences/euro_p20.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p21.xlsx", 'path': "expt_move/resources/sequences/euro_p21.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p22.xlsx", 'path': "expt_move/resources/sequences/euro_p22.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p23.xlsx", 'path': "expt_move/resources/sequences/euro_p23.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p24.xlsx", 'path': "expt_move/resources/sequences/euro_p24.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p25.xlsx", 'path': "expt_move/resources/sequences/euro_p25.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p26.xlsx", 'path': "expt_move/resources/sequences/euro_p26.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p27.xlsx", 'path': "expt_move/resources/sequences/euro_p27.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p28.xlsx", 'path': "expt_move/resources/sequences/euro_p28.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p29.xlsx", 'path': "expt_move/resources/sequences/euro_p29.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p30.xlsx", 'path': "expt_move/resources/sequences/euro_p30.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p31.xlsx", 'path': "expt_move/resources/sequences/euro_p31.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p32.xlsx", 'path': "expt_move/resources/sequences/euro_p32.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p33.xlsx", 'path': "expt_move/resources/sequences/euro_p33.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p34.xlsx", 'path': "expt_move/resources/sequences/euro_p34.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p35.xlsx", 'path': "expt_move/resources/sequences/euro_p35.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p36.xlsx", 'path': "expt_move/resources/sequences/euro_p36.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p37.xlsx", 'path': "expt_move/resources/sequences/euro_p37.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p38.xlsx", 'path': "expt_move/resources/sequences/euro_p38.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p39.xlsx", 'path': "expt_move/resources/sequences/euro_p39.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p40.xlsx", 'path': "expt_move/resources/sequences/euro_p40.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p41.xlsx", 'path': "expt_move/resources/sequences/euro_p41.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p42.xlsx", 'path': "expt_move/resources/sequences/euro_p42.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p43.xlsx", 'path': "expt_move/resources/sequences/euro_p43.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p44.xlsx", 'path': "expt_move/resources/sequences/euro_p44.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p45.xlsx", 'path': "expt_move/resources/sequences/euro_p45.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p46.xlsx", 'path': "expt_move/resources/sequences/euro_p46.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p47.xlsx", 'path': "expt_move/resources/sequences/euro_p47.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p48.xlsx", 'path': "expt_move/resources/sequences/euro_p48.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p49.xlsx", 'path': "expt_move/resources/sequences/euro_p49.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p50.xlsx", 'path': "expt_move/resources/sequences/euro_p50.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p51.xlsx", 'path': "expt_move/resources/sequences/euro_p51.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p52.xlsx", 'path': "expt_move/resources/sequences/euro_p52.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p53.xlsx", 'path': "expt_move/resources/sequences/euro_p53.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p54.xlsx", 'path': "expt_move/resources/sequences/euro_p54.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p55.xlsx", 'path': "expt_move/resources/sequences/euro_p55.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p56.xlsx", 'path': "expt_move/resources/sequences/euro_p56.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p57.xlsx", 'path': "expt_move/resources/sequences/euro_p57.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p58.xlsx", 'path': "expt_move/resources/sequences/euro_p58.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p59.xlsx", 'path': "expt_move/resources/sequences/euro_p59.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p60.xlsx", 'path': "expt_move/resources/sequences/euro_p60.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p61.xlsx", 'path': "expt_move/resources/sequences/euro_p61.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p62.xlsx", 'path': "expt_move/resources/sequences/euro_p62.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p63.xlsx", 'path': "expt_move/resources/sequences/euro_p63.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p64.xlsx", 'path': "expt_move/resources/sequences/euro_p64.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p65.xlsx", 'path': "expt_move/resources/sequences/euro_p65.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p66.xlsx", 'path': "expt_move/resources/sequences/euro_p66.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p67.xlsx", 'path': "expt_move/resources/sequences/euro_p67.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p68.xlsx", 'path': "expt_move/resources/sequences/euro_p68.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p69.xlsx", 'path': "expt_move/resources/sequences/euro_p69.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p70.xlsx", 'path': "expt_move/resources/sequences/euro_p70.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p71.xlsx", 'path': "expt_move/resources/sequences/euro_p71.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p72.xlsx", 'path': "expt_move/resources/sequences/euro_p72.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p73.xlsx", 'path': "expt_move/resources/sequences/euro_p73.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p74.xlsx", 'path': "expt_move/resources/sequences/euro_p74.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p75.xlsx", 'path': "expt_move/resources/sequences/euro_p75.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p76.xlsx", 'path': "expt_move/resources/sequences/euro_p76.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p77.xlsx", 'path': "expt_move/resources/sequences/euro_p77.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p78.xlsx", 'path': "expt_move/resources/sequences/euro_p78.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p79.xlsx", 'path': "expt_move/resources/sequences/euro_p79.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p80.xlsx", 'path': "expt_move/resources/sequences/euro_p80.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p81.xlsx", 'path': "expt_move/resources/sequences/euro_p81.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p82.xlsx", 'path': "expt_move/resources/sequences/euro_p82.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p83.xlsx", 'path': "expt_move/resources/sequences/euro_p83.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p84.xlsx", 'path': "expt_move/resources/sequences/euro_p84.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p85.xlsx", 'path': "expt_move/resources/sequences/euro_p85.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p86.xlsx", 'path': "expt_move/resources/sequences/euro_p86.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p87.xlsx", 'path': "expt_move/resources/sequences/euro_p87.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p88.xlsx", 'path': "expt_move/resources/sequences/euro_p88.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p89.xlsx", 'path': "expt_move/resources/sequences/euro_p89.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p90.xlsx", 'path': "expt_move/resources/sequences/euro_p90.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p91.xlsx", 'path': "expt_move/resources/sequences/euro_p91.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p92.xlsx", 'path': "expt_move/resources/sequences/euro_p92.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p93.xlsx", 'path': "expt_move/resources/sequences/euro_p93.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p94.xlsx", 'path': "expt_move/resources/sequences/euro_p94.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p95.xlsx", 'path': "expt_move/resources/sequences/euro_p95.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p96.xlsx", 'path': "expt_move/resources/sequences/euro_p96.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p97.xlsx", 'path': "expt_move/resources/sequences/euro_p97.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p98.xlsx", 'path': "expt_move/resources/sequences/euro_p98.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p99.xlsx", 'path': "expt_move/resources/sequences/euro_p99.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p100.xlsx", 'path': "expt_move/resources/sequences/euro_p100.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p101.xlsx", 'path': "expt_move/resources/sequences/euro_p101.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p102.xlsx", 'path': "expt_move/resources/sequences/euro_p102.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p103.xlsx", 'path': "expt_move/resources/sequences/euro_p103.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p104.xlsx", 'path': "expt_move/resources/sequences/euro_p104.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p105.xlsx", 'path': "expt_move/resources/sequences/euro_p105.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p106.xlsx", 'path': "expt_move/resources/sequences/euro_p106.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p107.xlsx", 'path': "expt_move/resources/sequences/euro_p107.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p108.xlsx", 'path': "expt_move/resources/sequences/euro_p108.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p109.xlsx", 'path': "expt_move/resources/sequences/euro_p109.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p110.xlsx", 'path': "expt_move/resources/sequences/euro_p110.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p111.xlsx", 'path': "expt_move/resources/sequences/euro_p111.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p112.xlsx", 'path': "expt_move/resources/sequences/euro_p112.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p113.xlsx", 'path': "expt_move/resources/sequences/euro_p113.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p114.xlsx", 'path': "expt_move/resources/sequences/euro_p114.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p115.xlsx", 'path': "expt_move/resources/sequences/euro_p115.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p116.xlsx", 'path': "expt_move/resources/sequences/euro_p116.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p117.xlsx", 'path': "expt_move/resources/sequences/euro_p117.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p118.xlsx", 'path': "expt_move/resources/sequences/euro_p118.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p119.xlsx", 'path': "expt_move/resources/sequences/euro_p119.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p120.xlsx", 'path': "expt_move/resources/sequences/euro_p120.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p121.xlsx", 'path': "expt_move/resources/sequences/euro_p121.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p122.xlsx", 'path': "expt_move/resources/sequences/euro_p122.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p123.xlsx", 'path': "expt_move/resources/sequences/euro_p123.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p124.xlsx", 'path': "expt_move/resources/sequences/euro_p124.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p125.xlsx", 'path': "expt_move/resources/sequences/euro_p125.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p126.xlsx", 'path': "expt_move/resources/sequences/euro_p126.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p127.xlsx", 'path': "expt_move/resources/sequences/euro_p127.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p128.xlsx", 'path': "expt_move/resources/sequences/euro_p128.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p129.xlsx", 'path': "expt_move/resources/sequences/euro_p129.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p130.xlsx", 'path': "expt_move/resources/sequences/euro_p130.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p131.xlsx", 'path': "expt_move/resources/sequences/euro_p131.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p132.xlsx", 'path': "expt_move/resources/sequences/euro_p132.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p133.xlsx", 'path': "expt_move/resources/sequences/euro_p133.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p134.xlsx", 'path': "expt_move/resources/sequences/euro_p134.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p135.xlsx", 'path': "expt_move/resources/sequences/euro_p135.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p136.xlsx", 'path': "expt_move/resources/sequences/euro_p136.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p137.xlsx", 'path': "expt_move/resources/sequences/euro_p137.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p138.xlsx", 'path': "expt_move/resources/sequences/euro_p138.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p139.xlsx", 'path': "expt_move/resources/sequences/euro_p139.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p140.xlsx", 'path': "expt_move/resources/sequences/euro_p140.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p141.xlsx", 'path': "expt_move/resources/sequences/euro_p141.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p142.xlsx", 'path': "expt_move/resources/sequences/euro_p142.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p143.xlsx", 'path': "expt_move/resources/sequences/euro_p143.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p144.xlsx", 'path': "expt_move/resources/sequences/euro_p144.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p145.xlsx", 'path': "expt_move/resources/sequences/euro_p145.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p146.xlsx", 'path': "expt_move/resources/sequences/euro_p146.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p147.xlsx", 'path': "expt_move/resources/sequences/euro_p147.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p148.xlsx", 'path': "expt_move/resources/sequences/euro_p148.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p149.xlsx", 'path': "expt_move/resources/sequences/euro_p149.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p150.xlsx", 'path': "expt_move/resources/sequences/euro_p150.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p151.xlsx", 'path': "expt_move/resources/sequences/euro_p151.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p152.xlsx", 'path': "expt_move/resources/sequences/euro_p152.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p153.xlsx", 'path': "expt_move/resources/sequences/euro_p153.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p154.xlsx", 'path': "expt_move/resources/sequences/euro_p154.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p155.xlsx", 'path': "expt_move/resources/sequences/euro_p155.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p156.xlsx", 'path': "expt_move/resources/sequences/euro_p156.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p157.xlsx", 'path': "expt_move/resources/sequences/euro_p157.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p158.xlsx", 'path': "expt_move/resources/sequences/euro_p158.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p159.xlsx", 'path': "expt_move/resources/sequences/euro_p159.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p160.xlsx", 'path': "expt_move/resources/sequences/euro_p160.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p161.xlsx", 'path': "expt_move/resources/sequences/euro_p161.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p162.xlsx", 'path': "expt_move/resources/sequences/euro_p162.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p163.xlsx", 'path': "expt_move/resources/sequences/euro_p163.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p164.xlsx", 'path': "expt_move/resources/sequences/euro_p164.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p165.xlsx", 'path': "expt_move/resources/sequences/euro_p165.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p166.xlsx", 'path': "expt_move/resources/sequences/euro_p166.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p167.xlsx", 'path': "expt_move/resources/sequences/euro_p167.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p168.xlsx", 'path': "expt_move/resources/sequences/euro_p168.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p169.xlsx", 'path': "expt_move/resources/sequences/euro_p169.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p170.xlsx", 'path': "expt_move/resources/sequences/euro_p170.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p171.xlsx", 'path': "expt_move/resources/sequences/euro_p171.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p172.xlsx", 'path': "expt_move/resources/sequences/euro_p172.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p173.xlsx", 'path': "expt_move/resources/sequences/euro_p173.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p174.xlsx", 'path': "expt_move/resources/sequences/euro_p174.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p175.xlsx", 'path': "expt_move/resources/sequences/euro_p175.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p176.xlsx", 'path': "expt_move/resources/sequences/euro_p176.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p177.xlsx", 'path': "expt_move/resources/sequences/euro_p177.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p178.xlsx", 'path': "expt_move/resources/sequences/euro_p178.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p179.xlsx", 'path': "expt_move/resources/sequences/euro_p179.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p180.xlsx", 'path': "expt_move/resources/sequences/euro_p180.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p181.xlsx", 'path': "expt_move/resources/sequences/euro_p181.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p182.xlsx", 'path': "expt_move/resources/sequences/euro_p182.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p183.xlsx", 'path': "expt_move/resources/sequences/euro_p183.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p184.xlsx", 'path': "expt_move/resources/sequences/euro_p184.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p185.xlsx", 'path': "expt_move/resources/sequences/euro_p185.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p186.xlsx", 'path': "expt_move/resources/sequences/euro_p186.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p187.xlsx", 'path': "expt_move/resources/sequences/euro_p187.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p188.xlsx", 'path': "expt_move/resources/sequences/euro_p188.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p189.xlsx", 'path': "expt_move/resources/sequences/euro_p189.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p190.xlsx", 'path': "expt_move/resources/sequences/euro_p190.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p191.xlsx", 'path': "expt_move/resources/sequences/euro_p191.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p192.xlsx", 'path': "expt_move/resources/sequences/euro_p192.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p193.xlsx", 'path': "expt_move/resources/sequences/euro_p193.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p194.xlsx", 'path': "expt_move/resources/sequences/euro_p194.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p195.xlsx", 'path': "expt_move/resources/sequences/euro_p195.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p196.xlsx", 'path': "expt_move/resources/sequences/euro_p196.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p197.xlsx", 'path': "expt_move/resources/sequences/euro_p197.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p198.xlsx", 'path': "expt_move/resources/sequences/euro_p198.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p199.xlsx", 'path': "expt_move/resources/sequences/euro_p199.xlsx"} ,
    // {'name': "expt_move/resources/sequences/euro_p200.xlsx", 'path': "expt_move/resources/sequences/euro_p200.xlsx"} ,
    {'name': 'expt_move/resources/sequences/euro_p201.xlsx', 'path': 'expt_move/resources/sequences/euro_p201.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p202.xlsx', 'path': 'expt_move/resources/sequences/euro_p202.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p203.xlsx', 'path': 'expt_move/resources/sequences/euro_p203.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p204.xlsx', 'path': 'expt_move/resources/sequences/euro_p204.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p205.xlsx', 'path': 'expt_move/resources/sequences/euro_p205.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p206.xlsx', 'path': 'expt_move/resources/sequences/euro_p206.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p207.xlsx', 'path': 'expt_move/resources/sequences/euro_p207.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p208.xlsx', 'path': 'expt_move/resources/sequences/euro_p208.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p209.xlsx', 'path': 'expt_move/resources/sequences/euro_p209.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p210.xlsx', 'path': 'expt_move/resources/sequences/euro_p210.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p211.xlsx', 'path': 'expt_move/resources/sequences/euro_p211.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p212.xlsx', 'path': 'expt_move/resources/sequences/euro_p212.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p213.xlsx', 'path': 'expt_move/resources/sequences/euro_p213.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p214.xlsx', 'path': 'expt_move/resources/sequences/euro_p214.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p215.xlsx', 'path': 'expt_move/resources/sequences/euro_p215.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p216.xlsx', 'path': 'expt_move/resources/sequences/euro_p216.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p217.xlsx', 'path': 'expt_move/resources/sequences/euro_p217.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p218.xlsx', 'path': 'expt_move/resources/sequences/euro_p218.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p219.xlsx', 'path': 'expt_move/resources/sequences/euro_p219.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p220.xlsx', 'path': 'expt_move/resources/sequences/euro_p220.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p221.xlsx', 'path': 'expt_move/resources/sequences/euro_p221.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p222.xlsx', 'path': 'expt_move/resources/sequences/euro_p222.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p223.xlsx', 'path': 'expt_move/resources/sequences/euro_p223.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p224.xlsx', 'path': 'expt_move/resources/sequences/euro_p224.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p225.xlsx', 'path': 'expt_move/resources/sequences/euro_p225.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p226.xlsx', 'path': 'expt_move/resources/sequences/euro_p226.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p227.xlsx', 'path': 'expt_move/resources/sequences/euro_p227.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p228.xlsx', 'path': 'expt_move/resources/sequences/euro_p228.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p229.xlsx', 'path': 'expt_move/resources/sequences/euro_p229.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p230.xlsx', 'path': 'expt_move/resources/sequences/euro_p230.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p231.xlsx', 'path': 'expt_move/resources/sequences/euro_p231.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p232.xlsx', 'path': 'expt_move/resources/sequences/euro_p232.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p233.xlsx', 'path': 'expt_move/resources/sequences/euro_p233.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p234.xlsx', 'path': 'expt_move/resources/sequences/euro_p234.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p235.xlsx', 'path': 'expt_move/resources/sequences/euro_p235.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p236.xlsx', 'path': 'expt_move/resources/sequences/euro_p236.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p237.xlsx', 'path': 'expt_move/resources/sequences/euro_p237.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p238.xlsx', 'path': 'expt_move/resources/sequences/euro_p238.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p239.xlsx', 'path': 'expt_move/resources/sequences/euro_p239.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p240.xlsx', 'path': 'expt_move/resources/sequences/euro_p240.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p241.xlsx', 'path': 'expt_move/resources/sequences/euro_p241.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p242.xlsx', 'path': 'expt_move/resources/sequences/euro_p242.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p243.xlsx', 'path': 'expt_move/resources/sequences/euro_p243.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p244.xlsx', 'path': 'expt_move/resources/sequences/euro_p244.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p245.xlsx', 'path': 'expt_move/resources/sequences/euro_p245.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p246.xlsx', 'path': 'expt_move/resources/sequences/euro_p246.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p247.xlsx', 'path': 'expt_move/resources/sequences/euro_p247.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p248.xlsx', 'path': 'expt_move/resources/sequences/euro_p248.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p249.xlsx', 'path': 'expt_move/resources/sequences/euro_p249.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p250.xlsx', 'path': 'expt_move/resources/sequences/euro_p250.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p251.xlsx', 'path': 'expt_move/resources/sequences/euro_p251.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p252.xlsx', 'path': 'expt_move/resources/sequences/euro_p252.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p253.xlsx', 'path': 'expt_move/resources/sequences/euro_p253.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p254.xlsx', 'path': 'expt_move/resources/sequences/euro_p254.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p255.xlsx', 'path': 'expt_move/resources/sequences/euro_p255.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p256.xlsx', 'path': 'expt_move/resources/sequences/euro_p256.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p257.xlsx', 'path': 'expt_move/resources/sequences/euro_p257.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p258.xlsx', 'path': 'expt_move/resources/sequences/euro_p258.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p259.xlsx', 'path': 'expt_move/resources/sequences/euro_p259.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p260.xlsx', 'path': 'expt_move/resources/sequences/euro_p260.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p261.xlsx', 'path': 'expt_move/resources/sequences/euro_p261.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p262.xlsx', 'path': 'expt_move/resources/sequences/euro_p262.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p263.xlsx', 'path': 'expt_move/resources/sequences/euro_p263.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p264.xlsx', 'path': 'expt_move/resources/sequences/euro_p264.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p265.xlsx', 'path': 'expt_move/resources/sequences/euro_p265.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p266.xlsx', 'path': 'expt_move/resources/sequences/euro_p266.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p267.xlsx', 'path': 'expt_move/resources/sequences/euro_p267.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p268.xlsx', 'path': 'expt_move/resources/sequences/euro_p268.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p269.xlsx', 'path': 'expt_move/resources/sequences/euro_p269.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p270.xlsx', 'path': 'expt_move/resources/sequences/euro_p270.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p271.xlsx', 'path': 'expt_move/resources/sequences/euro_p271.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p272.xlsx', 'path': 'expt_move/resources/sequences/euro_p272.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p273.xlsx', 'path': 'expt_move/resources/sequences/euro_p273.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p274.xlsx', 'path': 'expt_move/resources/sequences/euro_p274.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p275.xlsx', 'path': 'expt_move/resources/sequences/euro_p275.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p276.xlsx', 'path': 'expt_move/resources/sequences/euro_p276.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p277.xlsx', 'path': 'expt_move/resources/sequences/euro_p277.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p278.xlsx', 'path': 'expt_move/resources/sequences/euro_p278.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p279.xlsx', 'path': 'expt_move/resources/sequences/euro_p279.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p280.xlsx', 'path': 'expt_move/resources/sequences/euro_p280.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p281.xlsx', 'path': 'expt_move/resources/sequences/euro_p281.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p282.xlsx', 'path': 'expt_move/resources/sequences/euro_p282.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p283.xlsx', 'path': 'expt_move/resources/sequences/euro_p283.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p284.xlsx', 'path': 'expt_move/resources/sequences/euro_p284.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p285.xlsx', 'path': 'expt_move/resources/sequences/euro_p285.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p286.xlsx', 'path': 'expt_move/resources/sequences/euro_p286.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p287.xlsx', 'path': 'expt_move/resources/sequences/euro_p287.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p288.xlsx', 'path': 'expt_move/resources/sequences/euro_p288.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p289.xlsx', 'path': 'expt_move/resources/sequences/euro_p289.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p290.xlsx', 'path': 'expt_move/resources/sequences/euro_p290.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p291.xlsx', 'path': 'expt_move/resources/sequences/euro_p291.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p292.xlsx', 'path': 'expt_move/resources/sequences/euro_p292.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p293.xlsx', 'path': 'expt_move/resources/sequences/euro_p293.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p294.xlsx', 'path': 'expt_move/resources/sequences/euro_p294.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p295.xlsx', 'path': 'expt_move/resources/sequences/euro_p295.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p296.xlsx', 'path': 'expt_move/resources/sequences/euro_p296.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p297.xlsx', 'path': 'expt_move/resources/sequences/euro_p297.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p298.xlsx', 'path': 'expt_move/resources/sequences/euro_p298.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p299.xlsx', 'path': 'expt_move/resources/sequences/euro_p299.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p300.xlsx', 'path': 'expt_move/resources/sequences/euro_p300.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p301.xlsx', 'path': 'expt_move/resources/sequences/euro_p301.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p302.xlsx', 'path': 'expt_move/resources/sequences/euro_p302.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p303.xlsx', 'path': 'expt_move/resources/sequences/euro_p303.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p304.xlsx', 'path': 'expt_move/resources/sequences/euro_p304.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p305.xlsx', 'path': 'expt_move/resources/sequences/euro_p305.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p306.xlsx', 'path': 'expt_move/resources/sequences/euro_p306.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p307.xlsx', 'path': 'expt_move/resources/sequences/euro_p307.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p308.xlsx', 'path': 'expt_move/resources/sequences/euro_p308.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p309.xlsx', 'path': 'expt_move/resources/sequences/euro_p309.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p310.xlsx', 'path': 'expt_move/resources/sequences/euro_p310.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p311.xlsx', 'path': 'expt_move/resources/sequences/euro_p311.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p312.xlsx', 'path': 'expt_move/resources/sequences/euro_p312.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p313.xlsx', 'path': 'expt_move/resources/sequences/euro_p313.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p314.xlsx', 'path': 'expt_move/resources/sequences/euro_p314.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p315.xlsx', 'path': 'expt_move/resources/sequences/euro_p315.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p316.xlsx', 'path': 'expt_move/resources/sequences/euro_p316.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p317.xlsx', 'path': 'expt_move/resources/sequences/euro_p317.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p318.xlsx', 'path': 'expt_move/resources/sequences/euro_p318.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p319.xlsx', 'path': 'expt_move/resources/sequences/euro_p319.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p320.xlsx', 'path': 'expt_move/resources/sequences/euro_p320.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p321.xlsx', 'path': 'expt_move/resources/sequences/euro_p321.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p322.xlsx', 'path': 'expt_move/resources/sequences/euro_p322.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p323.xlsx', 'path': 'expt_move/resources/sequences/euro_p323.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p324.xlsx', 'path': 'expt_move/resources/sequences/euro_p324.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p325.xlsx', 'path': 'expt_move/resources/sequences/euro_p325.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p326.xlsx', 'path': 'expt_move/resources/sequences/euro_p326.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p327.xlsx', 'path': 'expt_move/resources/sequences/euro_p327.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p328.xlsx', 'path': 'expt_move/resources/sequences/euro_p328.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p329.xlsx', 'path': 'expt_move/resources/sequences/euro_p329.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p330.xlsx', 'path': 'expt_move/resources/sequences/euro_p330.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p331.xlsx', 'path': 'expt_move/resources/sequences/euro_p331.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p332.xlsx', 'path': 'expt_move/resources/sequences/euro_p332.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p333.xlsx', 'path': 'expt_move/resources/sequences/euro_p333.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p334.xlsx', 'path': 'expt_move/resources/sequences/euro_p334.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p335.xlsx', 'path': 'expt_move/resources/sequences/euro_p335.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p336.xlsx', 'path': 'expt_move/resources/sequences/euro_p336.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p337.xlsx', 'path': 'expt_move/resources/sequences/euro_p337.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p338.xlsx', 'path': 'expt_move/resources/sequences/euro_p338.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p339.xlsx', 'path': 'expt_move/resources/sequences/euro_p339.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p340.xlsx', 'path': 'expt_move/resources/sequences/euro_p340.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p341.xlsx', 'path': 'expt_move/resources/sequences/euro_p341.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p342.xlsx', 'path': 'expt_move/resources/sequences/euro_p342.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p343.xlsx', 'path': 'expt_move/resources/sequences/euro_p343.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p344.xlsx', 'path': 'expt_move/resources/sequences/euro_p344.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p345.xlsx', 'path': 'expt_move/resources/sequences/euro_p345.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p346.xlsx', 'path': 'expt_move/resources/sequences/euro_p346.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p347.xlsx', 'path': 'expt_move/resources/sequences/euro_p347.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p348.xlsx', 'path': 'expt_move/resources/sequences/euro_p348.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p349.xlsx', 'path': 'expt_move/resources/sequences/euro_p349.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p350.xlsx', 'path': 'expt_move/resources/sequences/euro_p350.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p351.xlsx', 'path': 'expt_move/resources/sequences/euro_p351.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p352.xlsx', 'path': 'expt_move/resources/sequences/euro_p352.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p353.xlsx', 'path': 'expt_move/resources/sequences/euro_p353.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p354.xlsx', 'path': 'expt_move/resources/sequences/euro_p354.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p355.xlsx', 'path': 'expt_move/resources/sequences/euro_p355.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p356.xlsx', 'path': 'expt_move/resources/sequences/euro_p356.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p357.xlsx', 'path': 'expt_move/resources/sequences/euro_p357.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p358.xlsx', 'path': 'expt_move/resources/sequences/euro_p358.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p359.xlsx', 'path': 'expt_move/resources/sequences/euro_p359.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p360.xlsx', 'path': 'expt_move/resources/sequences/euro_p360.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p361.xlsx', 'path': 'expt_move/resources/sequences/euro_p361.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p362.xlsx', 'path': 'expt_move/resources/sequences/euro_p362.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p363.xlsx', 'path': 'expt_move/resources/sequences/euro_p363.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p364.xlsx', 'path': 'expt_move/resources/sequences/euro_p364.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p365.xlsx', 'path': 'expt_move/resources/sequences/euro_p365.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p366.xlsx', 'path': 'expt_move/resources/sequences/euro_p366.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p367.xlsx', 'path': 'expt_move/resources/sequences/euro_p367.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p368.xlsx', 'path': 'expt_move/resources/sequences/euro_p368.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p369.xlsx', 'path': 'expt_move/resources/sequences/euro_p369.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p370.xlsx', 'path': 'expt_move/resources/sequences/euro_p370.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p371.xlsx', 'path': 'expt_move/resources/sequences/euro_p371.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p372.xlsx', 'path': 'expt_move/resources/sequences/euro_p372.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p373.xlsx', 'path': 'expt_move/resources/sequences/euro_p373.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p374.xlsx', 'path': 'expt_move/resources/sequences/euro_p374.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p375.xlsx', 'path': 'expt_move/resources/sequences/euro_p375.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p376.xlsx', 'path': 'expt_move/resources/sequences/euro_p376.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p377.xlsx', 'path': 'expt_move/resources/sequences/euro_p377.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p378.xlsx', 'path': 'expt_move/resources/sequences/euro_p378.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p379.xlsx', 'path': 'expt_move/resources/sequences/euro_p379.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p380.xlsx', 'path': 'expt_move/resources/sequences/euro_p380.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p381.xlsx', 'path': 'expt_move/resources/sequences/euro_p381.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p382.xlsx', 'path': 'expt_move/resources/sequences/euro_p382.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p383.xlsx', 'path': 'expt_move/resources/sequences/euro_p383.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p384.xlsx', 'path': 'expt_move/resources/sequences/euro_p384.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p385.xlsx', 'path': 'expt_move/resources/sequences/euro_p385.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p386.xlsx', 'path': 'expt_move/resources/sequences/euro_p386.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p387.xlsx', 'path': 'expt_move/resources/sequences/euro_p387.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p388.xlsx', 'path': 'expt_move/resources/sequences/euro_p388.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p389.xlsx', 'path': 'expt_move/resources/sequences/euro_p389.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p390.xlsx', 'path': 'expt_move/resources/sequences/euro_p390.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p391.xlsx', 'path': 'expt_move/resources/sequences/euro_p391.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p392.xlsx', 'path': 'expt_move/resources/sequences/euro_p392.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p393.xlsx', 'path': 'expt_move/resources/sequences/euro_p393.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p394.xlsx', 'path': 'expt_move/resources/sequences/euro_p394.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p395.xlsx', 'path': 'expt_move/resources/sequences/euro_p395.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p396.xlsx', 'path': 'expt_move/resources/sequences/euro_p396.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p397.xlsx', 'path': 'expt_move/resources/sequences/euro_p397.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p398.xlsx', 'path': 'expt_move/resources/sequences/euro_p398.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p399.xlsx', 'path': 'expt_move/resources/sequences/euro_p399.xlsx'} ,
    {'name': 'expt_move/resources/sequences/euro_p400.xlsx', 'path': 'expt_move/resources/sequences/euro_p400.xlsx'} ,
    ]
});


psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.2';
  expInfo['OS'] = window.navigator.platform;
  expInfo['Participant'] = participant

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["Participant"]}_${expName}_${expInfo["date"]}`);
  // psychoJS.experiment.dataFileName = (("." + "/" + "data/" + participant.toString()) + `_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=C1EPU29I', 'https://app.prolific.co/submissions/complete?cc=C1K7X1R4');

  return Scheduler.Event.NEXT;
}


var instructionsClock;
var quick_instructionsClock;
var instr1;
var keyNext;
var random;
var thisExp;
var win;
var event;
var img_no;
var quick_img_no;
var current_img;
var quick_current_img;
var practiceBlocksClock;
var practiceBlock;
var msgStartPractice;
var key_startPrac;
var practiceMessage;
var fixation_2Clock;
var fixcross;
var practiceClock;
var practiceP1;
var practiceP2;
var practiceKey;
var msgPractice;
var acc_practice;
var prac_trial;
var tprac;
var durationBlank;
var crossPractice;
var PracFeedb_2Clock;
var practiceFeedback;
var screenAfterFB;
var attentionCheckPracClock;
var key_respAC_prac;
var AC_acc;
var hits_in_attention;
var abortMsg;
var Pos1_prac;
var Pos2_prac;
var Pos3_prac;
var Pos4_prac;
var taskAC_prac;
var ac_stim_prac;
var disturbanceClock;
var disturbed;
var keyDisturbed;
var ContinueOrEndClock;
var blockRepetitions;
var numberQuits;
var messageChecks;
var key_endFail;
var quitExperimentClock;
var LoopControl_2Clock;
var thisBlock;
var numberACresults;
var msgBlockNumber;
var main_task_blocks;
var beginBlock;
var key_respStart;
var fixation_mainClock;
var fixcross_2;
var trialClock;
var imageP1;
var imageP2;
var key_resp;
var msg;
var ntrial;
var trialReal;
var Accuracy;
var acc_feedback;
var hits_per_block;
var hits_per_block_real;
var bonus_accuracies;
var cross_objects;
var feedbackClock;
var Feedback;
var blankScreen2;
var attentionCheckClock;
var key_respAC;
var hits_in_attention2;
var Pos1;
var Pos2;
var Pos3;
var Pos4;
var shapeInstructions;
var ac_stim;
var ContinueOrEnd2Clock;
var numberQuits2;
var msgEndExperiment;
var textEndExperiment;
var pressToEndExp;
var quitExperiment2Clock;
var BlockFeedbackClock;
var msgBlock;
var feedbBlocks;
var keynextBlock;
var textBoxClock;
var textbox;
var ask_for_resp;
var endBtn_3;
var mouse;
var bonusClock;
var msgBonus;
var get_bonus;
var key_resp2;
var presentBonus;
var modify;
var finishExperimentClock;
var finalText;
var key_respEnd;
var globalClock;
var routineTimer;
var chosenVal;

var dragClock;
var mouse_drag;
var item_1;
var item_2;
var item_3;
var item_4;
var item_5;
var item_6;
var item_7;
var item__1;
var item__2;
var item__3;
var item__4;
var item__5;
var item__6;
var item__7;
var ask_for_drag;
var least_cnarcy;
var most_cnarcy;
var endBtn;
var endBtn_2;
var endBtn_3;
var selectClock;
var mouse_select;
var ask_for_select;
var dragComponents;
var selectComponents;
var pieces;
var pieces_1;
var picked
var movingPiece;
var pieces;
var grabbed;
var movePicked;
picked = []
movingPiece = null;


async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  quick_instructionsClock = new util.Clock();
  instr1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instr1', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  keyNext = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // alias for random func
  
  random = function (a) {
      return Math.random();
  }
  
  // also define randint
  
  function randint(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
  }
  
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  event=psychoJS.eventManager;
  
  // read in p=1 from the file - change later
  //var participantCount; 
  //participantCount = new TrialHandler({
  //    psychoJS: psychoJS,
  //    nReps: 1, method: TrialHandler.Method.RANDOM,
  //    extraInfo: expInfo, originPath: undefined,
  //    trialList: 'p_number_pilot.csv',
  //    seed: undefined, name: 'participantCount'
  //});
      
  //trialList = participantCount.getTrialList();    
  //p_number = trialList[0]['P_number'];
  
  //file_number = (Number.parseInt(p_number) + 1);
  
  // get width, height, browser id
  var sUsrAg;
  var nIdx;
  function getBrowserId () {
   var browsers = ["MSIE", "Firefox", "Safari", "Chrome", "Opera"];
   sUsrAg = window.navigator.userAgent,
   nIdx = browsers.length - 1;
   for (nIdx; nIdx > -1 && sUsrAg.indexOf(browsers [nIdx]) === -1; nIdx--);
   
    return browsers[nIdx];
  }
   
  expInfo['browser'] = getBrowserId();
  expInfo['xResolution'] = screen.width;
  expInfo['yResolution'] = screen.height;
  //W = screen.width;
  //H = screen.height;
  // Run 'Begin Experiment' code from imagesSlides
  img_no = 1;
  current_img = ((("expt_move/resources/instructions/Slide") + img_no.toString()) + ".jpg");
  quick_img_no = 1;
  quick_current_img = ((("expt_move/resources/quick_instructions/Slide") + quick_img_no.toString()) + ".jpg");
  
  // Initialize components for Routine "practiceBlocks"
  practiceBlocksClock = new util.Clock();
  // Run 'Begin Experiment' code from codePracStart
  // Counter for the practice blocks
  practiceBlock = 0;
  
  // Message to be updated before every practice block
  msgStartPractice = "message shown before a practice Block";

  
  
  key_startPrac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  practiceMessage = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceMessage',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  fixcross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixcross', units : 'pix', 
    vertices: 'cross', size:[20, 20],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  
  
  // Initialize components for Routine "practice"
  practiceClock = new util.Clock();
  practiceP1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practiceP1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 250), 0], size : [200, 200],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  practiceP2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practiceP2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [250, 0], size : [200, 200],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  practiceKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from practiceFeedb
  msgPractice = "Feedback msg after practice trial";
  acc_practice = [];
  prac_trial = 0;
  tprac = [];
  durationBlank = 0.0;
  
  crossPractice = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crossPractice', units : 'pix', 
    vertices: 'cross', size:[20, 20],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1.0, depth: -4, interpolate: true,
  });
  
  // Initialize components for Routine "PracFeedb_2"
  PracFeedb_2Clock = new util.Clock();
  practiceFeedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceFeedback',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  screenAfterFB = new visual.TextStim({
    win: psychoJS.window,
    name: 'screenAfterFB',
    text: 'Any text\n\nincluding line breaks',
    font: 'Calibri',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "attentionCheckPrac"
  attentionCheckPracClock = new util.Clock();
  key_respAC_prac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from run_check_prac
  AC_acc = [];
  hits_in_attention = 0;
  abortMsg = "";
  
  Pos1_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos1_prac',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  Pos2_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos2_prac',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0.3, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  Pos3_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos3_prac',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  Pos4_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos4_prac',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [(- 0.3), 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  taskAC_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskAC_prac',
    text: 'Use arrow keys to pick the number shown in the center',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  ac_stim_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'ac_stim_prac',
    text: '',
    font: 'Calibri',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "disturbance"
  disturbanceClock = new util.Clock();
  disturbed = new visual.TextStim({
    win: psychoJS.window,
    name: 'disturbed',
    text: "Were things around you quiet during the last block?\n\nPress '1' if you were disturbed and '0' if you were NOT disturbed.\n\nPlease do NOT use the NumPad.",
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  keyDisturbed = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ContinueOrEnd"
  ContinueOrEndClock = new util.Clock();
  // Run 'Begin Experiment' code from AccuracyCheck
  blockRepetitions = 0;
  numberQuits = 0;
  
  messageChecks = new visual.TextStim({
    win: psychoJS.window,
    name: 'messageChecks',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_endFail = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quitExperiment"
  quitExperimentClock = new util.Clock();
  // Initialize components for Routine "LoopControl_2"
  LoopControl_2Clock = new util.Clock();
  // Run 'Begin Experiment' code from LoopContr
  thisBlock = 0;
  numberACresults = 0;
  msgBlockNumber = "which block we say we starting";


  // load conditions file 

  main_task_blocks = (("expt_move/resources/sequences/euro_p" + participant.toString()) + ".xlsx");

  
  // main_task_blocks = (("expt_move/resources/sequences/euro_p" + expInfo["Participant"].toString()) + ".xlsx");
  
  beginBlock = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginBlock',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_respStart = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_main"
  fixation_mainClock = new util.Clock();
  fixcross_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixcross_2', units : 'pix', 
    vertices: 'cross', size:[20, 20],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  //trialtimer = new util.Clock(); //define a beginning of exp timer
  
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  imageP1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageP1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 250), 0], size : [200, 200],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  imageP2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageP2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [250, 0], size : [200, 200],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from Feedb
  msg = "Feedback msg after trial";
  ntrial = 0;
  trialReal = [];
  Accuracy = [];
  acc_feedback = [];
  hits_per_block = 0;
  hits_per_block_real = 0;
  bonus_accuracies = [];
  
  cross_objects = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cross_objects', units : 'pix', 
    vertices: 'cross', size:[20, 20],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1.0, depth: -4, interpolate: true,
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  Feedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  blankScreen2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankScreen2',
    text: 'Any text\n\nincluding line breaks',
    font: 'Calibri',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "attentionCheck"
  attentionCheckClock = new util.Clock();
  key_respAC = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from run_check
  AC_acc = [];
  hits_in_attention2 = 0;
  
  Pos1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos1',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  Pos2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos2',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0.3, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  Pos3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos3',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  Pos4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos4',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [(- 0.3), 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  shapeInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'shapeInstructions',
    text: 'Use arrow keys to pick the number shown in the center',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  ac_stim = new visual.TextStim({
    win: psychoJS.window,
    name: 'ac_stim',
    text: '',
    font: 'Calibri',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "ContinueOrEnd2"
  ContinueOrEnd2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_3
  numberQuits2 = 0;
  msgEndExperiment = "text after attention checks";
  
  textEndExperiment = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEndExperiment',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  pressToEndExp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quitExperiment2"
  quitExperiment2Clock = new util.Clock();
  // Initialize components for Routine "BlockFeedback"
  BlockFeedbackClock = new util.Clock();
  // Run 'Begin Experiment' code from fbBlock
  msgBlock = "fb after Block";
  
  feedbBlocks = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbBlocks',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  keynextBlock = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // alias for random func
  
  random = function (a) {
      return Math.random();
  }
  
  // also define randint
  
  function randint(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
  }
  
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  event=psychoJS.eventManager;
  
  // read in p=1 from the file - change later
  //var participantCount; 
  //participantCount = new TrialHandler({
  //    psychoJS: psychoJS,
  //    nReps: 1, method: TrialHandler.Method.RANDOM,
  //    extraInfo: expInfo, originPath: undefined,
  //    trialList: 'p_number_pilot.csv',
  //    seed: undefined, name: 'participantCount'
  //});
      
  //trialList = participantCount.getTrialList();    
  //p_number = trialList[0]['P_number'];
  
  //file_number = (Number.parseInt(p_number) + 1);
  
  // get width, height, browser id
  var sUsrAg;
  var nIdx;
  function getBrowserId () {
   var browsers = ["MSIE", "Firefox", "Safari", "Chrome", "Opera"];
   sUsrAg = window.navigator.userAgent,
   nIdx = browsers.length - 1;
   for (nIdx; nIdx > -1 && sUsrAg.indexOf(browsers [nIdx]) === -1; nIdx--);
   
    return browsers[nIdx];
  }
   
  expInfo['browser'] = getBrowserId();
  expInfo['xResolution'] = screen.width;
  expInfo['yResolution'] = screen.height;
  //W = screen.width;
  //H = screen.height;
  // Run 'Begin Experiment' code from imagesSlides_2
  

// Initialize components for Routine "drag"
  dragClock = new util.Clock();
  mouse_drag = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_drag.mouseClock = new util.Clock();
  
  // Run 'Begin Experiment' code from code
  // movePicked = function(picked, mouse, grabbed) {
  //   var piece;
  //   if (((grabbed !== null) && mouse.isPressedIn(grabbed))) {
  //       grabbed.pos = mouse.getPos();
  //       return grabbed;
  //   } else {
  //       for (var p, _pj_c = 0, _pj_a = util.range(picked.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
  //           p = _pj_a[_pj_c];
  //           piece = picked[p];
  //           if ((mouse.isPressedIn(piece) && (grabbed === null))) {
  //               return piece;
  //           }
  //       }
  //   }
  // }
  movePicked = function(picked, mouse, grabbed) {
    if (grabbed != 'undefined' &&  mouse.getPressed()[0] === 1) {
      grabbed.pos = mouse.getPos();
      return grabbed
    } else {
        for (let piece of picked) {
          if (piece.contains(mouse) &&  mouse.getPressed()[0] === 1 && grabbed === 'undefined'){
            piece.pos = mouse.getPos();
            return piece;
          }
        }
    return 'undefined'
    }
  }
  
  item_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : '01_scarf.jpg', units : undefined, 
    image : 'expt_move/resources/stim_IDs/01_scarf.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  item_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : '02_radio.jpg', units : undefined, 
    image : 'expt_move/resources/stim_IDs/02_radio.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  item_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : '03_dress.jpg', units : undefined, 
    image : 'expt_move/resources/stim_IDs/03_dress.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  item_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : '04_satellite_dish.jpg', units : undefined, 
    image : 'expt_move/resources/stim_IDs/04_satellite_dish.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  item_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : '05_hat.jpg', units : undefined, 
    image : 'expt_move/resources/stim_IDs/05_hat.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  item_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : '06_slipper.jpg', units : undefined, 
    image : 'expt_move/resources/stim_IDs/06_slipper.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  item_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : '07_phone.jpg', units : undefined, 
    image : 'expt_move/resources/stim_IDs/07_phone.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  ask_for_drag = new visual.TextStim({
    win: psychoJS.window,
    name: 'ask_for_drag',
    text: 'Please arrange the items according to how cnarcy you thought they were at the end of the experiment. Click, hold and drag the items to move them.',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -9.0 
  });
  
  least_cnarcy = new visual.TextStim({
    win: psychoJS.window,
    name: 'least_cnarcy',
    text: 'Least cnarcy',
    font: 'Sans Serif',
    units: undefined, 
    pos: [(- 0.5), (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -10.0 
  });
  
  most_cnarcy = new visual.TextStim({
    win: psychoJS.window,
    name: 'most_cnarcy',
    text: 'Most cnarcy',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0.5, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -11.0 
  });
  
  endBtn = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'endBtn',
    text: 'Click to continue',
    fillColor: 'black',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.4)],
    letterHeight: 0.05,
    size: [0.5, 0.07]
  });
  endBtn.clock = new util.Clock();



  
  // Initialize components for Routine "select"
  selectClock = new util.Clock();
  mouse_select = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_select.mouseClock = new util.Clock();
  item__1 = new visual.ImageStim({
    win : psychoJS.window,
    name : '01__scarf', units : undefined, 
    image : 'expt_move/resources/stim_IDs/01_scarf.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  item__2 = new visual.ImageStim({
    win : psychoJS.window,
    name : '02__radio', units : undefined, 
    image : 'expt_move/resources/stim_IDs/02_radio.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  item__3 = new visual.ImageStim({
    win : psychoJS.window,
    name : '03__dress', units : undefined, 
    image : 'expt_move/resources/stim_IDs/03_dress.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  item__4 = new visual.ImageStim({
    win : psychoJS.window,
    name : '04__satellite_dish', units : undefined, 
    image : 'expt_move/resources/stim_IDs/04_satellite_dish.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  item__5 = new visual.ImageStim({
    win : psychoJS.window,
    name : '05__hat', units : undefined, 
    image : 'expt_move/resources/stim_IDs/05_hat.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  item__6 = new visual.ImageStim({
    win : psychoJS.window,
    name : '06__slipper', units : undefined, 
    image : 'expt_move/resources/stim_IDs/06_slipper.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  item__7 = new visual.ImageStim({
    win : psychoJS.window,
    name : '07__phone', units : undefined, 
    image : 'expt_move/resources/stim_IDs/07_phone.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  ask_for_select = new visual.TextStim({
    win: psychoJS.window,
    name: 'ask_for_select',
    text: 'Did you notice any items changing how cnarcy they were? If so, please select them by clicking. \nNOTE: you cannot unselect items once you click them, so choose carefully.',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -9.0 
  });
  
  endBtn_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'endBtn_2',
    text: 'Click to continue',
    fillColor: 'black',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.4)],
    letterHeight: 0.05,
    size: [0.5, 0.07]
  });
  endBtn_2.clock = new util.Clock();



  // Initialize components for Routine "textBox"
  textBoxClock = new util.Clock();
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    font: 'Open Sans',
    pos: [0, (- 0.18)], letterHeight: 0.04,
    size: [null, null],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 1.0,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  ask_for_resp = new visual.TextStim({
    win: psychoJS.window,
    name: 'ask_for_resp',
    text: 'Please write down any comments you would like to share on, for example, how you performed the task, the feedback you received, how difficult the task was etc. \n\n[When you are finished, click the button below to go to the final screen]',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -1.0 
  });
  

  endBtn_3 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'endBtn_3',
    text: 'Click to continue',
    fillColor: 'black',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.4)],
    letterHeight: 0.05,
    size: [0.5, 0.07]
  });
  endBtn_3.clock = new util.Clock();
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();

  // Initialize components for Routine "bonus"
  bonusClock = new util.Clock();
  // Run 'Begin Experiment' code from bonusCode
  msgBonus = "Feedback msg to say if participant gets bonus";
  get_bonus = [];
  
  key_resp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  presentBonus = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentBonus',
    text: '',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });

  
  // Initialize components for Routine "finishExperiment"
  finishExperimentClock = new util.Clock();
  finalText = new visual.TextStim({
    win: psychoJS.window,
    name: 'finalText',
    text: 'Great! You finished the task. Thank you! \nPress space to exit and please wait until you get redirected back to Prolific. ',
    font: 'Sans Serif',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_respEnd = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}



var instructionsLoop;
function instructionsLoopLoopBegin(instructionsLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    instructionsLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 100, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'instructionsLoop'
    });
    psychoJS.experiment.addLoop(instructionsLoop); // add the loop to the experiment
    currentLoop = instructionsLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisInstructionsLoop of instructionsLoop) {
      snapshot = instructionsLoop.getSnapshot();
      instructionsLoopLoopScheduler.add(importConditions(snapshot));
      instructionsLoopLoopScheduler.add(instructionsRoutineBegin(snapshot));
      instructionsLoopLoopScheduler.add(instructionsRoutineEachFrame());
      instructionsLoopLoopScheduler.add(instructionsRoutineEnd(snapshot));
      instructionsLoopLoopScheduler.add(instructionsLoopLoopEndIteration(instructionsLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function instructionsLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(instructionsLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function instructionsLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var quick_instructionsLoop;
function quick_instructionsLoopLoopBegin(quick_instructionsLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    quick_instructionsLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 100, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'quick_instructionsLoop'
    });
    psychoJS.experiment.addLoop(quick_instructionsLoop); // add the loop to the experiment
    currentLoop = quick_instructionsLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisquick_instructionsLoop of quick_instructionsLoop) {
      snapshot = quick_instructionsLoop.getSnapshot();
      quick_instructionsLoopLoopScheduler.add(importConditions(snapshot));
      quick_instructionsLoopLoopScheduler.add(quick_instructionsRoutineBegin(snapshot));
      quick_instructionsLoopLoopScheduler.add(quick_instructionsRoutineEachFrame());
      quick_instructionsLoopLoopScheduler.add(quick_instructionsRoutineEnd(snapshot));
      quick_instructionsLoopLoopScheduler.add(quick_instructionsLoopLoopEndIteration(quick_instructionsLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function quick_instructionsLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(quick_instructionsLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function quick_instructionsLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var repPractice;
function repPracticeLoopBegin(repPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    repPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'repPractice'
    });
    psychoJS.experiment.addLoop(repPractice); // add the loop to the experiment
    currentLoop = repPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRepPractice of repPractice) {
      snapshot = repPractice.getSnapshot();
      repPracticeLoopScheduler.add(importConditions(snapshot));
      repPracticeLoopScheduler.add(practiceBlocksRoutineBegin(snapshot));
      repPracticeLoopScheduler.add(practiceBlocksRoutineEachFrame());
      repPracticeLoopScheduler.add(practiceBlocksRoutineEnd(snapshot));
      const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
      repPracticeLoopScheduler.add(practiceTrialsLoopBegin(practiceTrialsLoopScheduler, snapshot));
      repPracticeLoopScheduler.add(practiceTrialsLoopScheduler);
      repPracticeLoopScheduler.add(practiceTrialsLoopEnd);
      const AttentionsLoopScheduler = new Scheduler(psychoJS);
      repPracticeLoopScheduler.add(AttentionsLoopBegin(AttentionsLoopScheduler, snapshot));
      repPracticeLoopScheduler.add(AttentionsLoopScheduler);
      repPracticeLoopScheduler.add(AttentionsLoopEnd);
      repPracticeLoopScheduler.add(disturbanceRoutineBegin(snapshot));
      repPracticeLoopScheduler.add(disturbanceRoutineEachFrame());
      repPracticeLoopScheduler.add(disturbanceRoutineEnd(snapshot));
      repPracticeLoopScheduler.add(repPracticeLoopEndIteration(repPracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var practiceTrials;
function practiceTrialsLoopBegin(practiceTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, conditions_practice, myIndices),
      seed: undefined, name: 'practiceTrials'
    });
    psychoJS.experiment.addLoop(practiceTrials); // add the loop to the experiment
    currentLoop = practiceTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracticeTrial of practiceTrials) {
      snapshot = practiceTrials.getSnapshot();
      practiceTrialsLoopScheduler.add(importConditions(snapshot));
      practiceTrialsLoopScheduler.add(fixation_2RoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(fixation_2RoutineEachFrame());
      practiceTrialsLoopScheduler.add(fixation_2RoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practiceRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(practiceRoutineEachFrame());
      practiceTrialsLoopScheduler.add(practiceRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(PracFeedb_2RoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(PracFeedb_2RoutineEachFrame());
      practiceTrialsLoopScheduler.add(PracFeedb_2RoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practiceTrialsLoopEndIteration(practiceTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Attentions;
function AttentionsLoopBegin(AttentionsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Attentions = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, "expt_move/resources/attentionChecks.xlsx", '0:4'),
      seed: undefined, name: 'Attentions'
    });
    psychoJS.experiment.addLoop(Attentions); // add the loop to the experiment
    currentLoop = Attentions;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisAttention of Attentions) {
      snapshot = Attentions.getSnapshot();
      AttentionsLoopScheduler.add(importConditions(snapshot));
      AttentionsLoopScheduler.add(attentionCheckPracRoutineBegin(snapshot));
      AttentionsLoopScheduler.add(attentionCheckPracRoutineEachFrame());
      AttentionsLoopScheduler.add(attentionCheckPracRoutineEnd(snapshot));
      AttentionsLoopScheduler.add(AttentionsLoopEndIteration(AttentionsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function AttentionsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Attentions);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function AttentionsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function repPracticeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(repPractice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function repPracticeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var quitExpLoop;
function quitExpLoopLoopBegin(quitExpLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    quitExpLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: numberQuits, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'quitExpLoop'
    });
    psychoJS.experiment.addLoop(quitExpLoop); // add the loop to the experiment
    currentLoop = quitExpLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisQuitExpLoop of quitExpLoop) {
      snapshot = quitExpLoop.getSnapshot();
      quitExpLoopLoopScheduler.add(importConditions(snapshot));
      quitExpLoopLoopScheduler.add(quitExperimentRoutineBegin(snapshot));
      quitExpLoopLoopScheduler.add(quitExperimentRoutineEachFrame());
      quitExpLoopLoopScheduler.add(quitExperimentRoutineEnd(snapshot));
      quitExpLoopLoopScheduler.add(quitExpLoopLoopEndIteration(quitExpLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function quitExpLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(quitExpLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function quitExpLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var repBlocks;
function repBlocksLoopBegin(repBlocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    repBlocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: blockRepetitions, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'repBlocks'
    });
    psychoJS.experiment.addLoop(repBlocks); // add the loop to the experiment
    currentLoop = repBlocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRepBlock of repBlocks) {
      snapshot = repBlocks.getSnapshot();
      repBlocksLoopScheduler.add(importConditions(snapshot));
      repBlocksLoopScheduler.add(LoopControl_2RoutineBegin(snapshot));
      repBlocksLoopScheduler.add(LoopControl_2RoutineEachFrame());
      repBlocksLoopScheduler.add(LoopControl_2RoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      repBlocksLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      repBlocksLoopScheduler.add(trialsLoopScheduler);
      repBlocksLoopScheduler.add(trialsLoopEnd);
      const trials_ACLoopScheduler = new Scheduler(psychoJS);
      repBlocksLoopScheduler.add(trials_ACLoopBegin(trials_ACLoopScheduler, snapshot));
      repBlocksLoopScheduler.add(trials_ACLoopScheduler);
      repBlocksLoopScheduler.add(trials_ACLoopEnd);
      const presentACresultsLoopScheduler = new Scheduler(psychoJS);
      repBlocksLoopScheduler.add(presentACresultsLoopBegin(presentACresultsLoopScheduler, snapshot));
      repBlocksLoopScheduler.add(presentACresultsLoopScheduler);
      repBlocksLoopScheduler.add(presentACresultsLoopEnd);
      const quitExpLoop2LoopScheduler = new Scheduler(psychoJS);
      repBlocksLoopScheduler.add(quitExpLoop2LoopBegin(quitExpLoop2LoopScheduler, snapshot));
      repBlocksLoopScheduler.add(quitExpLoop2LoopScheduler);
      repBlocksLoopScheduler.add(quitExpLoop2LoopEnd);
      repBlocksLoopScheduler.add(BlockFeedbackRoutineBegin(snapshot));
      repBlocksLoopScheduler.add(BlockFeedbackRoutineEachFrame());
      repBlocksLoopScheduler.add(BlockFeedbackRoutineEnd(snapshot));
      repBlocksLoopScheduler.add(disturbanceRoutineBegin(snapshot));
      repBlocksLoopScheduler.add(disturbanceRoutineEachFrame());
      repBlocksLoopScheduler.add(disturbanceRoutineEnd(snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, main_task_blocks, MyIndicesMain),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixation_mainRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixation_mainRoutineEachFrame());
      trialsLoopScheduler.add(fixation_mainRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_AC;
function trials_ACLoopBegin(trials_ACLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_AC = new TrialHandler({
      psychoJS: psychoJS,
      nReps: repsAC, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: "expt_move/resources/attentionChecks.xlsx",
      seed: undefined, name: 'trials_AC'
    });
    psychoJS.experiment.addLoop(trials_AC); // add the loop to the experiment
    currentLoop = trials_AC;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_AC of trials_AC) {
      snapshot = trials_AC.getSnapshot();
      trials_ACLoopScheduler.add(importConditions(snapshot));
      trials_ACLoopScheduler.add(attentionCheckRoutineBegin(snapshot));
      trials_ACLoopScheduler.add(attentionCheckRoutineEachFrame());
      trials_ACLoopScheduler.add(attentionCheckRoutineEnd(snapshot));
      trials_ACLoopScheduler.add(trials_ACLoopEndIteration(trials_ACLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_ACLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_AC);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_ACLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var presentACresults;
function presentACresultsLoopBegin(presentACresultsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    presentACresults = new TrialHandler({
      psychoJS: psychoJS,
      nReps: numberACresults, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'presentACresults'
    });
    psychoJS.experiment.addLoop(presentACresults); // add the loop to the experiment
    currentLoop = presentACresults;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPresentACresult of presentACresults) {
      snapshot = presentACresults.getSnapshot();
      presentACresultsLoopScheduler.add(importConditions(snapshot));
      presentACresultsLoopScheduler.add(ContinueOrEnd2RoutineBegin(snapshot));
      presentACresultsLoopScheduler.add(ContinueOrEnd2RoutineEachFrame());
      presentACresultsLoopScheduler.add(ContinueOrEnd2RoutineEnd(snapshot));
      presentACresultsLoopScheduler.add(presentACresultsLoopEndIteration(presentACresultsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function presentACresultsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(presentACresults);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function presentACresultsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var quitExpLoop2;
function quitExpLoop2LoopBegin(quitExpLoop2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    quitExpLoop2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: numberQuits2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'quitExpLoop2'
    });
    psychoJS.experiment.addLoop(quitExpLoop2); // add the loop to the experiment
    currentLoop = quitExpLoop2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisQuitExpLoop2 of quitExpLoop2) {
      snapshot = quitExpLoop2.getSnapshot();
      quitExpLoop2LoopScheduler.add(importConditions(snapshot));
      quitExpLoop2LoopScheduler.add(quitExperiment2RoutineBegin(snapshot));
      quitExpLoop2LoopScheduler.add(quitExperiment2RoutineEachFrame());
      quitExpLoop2LoopScheduler.add(quitExperiment2RoutineEnd(snapshot));
      quitExpLoop2LoopScheduler.add(quitExpLoop2LoopEndIteration(quitExpLoop2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function quitExpLoop2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(quitExpLoop2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function quitExpLoop2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function repBlocksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(repBlocks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function repBlocksLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var BonusLoop;
function BonusLoopLoopBegin(BonusLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    BonusLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: repsBonus, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'BonusLoop'
    });
    psychoJS.experiment.addLoop(BonusLoop); // add the loop to the experiment
    currentLoop = BonusLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBonusLoop of BonusLoop) {
      snapshot = BonusLoop.getSnapshot();
      BonusLoopLoopScheduler.add(importConditions(snapshot));
      BonusLoopLoopScheduler.add(bonusRoutineBegin(snapshot));
      BonusLoopLoopScheduler.add(bonusRoutineEachFrame());
      BonusLoopLoopScheduler.add(bonusRoutineEnd(snapshot));
      BonusLoopLoopScheduler.add(BonusLoopLoopEndIteration(BonusLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function BonusLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(BonusLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function BonusLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var _keyNext_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instr1.setImage(current_img);
    keyNext.keys = undefined;
    keyNext.rt = undefined;
    _keyNext_allKeys = [];
    // Run 'Begin Routine' code from imagesSlides
    current_img = ((("expt_move/resources/instructions/Slide") + img_no.toString()) + ".jpg");
    
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instr1);
    instructionsComponents.push(keyNext);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1* updates
    if (t >= 0.0 && instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1.tStart = t;  // (not accounting for frame time here)
      instr1.frameNStart = frameN;  // exact frame index
      
      instr1.setAutoDraw(true);
    }

    
    // *keyNext* updates
    if (t >= 0.0 && keyNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyNext.tStart = t;  // (not accounting for frame time here)
      keyNext.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyNext.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyNext.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyNext.clearEvents(); });
    }

    if (keyNext.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyNext.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _keyNext_allKeys = _keyNext_allKeys.concat(theseKeys);
      if (_keyNext_allKeys.length > 0) {
        keyNext.keys = _keyNext_allKeys[_keyNext_allKeys.length - 1].name;  // just the last key pressed
        keyNext.rt = _keyNext_allKeys[_keyNext_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    keyNext.stop();
    // Run 'End Routine' code from imagesSlides
    if (((img_no > 1) && ((keyNext.keys === "left".toString()) || (keyNext.keys === "left")))) {
        img_no -= 1;
    } else {
        if (((img_no < n_instructions) && ((keyNext.keys === "right".toString()) || (keyNext.keys === "right")))) {
            img_no += 1;
        } else {
            if (((img_no === n_instructions) && ((keyNext.keys === "space") || (keyNext.keys === "space".toString())))) {
                instructionsLoop.finished = true;
            }
        }
    }
    current_img = ((("expt_move/resources/instructions/Slide") + img_no.toString()) + ".jpg");
    
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

// quick loop
var t;
var frameN;
var continueRoutine;
var _keyNext_allKeys;
var quick_instructionsComponents;
function quick_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quick_instructions' ---
    t = 0;
    quick_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instr1.setImage(quick_current_img);
    keyNext.keys = undefined;
    keyNext.rt = undefined;
    _keyNext_allKeys = [];
    // Run 'Begin Routine' code from imagesSlides
    quick_current_img = ((("expt_move/resources/quick_instructions/Slide") + quick_img_no.toString()) + ".jpg");
    
    // keep track of which components have finished
    quick_instructionsComponents = [];
    quick_instructionsComponents.push(instr1);
    quick_instructionsComponents.push(keyNext);
    
    for (const thisComponent of quick_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function quick_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quick_instructions' ---
    // get current time
    t = quick_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1* updates
    if (t >= 0.0 && instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1.tStart = t;  // (not accounting for frame time here)
      instr1.frameNStart = frameN;  // exact frame index
      
      instr1.setAutoDraw(true);
    }

    
    // *keyNext* updates
    if (t >= 0.0 && keyNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyNext.tStart = t;  // (not accounting for frame time here)
      keyNext.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyNext.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyNext.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyNext.clearEvents(); });
    }

    if (keyNext.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyNext.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _keyNext_allKeys = _keyNext_allKeys.concat(theseKeys);
      if (_keyNext_allKeys.length > 0) {
        keyNext.keys = _keyNext_allKeys[_keyNext_allKeys.length - 1].name;  // just the last key pressed
        keyNext.rt = _keyNext_allKeys[_keyNext_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of quick_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quick_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quick_instructions' ---
    for (const thisComponent of quick_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    keyNext.stop();
    // Run 'End Routine' code from imagesSlides
    if (((quick_img_no > 1) && ((keyNext.keys === "left".toString()) || (keyNext.keys === "left")))) {
        quick_img_no -= 1;
    } else {
        if (((quick_img_no < n_instructions_quick) && ((keyNext.keys === "right".toString()) || (keyNext.keys === "right")))) {
            quick_img_no += 1;
        } else {
            if (((quick_img_no === n_instructions_quick) && ((keyNext.keys === "space") || (keyNext.keys === "space".toString())))) {
                quick_instructionsLoop.finished = true;
            }
        }
    }
    quick_current_img = ((("expt_move/resources/quick_instructions/Slide") + quick_img_no.toString()) + ".jpg");
    
    // the Routine "quick_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var myIndices;
var _key_startPrac_allKeys;
var practiceBlocksComponents;
function practiceBlocksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceBlocks' ---
    t = 0;
    practiceBlocksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codePracStart
    practiceBlock += 1;
    
    // For each block choose rows from the excel file that controls the loop 
    if ((practiceBlock === 1)) {
        myIndices = "0:8";
        msgStartPractice = "Let's start practising this task.\nDon't worry about making mistakes, just try to understand the goal for this task.\n[Press space bar to continue]";
    } else {
        myIndices = "8:16";
        msgStartPractice = "This is the second practice block. \nAgain, relax and try to get familiar with the task and the timing. Don't worry about mistakes.\n[Press space bar to start]";
    }
    
    key_startPrac.keys = undefined;
    key_startPrac.rt = undefined;
    _key_startPrac_allKeys = [];
    practiceMessage.setText(msgStartPractice);
    // keep track of which components have finished
    practiceBlocksComponents = [];
    practiceBlocksComponents.push(key_startPrac);
    practiceBlocksComponents.push(practiceMessage);
    
    for (const thisComponent of practiceBlocksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practiceBlocksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceBlocks' ---
    // get current time
    t = practiceBlocksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_startPrac* updates
    if (t >= 0.0 && key_startPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_startPrac.tStart = t;  // (not accounting for frame time here)
      key_startPrac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_startPrac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_startPrac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_startPrac.clearEvents(); });
    }

    if (key_startPrac.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_startPrac.getKeys({keyList: ['space'], waitRelease: false});
      _key_startPrac_allKeys = _key_startPrac_allKeys.concat(theseKeys);
      if (_key_startPrac_allKeys.length > 0) {
        key_startPrac.keys = _key_startPrac_allKeys[_key_startPrac_allKeys.length - 1].name;  // just the last key pressed
        key_startPrac.rt = _key_startPrac_allKeys[_key_startPrac_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *practiceMessage* updates
    if (t >= 0.0 && practiceMessage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceMessage.tStart = t;  // (not accounting for frame time here)
      practiceMessage.frameNStart = frameN;  // exact frame index
      
      practiceMessage.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceBlocksComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceBlocksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceBlocks' ---
    for (const thisComponent of practiceBlocksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_startPrac.stop();
    // the Routine "practiceBlocks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var fixTiming;
var jitter;
var routineStart;
var fixation_2Components;
function fixation_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_2' ---
    t = 0;
    fixation_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fixcross_prac_duration
    /* Syntax Error: Fix Python code */
    // keep track of which components have finished
    fixation_2Components = [];
    fixation_2Components.push(fixcross);
    
    for (const thisComponent of fixation_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixation_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_2' ---
    // get current time
    t = fixation_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixcross* updates
    if (frameN >= 0 && fixcross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixcross.tStart = t;  // (not accounting for frame time here)
      fixcross.frameNStart = frameN;  // exact frame index
      
      fixcross.setAutoDraw(true);
    }

    if (fixcross.status === PsychoJS.Status.STARTED && t >= (fixcross.tStart + 0.5)) {
      fixcross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixation_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_2' ---
    for (const thisComponent of fixation_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Store onset of the fix cross in practice to the output file
    psychoJS.experiment.addData('fix_onset', routineStart + fixcross.tStart);
    
    // the Routine "fixation_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _practiceKey_allKeys;
var crossDisappear;
var practiceComponents;
function practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice' ---
    t = 0;
    practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    practiceP1.setImage(LocItem1);
    practiceP2.setImage(LocItem2);
    practiceKey.keys = undefined;
    practiceKey.rt = undefined;
    _practiceKey_allKeys = [];
    // Run 'Begin Routine' code from practiceFeedb
    prac_trial += 1;
    tprac = prac_trial;
    psychoJS.experiment.addData("tprac", tprac);
    crossDisappear = 1;
    
    // keep track of which components have finished
    practiceComponents = [];
    practiceComponents.push(practiceP1);
    practiceComponents.push(practiceP2);
    practiceComponents.push(practiceKey);
    practiceComponents.push(crossPractice);
    
    for (const thisComponent of practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice' ---
    // get current time
    t = practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practiceP1* updates
    if (t >= 0.0 && practiceP1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceP1.tStart = t;  // (not accounting for frame time here)
      practiceP1.frameNStart = frameN;  // exact frame index
      
      practiceP1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practiceP1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practiceP1.setAutoDraw(false);
    }
    
    // *practiceP2* updates
    if (t >= 0.0 && practiceP2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceP2.tStart = t;  // (not accounting for frame time here)
      practiceP2.frameNStart = frameN;  // exact frame index
      
      practiceP2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practiceP2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practiceP2.setAutoDraw(false);
    }
    
    // *practiceKey* updates
    if (t >= 0.0 && practiceKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceKey.tStart = t;  // (not accounting for frame time here)
      practiceKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practiceKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practiceKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practiceKey.clearEvents(); });
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practiceKey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practiceKey.status = PsychoJS.Status.FINISHED;
  }

    if (practiceKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = practiceKey.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _practiceKey_allKeys = _practiceKey_allKeys.concat(theseKeys);
      if (_practiceKey_allKeys.length > 0) {
        practiceKey.keys = _practiceKey_allKeys[0].name;  // just the first key pressed
        practiceKey.rt = _practiceKey_allKeys[0].rt;
      }
    }
    
    // Run 'Each Frame' code from practiceFeedb
    if (((practiceKey.keys === "left") || (practiceKey.keys === "right"))) {
        crossDisappear = 0;
    }
    
    
    // *crossPractice* updates
    if (t >= 0.0 && crossPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crossPractice.tStart = t;  // (not accounting for frame time here)
      crossPractice.frameNStart = frameN;  // exact frame index
      
      crossPractice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crossPractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crossPractice.setAutoDraw(false);
    }
    
    if (crossPractice.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crossPractice.setOpacity(crossDisappear, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var valueDiff;
var value_dist;
var value_dist_abs;
function practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice' ---
    for (const thisComponent of practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practiceKey.corr, level);
    }
    psychoJS.experiment.addData('practiceKey.keys', practiceKey.keys);
    if (typeof practiceKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practiceKey.rt', practiceKey.rt);
        }
    
    practiceKey.stop();
    // Run 'End Routine' code from practiceFeedb
    if ((practiceKey.keys === "left")) {
        valueDiff = (P1 - P2);
    }
    if ((practiceKey.keys === "right")) {
        valueDiff = (P2 - P1);
    }
    if ((practiceKey.keys === undefined)) {
        valueDiff = undefined;
    }
    value_dist = (P1 - P2);
    value_dist_abs = Math.abs(value_dist);
    if ((practiceKey.keys === undefined)) {
        msgPractice = "TRY TO RESPOND FASTER";        
    } else {
        if ((Feedback_on === 0)) {
            msgPractice = "";
            durationBlank = 0.0;
        } else {
            if ((Feedback_on === 1)) {
                durationBlank = 0.5;
                if ((InverseFb === 1)) {
                    if ((valueDiff > 0)) {
                        msgPractice = "Incorrect";
                    } else {
                        if ((valueDiff < 0)) {
                            msgPractice = "Correct";
                        }
                    }
                } else {
                    if ((InverseFb === 0)) {
                        if ((valueDiff > 0)) {
                            msgPractice = "Correct";
                        } else {
                            if ((valueDiff < 0)) {
                                msgPractice = "Incorrect";
                            }
                        }
                    }
                }
            }
        }
    }
    if ((valueDiff === undefined)) {
        acc_practice = 2;
    } else {
        if ((valueDiff > 0)) {
            acc_practice = 1;
        } else {
            if ((valueDiff < 0)) {
                acc_practice = 0;
            }
        }
    }
    psychoJS.experiment.addData("acc_practice", acc_practice);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var startFeedb;
var PracFeedb_2Components;
function PracFeedb_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PracFeedb_2' ---
    t = 0;
    PracFeedb_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    practiceFeedback.setText(msgPractice);
    startFeedb = globalClock.getTime();
    // keep track of which components have finished
    PracFeedb_2Components = [];
    PracFeedb_2Components.push(practiceFeedback);
    PracFeedb_2Components.push(screenAfterFB);
    
    for (const thisComponent of PracFeedb_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracFeedb_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PracFeedb_2' ---
    // get current time
    t = PracFeedb_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practiceFeedback* updates
    if (t >= 0.0 && practiceFeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceFeedback.tStart = t;  // (not accounting for frame time here)
      practiceFeedback.frameNStart = frameN;  // exact frame index
      
      practiceFeedback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practiceFeedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practiceFeedback.setAutoDraw(false);
    }
    
    // *screenAfterFB* updates
    if (t >= 0.5 && screenAfterFB.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      screenAfterFB.tStart = t;  // (not accounting for frame time here)
      screenAfterFB.frameNStart = frameN;  // exact frame index
      
      screenAfterFB.setAutoDraw(true);
    }

    frameRemains = 0.5 + durationBlank - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (screenAfterFB.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      screenAfterFB.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracFeedb_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracFeedb_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PracFeedb_2' ---
    for (const thisComponent of PracFeedb_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Store onset of feedbakc during practice
    psychoJS.experiment.addData('onsetFeedbPrac', startFeedb + practiceFeedback.tStart);
    // the Routine "PracFeedb_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_respAC_prac_allKeys;
var attentionCheckPracComponents;
function attentionCheckPracRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'attentionCheckPrac' ---
    t = 0;
    attentionCheckPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    key_respAC_prac.keys = undefined;
    key_respAC_prac.rt = undefined;
    _key_respAC_prac_allKeys = [];
    Pos1_prac.setText(Loc1);
    Pos2_prac.setText(Loc2);
    Pos3_prac.setText(Loc3);
    Pos4_prac.setText(Loc4);
    ac_stim_prac.setText(Stim);
    // keep track of which components have finished
    attentionCheckPracComponents = [];
    attentionCheckPracComponents.push(key_respAC_prac);
    attentionCheckPracComponents.push(Pos1_prac);
    attentionCheckPracComponents.push(Pos2_prac);
    attentionCheckPracComponents.push(Pos3_prac);
    attentionCheckPracComponents.push(Pos4_prac);
    attentionCheckPracComponents.push(taskAC_prac);
    attentionCheckPracComponents.push(ac_stim_prac);
    
    for (const thisComponent of attentionCheckPracComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function attentionCheckPracRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'attentionCheckPrac' ---
    // get current time
    t = attentionCheckPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_respAC_prac* updates
    if (t >= 0.0 && key_respAC_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respAC_prac.tStart = t;  // (not accounting for frame time here)
      key_respAC_prac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respAC_prac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respAC_prac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respAC_prac.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_respAC_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_respAC_prac.status = PsychoJS.Status.FINISHED;
  }

    if (key_respAC_prac.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respAC_prac.getKeys({keyList: ['up', 'down', 'left', 'right'], waitRelease: false});
      _key_respAC_prac_allKeys = _key_respAC_prac_allKeys.concat(theseKeys);
      if (_key_respAC_prac_allKeys.length > 0) {
        key_respAC_prac.keys = _key_respAC_prac_allKeys[0].name;  // just the first key pressed
        key_respAC_prac.rt = _key_respAC_prac_allKeys[0].rt;
        // was this correct?
        if (key_respAC_prac.keys == CorrAns) {
            key_respAC_prac.corr = 1;
        } else {
            key_respAC_prac.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Pos1_prac* updates
    if (t >= 0.0 && Pos1_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos1_prac.tStart = t;  // (not accounting for frame time here)
      Pos1_prac.frameNStart = frameN;  // exact frame index
      
      Pos1_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos1_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos1_prac.setAutoDraw(false);
    }
    
    // *Pos2_prac* updates
    if (t >= 0.0 && Pos2_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos2_prac.tStart = t;  // (not accounting for frame time here)
      Pos2_prac.frameNStart = frameN;  // exact frame index
      
      Pos2_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos2_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos2_prac.setAutoDraw(false);
    }
    
    // *Pos3_prac* updates
    if (t >= 0.0 && Pos3_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos3_prac.tStart = t;  // (not accounting for frame time here)
      Pos3_prac.frameNStart = frameN;  // exact frame index
      
      Pos3_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos3_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos3_prac.setAutoDraw(false);
    }
    
    // *Pos4_prac* updates
    if (t >= 0.0 && Pos4_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos4_prac.tStart = t;  // (not accounting for frame time here)
      Pos4_prac.frameNStart = frameN;  // exact frame index
      
      Pos4_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos4_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos4_prac.setAutoDraw(false);
    }
    
    // *taskAC_prac* updates
    if (t >= 0.0 && taskAC_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskAC_prac.tStart = t;  // (not accounting for frame time here)
      taskAC_prac.frameNStart = frameN;  // exact frame index
      
      taskAC_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (taskAC_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      taskAC_prac.setAutoDraw(false);
    }
    
    // *ac_stim_prac* updates
    if (t >= 0.0 && ac_stim_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ac_stim_prac.tStart = t;  // (not accounting for frame time here)
      ac_stim_prac.frameNStart = frameN;  // exact frame index
      
      ac_stim_prac.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ac_stim_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ac_stim_prac.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of attentionCheckPracComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function attentionCheckPracRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'attentionCheckPrac' ---
    for (const thisComponent of attentionCheckPracComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_respAC_prac.keys === undefined) {
      if (['None','none',undefined].includes(CorrAns)) {
         key_respAC_prac.corr = 1;  // correct non-response
      } else {
         key_respAC_prac.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respAC_prac.corr, level);
    }
    psychoJS.experiment.addData('key_respAC_prac.keys', key_respAC_prac.keys);
    psychoJS.experiment.addData('key_respAC_prac.corr', key_respAC_prac.corr);
    if (typeof key_respAC_prac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respAC_prac.rt', key_respAC_prac.rt);
        routineTimer.reset();
        }
    
    key_respAC_prac.stop();
    // Run 'End Routine' code from run_check_prac
    // Add accuracy in attention checks to output file 
    if (key_respAC_prac.corr) {
        AC_acc = 1;
        hits_in_attention += 1;
    } else {
        AC_acc = 0;
    }
    psychoJS.experiment.addData("AC_acc", AC_acc);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyDisturbed_allKeys;
var disturbanceComponents;
function disturbanceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'disturbance' ---
    t = 0;
    disturbanceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyDisturbed.keys = undefined;
    keyDisturbed.rt = undefined;
    _keyDisturbed_allKeys = [];
    // keep track of which components have finished
    disturbanceComponents = [];
    disturbanceComponents.push(disturbed);
    disturbanceComponents.push(keyDisturbed);
    
    for (const thisComponent of disturbanceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function disturbanceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'disturbance' ---
    // get current time
    t = disturbanceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *disturbed* updates
    if (t >= 0.0 && disturbed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      disturbed.tStart = t;  // (not accounting for frame time here)
      disturbed.frameNStart = frameN;  // exact frame index
      
      disturbed.setAutoDraw(true);
    }

    
    // *keyDisturbed* updates
    if (t >= 0.0 && keyDisturbed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyDisturbed.tStart = t;  // (not accounting for frame time here)
      keyDisturbed.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      keyDisturbed.clock.reset();
      keyDisturbed.start();
      keyDisturbed.clearEvents();
    }

    if (keyDisturbed.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyDisturbed.getKeys({keyList: ['1', '0'], waitRelease: false});
      _keyDisturbed_allKeys = _keyDisturbed_allKeys.concat(theseKeys);
      if (_keyDisturbed_allKeys.length > 0) {
        keyDisturbed.keys = _keyDisturbed_allKeys[_keyDisturbed_allKeys.length - 1].name;  // just the last key pressed
        keyDisturbed.rt = _keyDisturbed_allKeys[_keyDisturbed_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of disturbanceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function disturbanceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'disturbance' ---
    for (const thisComponent of disturbanceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyDisturbed.corr, level);
    }
    psychoJS.experiment.addData('keyDisturbed.keys', keyDisturbed.keys);
    if (typeof keyDisturbed.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyDisturbed.rt', keyDisturbed.rt);
        routineTimer.reset();
        }
    
    keyDisturbed.stop();
    // the Routine "disturbance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var check_AC_acc;
var repsBonus;
var _key_endFail_allKeys;
var ContinueOrEndComponents;
function ContinueOrEndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ContinueOrEnd' ---
    t = 0;
    ContinueOrEndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from AccuracyCheck
    check_AC_acc = (Number.parseFloat(hits_in_attention) / 8.0);
    if ((check_AC_acc < 0.5)) {
        blockRepetitions = 0;
        repsBonus = 0;
        abortMsg = "Your accuracy in the attention checks is too low. \nYou have reached the end of the experiment. \nPress space to quit the experiment. Thank you!";
        numberQuits = 1;
    } else {
        blockRepetitions = 6;
        repsBonus = 1;
        abortMsg = "You passed the attention checks. \n[ Press space bar to continue ]";
        numberQuits = 0;
    }
    
    messageChecks.setText(abortMsg);
    key_endFail.keys = undefined;
    key_endFail.rt = undefined;
    _key_endFail_allKeys = [];
    // keep track of which components have finished
    ContinueOrEndComponents = [];
    ContinueOrEndComponents.push(messageChecks);
    ContinueOrEndComponents.push(key_endFail);
    
    for (const thisComponent of ContinueOrEndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ContinueOrEndRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ContinueOrEnd' ---
    // get current time
    t = ContinueOrEndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *messageChecks* updates
    if (t >= 0.0 && messageChecks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      messageChecks.tStart = t;  // (not accounting for frame time here)
      messageChecks.frameNStart = frameN;  // exact frame index
      
      messageChecks.setAutoDraw(true);
    }

    
    // *key_endFail* updates
    if (t >= 0.0 && key_endFail.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_endFail.tStart = t;  // (not accounting for frame time here)
      key_endFail.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_endFail.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_endFail.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_endFail.clearEvents(); });
    }

    if (key_endFail.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_endFail.getKeys({keyList: ['space'], waitRelease: false});
      _key_endFail_allKeys = _key_endFail_allKeys.concat(theseKeys);
      if (_key_endFail_allKeys.length > 0) {
        key_endFail.keys = _key_endFail_allKeys[_key_endFail_allKeys.length - 1].name;  // just the last key pressed
        key_endFail.rt = _key_endFail_allKeys[_key_endFail_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ContinueOrEndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ContinueOrEndRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ContinueOrEnd' ---
    for (const thisComponent of ContinueOrEndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_endFail.stop();
    // the Routine "ContinueOrEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quitExperimentComponents;
function quitExperimentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quitExperiment' ---
    t = 0;
    quitExperimentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from quitExpCode
    psychoJS.quit();
    // keep track of which components have finished
    quitExperimentComponents = [];
    
    for (const thisComponent of quitExperimentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function quitExperimentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quitExperiment' ---
    // get current time
    t = quitExperimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of quitExperimentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quitExperimentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quitExperiment' ---
    for (const thisComponent of quitExperimentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "quitExperiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var MyIndicesMain;
var uroInstructions;
var repsAC;
var _key_respStart_allKeys;
var LoopControl_2Components;
function LoopControl_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'LoopControl_2' ---
    t = 0;
    LoopControl_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from LoopContr
    thisBlock += 1;


    // indices for expt involving 8 stimuli:

    // if ((expt_n === 1)) {
    //     if ((thisBlock === 1)) {
    //         MyIndicesMain = "0:70";
    //     } else {
    //         if ((thisBlock === 2)) {
    //             MyIndicesMain = "70:140";
    //         } else {
    //             if ((thisBlock === 3)) {
    //                 MyIndicesMain = "140:210";
    //             } else {
    //                 if ((thisBlock === 4)) {
    //                     MyIndicesMain = "210:282";
    //                 } else {
    //                     if ((thisBlock === 5)) {
    //                         MyIndicesMain = "282:354";
    //                     } else {
    //                         if ((thisBlock === 6)) {
    //                             MyIndicesMain = "354:426";
    //                         }
    //                     }
    //                 }
    //             }
    //         }
    //     }
    // } else {
    //     if ((expt_n === 2)) {
    //         if ((thisBlock === 1)) {
    //             MyIndicesMain = "0:54";
    //         } else {
    //             if ((thisBlock === 2)) {
    //                 MyIndicesMain = "54:108";
    //             } else {
    //                 if ((thisBlock === 3)) {
    //                     MyIndicesMain = "108:162";
    //                 } else {
    //                     if ((thisBlock === 4)) {
    //                         MyIndicesMain = "162:234";
    //                     } else {
    //                         if ((thisBlock === 5)) {
    //                             MyIndicesMain = "234:306";
    //                         } else {
    //                             if ((thisBlock === 6)) {
    //                                 MyIndicesMain = "306:378";
    //                             }
    //                         }
    //                     }
    //                 }
    //             }
    //         }
    //     } else {
    //         if ((expt_n === 3)) {
    //             if ((thisBlock === 1)) {
    //                 MyIndicesMain = "0:54";
    //             } else {
    //                 if ((thisBlock === 2)) {
    //                     MyIndicesMain = "54:108";
    //                 } else {
    //                     if ((thisBlock === 3)) {
    //                         MyIndicesMain = "108:162";
    //                     } else {
    //                         if ((thisBlock === 4)) {
    //                             MyIndicesMain = "162:232";
    //                         } else {
    //                             if ((thisBlock === 5)) {
    //                                 MyIndicesMain = "232:302";
    //                             } else {
    //                                 if ((thisBlock === 6)) {
    //                                     MyIndicesMain = "302:372";
    //                                 }
    //                             }
    //                         }
    //                     }
    //                 }
    //             }
    //         }
    //     }
    // }



    // indices for expt involving 7 stimuli and 6 blocks
      if ((thisBlock === 1)) {
          MyIndicesMain = "0:54";
      } else {
          if ((thisBlock === 2)) {
              MyIndicesMain = "54:108";
          } else {
              if ((thisBlock === 3)) {
                  MyIndicesMain = "108:162";
              } else {
                  if ((thisBlock === 4)) {
                      MyIndicesMain = "162:216";
                  } else {
                      if ((thisBlock === 5)) {
                          MyIndicesMain = "216:270";
                      } else {
                          if ((thisBlock === 6)) {
                              MyIndicesMain = "270:324";
                          }
                      }
                  }
              }
          }
      }

  
      
    msgBlockNumber = (("You will now start block " + thisBlock.toString()) + " out of 6. \n \nRemember that both accuracy and speed matter. \n \nAlso, remember that certain items may (or may not) change how cnarcy they are. \n \n[Press space bar to begin.]");
    if ((thisBlock === 3)) {
        uroInstructions = 0;
        repsAC = 1;
        numberACresults = 1;
    } else {
        uroInstructions = 0;
        repsAC = 0;
        numberACresults = 0;
    }

    // if ((thisBlock === 0)) {
    //   uroInstructions = 1;
    //   // repsAC = 1;
    //   // numberACresults = 1;
    // }


    
    beginBlock.setText(msgBlockNumber);
    key_respStart.keys = undefined;
    key_respStart.rt = undefined;
    _key_respStart_allKeys = [];
    // keep track of which components have finished
    LoopControl_2Components = [];
    LoopControl_2Components.push(beginBlock);
    LoopControl_2Components.push(key_respStart);
    
    for (const thisComponent of LoopControl_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function LoopControl_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'LoopControl_2' ---
    // get current time
    t = LoopControl_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *beginBlock* updates
    if (t >= 0.0 && beginBlock.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beginBlock.tStart = t;  // (not accounting for frame time here)
      beginBlock.frameNStart = frameN;  // exact frame index
      
      beginBlock.setAutoDraw(true);
    }

    
    // *key_respStart* updates
    if (t >= 0.0 && key_respStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respStart.tStart = t;  // (not accounting for frame time here)
      key_respStart.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respStart.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respStart.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respStart.clearEvents(); });
    }

    if (key_respStart.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respStart.getKeys({keyList: ['space'], waitRelease: false});
      _key_respStart_allKeys = _key_respStart_allKeys.concat(theseKeys);
      if (_key_respStart_allKeys.length > 0) {
        key_respStart.keys = _key_respStart_allKeys[_key_respStart_allKeys.length - 1].name;  // just the last key pressed
        key_respStart.rt = _key_respStart_allKeys[_key_respStart_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LoopControl_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LoopControl_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'LoopControl_2' ---
    for (const thisComponent of LoopControl_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_respStart.stop();
    // the Routine "LoopControl_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

var routineFixStart;
var fixation_mainComponents;
function fixation_mainRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_main' ---
    t = 0;
    fixation_mainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    /* Syntax Error: Fix Python code */
    // keep track of which components have finished
    fixation_mainComponents = [];
    fixation_mainComponents.push(fixcross_2);
    
    for (const thisComponent of fixation_mainComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixation_mainRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_main' ---
    // get current time
    t = fixation_mainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixcross_2* updates
    if (frameN >= 0 && fixcross_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixcross_2.tStart = t;  // (not accounting for frame time here)
      fixcross_2.frameNStart = frameN;  // exact frame index
      
      fixcross_2.setAutoDraw(true);
    }

    frameRemains = 0.5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((fixcross_2.status === PsychoJS.Status.STARTED || fixcross_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      fixcross_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixation_mainComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation_mainRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_main' ---
    for (const thisComponent of fixation_mainComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Store onset of the fixation cross in the main task to the output file
    psychoJS.experiment.addData("fixcross_onsetMain", routineFixStart + fixcross_2.tStart);
    // the Routine "fixation_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    imageP1.setImage(Path_1);
    imageP2.setImage(Path_2);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // Run 'Begin Routine' code from Feedb
    ntrial += 1;
    trialReal = ntrial;
    psychoJS.experiment.addData("Trial", trialReal);
    crossDisappear = 1;
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(imageP1);
    trialComponents.push(imageP2);
    trialComponents.push(key_resp);
    trialComponents.push(cross_objects);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imageP1* updates
    if (t >= 0 && imageP1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageP1.tStart = t;  // (not accounting for frame time here)
      imageP1.frameNStart = frameN;  // exact frame index
      
      imageP1.setAutoDraw(true);
    }

    frameRemains = 0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageP1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageP1.setAutoDraw(false);
    }
    
    // *imageP2* updates
    if (t >= 0 && imageP2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageP2.tStart = t;  // (not accounting for frame time here)
      imageP2.frameNStart = frameN;  // exact frame index
      
      imageP2.setAutoDraw(true);
    }

    frameRemains = 0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageP2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageP2.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[0].name;  // just the first key pressed
        key_resp.rt = _key_resp_allKeys[0].rt;
      }
    }
    
    // Run 'Each Frame' code from Feedb
    if (((key_resp.keys === "left") || (key_resp.keys === "right"))) {
        crossDisappear = 0;
    }
    
    
    // *cross_objects* updates
    if (t >= 0.0 && cross_objects.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross_objects.tStart = t;  // (not accounting for frame time here)
      cross_objects.frameNStart = frameN;  // exact frame index
      
      cross_objects.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cross_objects.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cross_objects.setAutoDraw(false);
    }
    
    if (cross_objects.status === PsychoJS.Status.STARTED){ // only update if being drawn
      cross_objects.setOpacity(crossDisappear, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        }
    
    key_resp.stop();
    // Run 'End Routine' code from Feedb
    if ((key_resp.keys === "left")) {
        chosenVal = Item_1
        psychoJS.experiment.addData("Chosen_name", Image_1);
        psychoJS.experiment.addData("Chosen_item", Item_1);
        psychoJS.experiment.addData("Chosen_rank", Rank_1);
    } else {
        if ((key_resp.keys === "right")) {
            chosenVal = Item_2
            psychoJS.experiment.addData("Chosen_name", Image_2);
            psychoJS.experiment.addData("Chosen_item", Item_2);
            psychoJS.experiment.addData("Chosen_rank", Rank_2);
        } else {
            if ((key_resp.keys === undefined)) {
                psychoJS.experiment.addData("Chosen_name", undefined);
                psychoJS.experiment.addData("Chosen_item", undefined);
                psychoJS.experiment.addData("Chosen_rank", undefined);
            }
        }
    }
    if ((key_resp.keys === undefined)) {
        msg = "TRY TO RESPOND FASTER";
        acc_feedback = 2;
        Accuracy = 2;
        durationBlank = 0.5;
    } else {

      // no feedback
        if ((Feedback_on === 0)) {
            msg = "";
            durationBlank = 0.0;
            acc_feedback = 3;
            if ((chosenVal === Winner)) {
                Accuracy = 1;
                hits_per_block_real = (hits_per_block_real + 1);
            } else {
                if ((chosenVal === Loser)) {
                    Accuracy = 0;
                }
            }

        // feedback
        } else {
            if ((Feedback_on === 1)) {
                durationBlank = 0.5;

                if ((chosenVal === Winner)) {
                    msg = "Correct";
                    acc_feedback = 1;
                    Accuracy = 1;
                    hits_per_block_real = (hits_per_block_real + 1);
                } else {
                    if ((chosenVal === Loser)) {
                        msg = "Incorrect";
                        acc_feedback = 0;
                        Accuracy = 0;
                    }
                }

            }
        }
    }
    // if ((chosenVal === undefined)) {
    //     Accuracy = 2;
    // psychoJS.experiment.addData("diff_chosen_minus_reject", valueDiff);
    psychoJS.experiment.addData("Accuracy", Accuracy);
    psychoJS.experiment.addData("Acc_feedback", acc_feedback);
    psychoJS.experiment.addData("Direction", Direction);
    
    bonus_accuracies.push(Accuracy);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var startFeedbMain;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Feedback.setText(msg);
    // Store time when the feedback routine is starting 
    startFeedbMain = globalClock.getTime();
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(Feedback);
    feedbackComponents.push(blankScreen2);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Feedback* updates
    if (t >= 0.0 && Feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Feedback.tStart = t;  // (not accounting for frame time here)
      Feedback.frameNStart = frameN;  // exact frame index
      
      Feedback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Feedback.setAutoDraw(false);
    }
    
    // *blankScreen2* updates
    if (t >= 0.6 && blankScreen2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blankScreen2.tStart = t;  // (not accounting for frame time here)
      blankScreen2.frameNStart = frameN;  // exact frame index
      
      blankScreen2.setAutoDraw(true);
    }

    frameRemains = 0.6 + durationBlank - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blankScreen2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blankScreen2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Add onset of feedback message to output file
    psychoJS.experiment.addData('feedb_onset', startFeedbMain + Feedback.tStart);
    // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_respAC_allKeys;
var attentionCheckComponents;
function attentionCheckRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'attentionCheck' ---
    t = 0;
    attentionCheckClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    key_respAC.keys = undefined;
    key_respAC.rt = undefined;
    _key_respAC_allKeys = [];
    Pos1.setText(Loc1);
    Pos2.setText(Loc2);
    Pos3.setText(Loc3);
    Pos4.setText(Loc4);
    ac_stim.setText(Stim);
    // keep track of which components have finished
    attentionCheckComponents = [];
    attentionCheckComponents.push(key_respAC);
    attentionCheckComponents.push(Pos1);
    attentionCheckComponents.push(Pos2);
    attentionCheckComponents.push(Pos3);
    attentionCheckComponents.push(Pos4);
    attentionCheckComponents.push(shapeInstructions);
    attentionCheckComponents.push(ac_stim);
    
    for (const thisComponent of attentionCheckComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function attentionCheckRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'attentionCheck' ---
    // get current time
    t = attentionCheckClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_respAC* updates
    if (t >= 0.0 && key_respAC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respAC.tStart = t;  // (not accounting for frame time here)
      key_respAC.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respAC.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respAC.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respAC.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_respAC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_respAC.status = PsychoJS.Status.FINISHED;
  }

    if (key_respAC.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respAC.getKeys({keyList: ['up', 'down', 'left', 'right'], waitRelease: false});
      _key_respAC_allKeys = _key_respAC_allKeys.concat(theseKeys);
      if (_key_respAC_allKeys.length > 0) {
        key_respAC.keys = _key_respAC_allKeys[0].name;  // just the first key pressed
        key_respAC.rt = _key_respAC_allKeys[0].rt;
        // was this correct?
        if (key_respAC.keys == CorrAns) {
            key_respAC.corr = 1;
        } else {
            key_respAC.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Pos1* updates
    if (t >= 0.0 && Pos1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos1.tStart = t;  // (not accounting for frame time here)
      Pos1.frameNStart = frameN;  // exact frame index
      
      Pos1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos1.setAutoDraw(false);
    }
    
    // *Pos2* updates
    if (t >= 0.0 && Pos2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos2.tStart = t;  // (not accounting for frame time here)
      Pos2.frameNStart = frameN;  // exact frame index
      
      Pos2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos2.setAutoDraw(false);
    }
    
    // *Pos3* updates
    if (t >= 0.0 && Pos3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos3.tStart = t;  // (not accounting for frame time here)
      Pos3.frameNStart = frameN;  // exact frame index
      
      Pos3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos3.setAutoDraw(false);
    }
    
    // *Pos4* updates
    if (t >= 0.0 && Pos4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos4.tStart = t;  // (not accounting for frame time here)
      Pos4.frameNStart = frameN;  // exact frame index
      
      Pos4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Pos4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Pos4.setAutoDraw(false);
    }
    
    // *shapeInstructions* updates
    if (t >= 0.0 && shapeInstructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shapeInstructions.tStart = t;  // (not accounting for frame time here)
      shapeInstructions.frameNStart = frameN;  // exact frame index
      
      shapeInstructions.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (shapeInstructions.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      shapeInstructions.setAutoDraw(false);
    }
    
    // *ac_stim* updates
    if (t >= 0.0 && ac_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ac_stim.tStart = t;  // (not accounting for frame time here)
      ac_stim.frameNStart = frameN;  // exact frame index
      
      ac_stim.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ac_stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ac_stim.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of attentionCheckComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function attentionCheckRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'attentionCheck' ---
    for (const thisComponent of attentionCheckComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_respAC.keys === undefined) {
      if (['None','none',undefined].includes(CorrAns)) {
         key_respAC.corr = 1;  // correct non-response
      } else {
         key_respAC.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respAC.corr, level);
    }
    psychoJS.experiment.addData('key_respAC.keys', key_respAC.keys);
    psychoJS.experiment.addData('key_respAC.corr', key_respAC.corr);
    if (typeof key_respAC.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respAC.rt', key_respAC.rt);
        routineTimer.reset();
        }
    
    key_respAC.stop();
    // Run 'End Routine' code from run_check
    if (key_respAC.corr) {
        AC_acc = 1;
        hits_in_attention2 += 1;
    } else {
        AC_acc = 0;
    }
    thisExp.addData("AC_acc", AC_acc);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var check_AC_acc_2;
var _pressToEndExp_allKeys;
var ContinueOrEnd2Components;
function ContinueOrEnd2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ContinueOrEnd2' ---
    t = 0;
    ContinueOrEnd2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_3
    check_AC_acc_2 = (Number.parseFloat(hits_in_attention2) / 8.0);
    if ((check_AC_acc_2 < 0.5)) {
        msgEndExperiment = "Your accuracy in the attention checks is too low. \nYou have reached the end of the experiment. \nPress the space to quit the experiment. Thank you!";
        numberQuits2 = 1;
    } else {
        msgEndExperiment = "You passed the attention checks. \nPress space to see your feedback for the block.";
        numberQuits2 = 0;
    }
    
    textEndExperiment.setText(msgEndExperiment);
    pressToEndExp.keys = undefined;
    pressToEndExp.rt = undefined;
    _pressToEndExp_allKeys = [];
    // keep track of which components have finished
    ContinueOrEnd2Components = [];
    ContinueOrEnd2Components.push(textEndExperiment);
    ContinueOrEnd2Components.push(pressToEndExp);
    
    for (const thisComponent of ContinueOrEnd2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ContinueOrEnd2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ContinueOrEnd2' ---
    // get current time
    t = ContinueOrEnd2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEndExperiment* updates
    if (t >= 0.0 && textEndExperiment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEndExperiment.tStart = t;  // (not accounting for frame time here)
      textEndExperiment.frameNStart = frameN;  // exact frame index
      
      textEndExperiment.setAutoDraw(true);
    }

    
    // *pressToEndExp* updates
    if (t >= 0.0 && pressToEndExp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pressToEndExp.tStart = t;  // (not accounting for frame time here)
      pressToEndExp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pressToEndExp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pressToEndExp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pressToEndExp.clearEvents(); });
    }

    if (pressToEndExp.status === PsychoJS.Status.STARTED) {
      let theseKeys = pressToEndExp.getKeys({keyList: ['space'], waitRelease: false});
      _pressToEndExp_allKeys = _pressToEndExp_allKeys.concat(theseKeys);
      if (_pressToEndExp_allKeys.length > 0) {
        pressToEndExp.keys = _pressToEndExp_allKeys[_pressToEndExp_allKeys.length - 1].name;  // just the last key pressed
        pressToEndExp.rt = _pressToEndExp_allKeys[_pressToEndExp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ContinueOrEnd2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ContinueOrEnd2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ContinueOrEnd2' ---
    for (const thisComponent of ContinueOrEnd2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    pressToEndExp.stop();
    // the Routine "ContinueOrEnd2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quitExperiment2Components;
function quitExperiment2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quitExperiment2' ---
    t = 0;
    quitExperiment2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from quitExpCode_2
    psychoJS.quit();
    // keep track of which components have finished
    quitExperiment2Components = [];
    
    for (const thisComponent of quitExperiment2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function quitExperiment2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quitExperiment2' ---
    // get current time
    t = quitExperiment2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of quitExperiment2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quitExperiment2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quitExperiment2' ---
    for (const thisComponent of quitExperiment2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "quitExperiment2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var previous_block_acc;
var _keynextBlock_allKeys;
var BlockFeedbackComponents;
function BlockFeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'BlockFeedback' ---
    t = 0;
    BlockFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fbBlock
    // Calculate accuracy in the block and in attention checks
    previous_block_acc = (Number.parseFloat(hits_per_block_real) / (ntrial));
    check_AC_acc = (hits_in_attention2 / 8);
    
    
    
    // Present messages depending on percentage of correct answers
    if ((previous_block_acc >= 0.8)) {
        msgBlock = "Amazing, your accuracy in the block was really high!\nRemember, the number of correct trials will determine the chance to get the bonus payment. [Press space bar to continue.]";
    } else {
        if (((previous_block_acc < 0.8) && (previous_block_acc >= 0.6))) {
            msgBlock = "Your accuracy in the block was great! You are doing an excellent job!\nRemember, the number of correct trials will determine the chance to get the bonus payment. [Press space bar to continue.]";
        } else {
            if (((previous_block_acc < 0.6) && (previous_block_acc >= 0.5))) {
                msgBlock = "Your accuracy in the block was good. However, there is still room for improvement!\nRemember, the number of correct trials will determine the chance to get the bonus payment. [Press space bar to continue.]";
            } else {
                if ((previous_block_acc < 0.5)) {
                    msgBlock = "Your accuracy in the block was a bit low. \nDon't give up! You will surely improve it.\nRemember, the number of correct trials will determine the chance to get the bonus payment. [Press space bar to continue.]";
                }
            }
        }
    }
    
    feedbBlocks.setText(msgBlock);
    keynextBlock.keys = undefined;
    keynextBlock.rt = undefined;
    _keynextBlock_allKeys = [];
    // keep track of which components have finished
    BlockFeedbackComponents = [];
    BlockFeedbackComponents.push(feedbBlocks);
    BlockFeedbackComponents.push(keynextBlock);
    
    for (const thisComponent of BlockFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function BlockFeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'BlockFeedback' ---
    // get current time
    t = BlockFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbBlocks* updates
    if (t >= 0.0 && feedbBlocks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbBlocks.tStart = t;  // (not accounting for frame time here)
      feedbBlocks.frameNStart = frameN;  // exact frame index
      
      feedbBlocks.setAutoDraw(true);
    }

    
    // *keynextBlock* updates
    if (t >= 0.0 && keynextBlock.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keynextBlock.tStart = t;  // (not accounting for frame time here)
      keynextBlock.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keynextBlock.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keynextBlock.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keynextBlock.clearEvents(); });
    }

    if (keynextBlock.status === PsychoJS.Status.STARTED) {
      let theseKeys = keynextBlock.getKeys({keyList: ['space'], waitRelease: false});
      _keynextBlock_allKeys = _keynextBlock_allKeys.concat(theseKeys);
      if (_keynextBlock_allKeys.length > 0) {
        keynextBlock.keys = _keynextBlock_allKeys[_keynextBlock_allKeys.length - 1].name;  // just the last key pressed
        keynextBlock.rt = _keynextBlock_allKeys[_keynextBlock_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BlockFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BlockFeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'BlockFeedback' ---
    for (const thisComponent of BlockFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    keynextBlock.stop();
    // the Routine "BlockFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}



// drag functions
function dragRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'drag' ---
    t = 0;
    dragClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_drag
    // current position of the mouse:
    mouse_drag.x = [];
    mouse_drag.y = [];
    mouse_drag.leftButton = [];
    mouse_drag.midButton = [];
    mouse_drag.rightButton = [];
    mouse_drag.time = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code
    pieces = [item_1, item_2, item_3, item_4, item_5, item_6, item_7];
    for (var p, _pj_c = 0, _pj_a = util.range(pieces.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        p = _pj_a[_pj_c];

        // randomly displace the position of each item slightly
        const rand_x = 0.1  * Math.sqrt(-2 * Math.log(Math.random())) * Math.cos(2 * Math.PI * Math.random());
        const rand_y = 0.05 * Math.sqrt(-2 * Math.log(Math.random())) * Math.cos(2 * Math.PI * Math.random());
        pieces[p].pos = [rand_x, rand_y];
    }
    picked = [];
    movingPiece = 'undefined';
    
    // keep track of which components have finished
    dragComponents = [];
    dragComponents.push(mouse_drag);
    dragComponents.push(item_1);
    dragComponents.push(item_2);
    dragComponents.push(item_3);
    dragComponents.push(item_4);
    dragComponents.push(item_5);
    dragComponents.push(item_6);
    dragComponents.push(item_7);
    dragComponents.push(ask_for_drag);
    dragComponents.push(least_cnarcy);
    dragComponents.push(most_cnarcy);
    dragComponents.push(endBtn);
    
    for (const thisComponent of dragComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function dragRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'drag' ---
    // get current time
    t = dragClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_drag* updates
    if (t >= 0 && mouse_drag.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_drag.tStart = t;  // (not accounting for frame time here)
      mouse_drag.frameNStart = frameN;  // exact frame index
      
      mouse_drag.status = PsychoJS.Status.STARTED;
      mouse_drag.mouseClock.reset();
      prevButtonState = mouse_drag.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_drag.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_drag.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_drag.getPos();
          mouse_drag.x.push(_mouseXYs[0]);
          mouse_drag.y.push(_mouseXYs[1]);
          mouse_drag.leftButton.push(_mouseButtons[0]);
          mouse_drag.midButton.push(_mouseButtons[1]);
          mouse_drag.rightButton.push(_mouseButtons[2]);
          mouse_drag.time.push(mouse_drag.mouseClock.getTime());
        }
      }
    }
    // Run 'Each Frame' code from code
    let pieces = [item_1, item_2, item_3, item_4, item_5, item_6, item_7];
    for (var p, _pj_c = 0, _pj_a = util.range(pieces.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        p = _pj_a[_pj_c];
        let piece = pieces[p];
        if ((mouse_drag.isPressedIn(piece) && (movingPiece === 'undefined'))) {
            picked.push(piece);
        }
    }
    movingPiece = movePicked(picked, mouse_drag, movingPiece);
    
    
    // *item_1* updates
    if (t >= 0.0 && item_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_1.tStart = t;  // (not accounting for frame time here)
      item_1.frameNStart = frameN;  // exact frame index
      
      item_1.setAutoDraw(true);
    }

    
    // *item_2* updates
    if (t >= 0.0 && item_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_2.tStart = t;  // (not accounting for frame time here)
      item_2.frameNStart = frameN;  // exact frame index
      
      item_2.setAutoDraw(true);
    }

    
    // *item_3* updates
    if (t >= 0.0 && item_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_3.tStart = t;  // (not accounting for frame time here)
      item_3.frameNStart = frameN;  // exact frame index
      
      item_3.setAutoDraw(true);
    }

    
    // *item_4* updates
    if (t >= 0.0 && item_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_4.tStart = t;  // (not accounting for frame time here)
      item_4.frameNStart = frameN;  // exact frame index
      
      item_4.setAutoDraw(true);
    }

    
    // *item_5* updates
    if (t >= 0.0 && item_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_5.tStart = t;  // (not accounting for frame time here)
      item_5.frameNStart = frameN;  // exact frame index
      
      item_5.setAutoDraw(true);
    }

    
    // *item_6* updates
    if (t >= 0.0 && item_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_6.tStart = t;  // (not accounting for frame time here)
      item_6.frameNStart = frameN;  // exact frame index
      
      item_6.setAutoDraw(true);
    }

    
    // *item_7* updates
    if (t >= 0.0 && item_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_7.tStart = t;  // (not accounting for frame time here)
      item_7.frameNStart = frameN;  // exact frame index
      
      item_7.setAutoDraw(true);
    }

    
    // *ask_for_drag* updates
    if (t >= 0.0 && ask_for_drag.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ask_for_drag.tStart = t;  // (not accounting for frame time here)
      ask_for_drag.frameNStart = frameN;  // exact frame index
      
      ask_for_drag.setAutoDraw(true);
    }

    
    // *least_cnarcy* updates
    if (t >= 0.0 && least_cnarcy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      least_cnarcy.tStart = t;  // (not accounting for frame time here)
      least_cnarcy.frameNStart = frameN;  // exact frame index
      
      least_cnarcy.setAutoDraw(true);
    }

    
    // *most_cnarcy* updates
    if (t >= 0.0 && most_cnarcy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      most_cnarcy.tStart = t;  // (not accounting for frame time here)
      most_cnarcy.frameNStart = frameN;  // exact frame index
      
      most_cnarcy.setAutoDraw(true);
    }

    
    // *endBtn* updates
    if (t >= 0.0 && endBtn.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endBtn.tStart = t;  // (not accounting for frame time here)
      endBtn.frameNStart = frameN;  // exact frame index
      
      endBtn.setAutoDraw(true);
    }

    if (endBtn.status === PsychoJS.Status.STARTED) {
      // check whether endBtn has been pressed
      if (endBtn.isClicked) {
        if (!endBtn.wasClicked) {
          // store time of first click
          endBtn.timesOn.push(endBtn.clock.getTime());
          endBtn.numClicks += 1;
          // store time clicked until
          endBtn.timesOff.push(endBtn.clock.getTime());
        } else {
          // update time clicked until;
          endBtn.timesOff[endBtn.timesOff.length - 1] = endBtn.clock.getTime();
        }
        if (!endBtn.wasClicked) {
          // end routine when endBtn is clicked
          continueRoutine = false;
        }
        // if endBtn is still clicked next frame, it is not a new click
        endBtn.wasClicked = true;
      } else {
        // if endBtn is clicked next frame, it is a new click
        endBtn.wasClicked = false;
      }
    } else {
      // keep clock at 0 if endBtn hasn't started / has finished
      endBtn.clock.reset();
      // if endBtn is clicked next frame, it is a new click
      endBtn.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of dragComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function dragRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'drag' ---
    for (const thisComponent of dragComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_drag.x', mouse_drag.x);
    psychoJS.experiment.addData('mouse_drag.y', mouse_drag.y);
    psychoJS.experiment.addData('mouse_drag.leftButton', mouse_drag.leftButton);
    psychoJS.experiment.addData('mouse_drag.midButton', mouse_drag.midButton);
    psychoJS.experiment.addData('mouse_drag.rightButton', mouse_drag.rightButton);
    psychoJS.experiment.addData('mouse_drag.time', mouse_drag.time);
    
    // Run 'End Routine' code from code
    for (var p, _pj_c = 0, _pj_a = util.range(pieces.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        p = _pj_a[_pj_c];
        // psychoJS.experiment.addData(("final_loc_item_" + (p + 1).toString()), pieces[p].pos);
        psychoJS.experiment.addData(("final_loc_item_" + pieces[p].name), pieces[p].pos);
    }
    
    psychoJS.experiment.addData('endBtn.numClicks', endBtn.numClicks);
    psychoJS.experiment.addData('endBtn.timesOn', endBtn.timesOn);
    psychoJS.experiment.addData('endBtn.timesOff', endBtn.timesOff);
    // the Routine "drag" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function selectRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'select' ---
    t = 0;
    selectClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_select
    // current position of the mouse:
    mouse_select.x = [];
    mouse_select.y = [];
    mouse_select.leftButton = [];
    mouse_select.midButton = [];
    mouse_select.rightButton = [];
    mouse_select.time = [];
    mouse_select.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_2
    var pieces_1, x_coords, y_coords;
    pieces_1 = util.shuffle([item__1, item__2, item__3, item__4, item__5, item__6, item__7]);
    x_coords = [-0.15, 0.15, -0.3, 0, 0.3, -0.15, 0.15];
    y_coords = [0.12, 0.12, 0, 0, 0, -0.12, -0.12];
    
    for (let p = 0; p < x_coords.length; p++) {
        pieces_1[p].pos = [x_coords[p], y_coords[p]];
    }

    
    // x_coords = Array.from({ length: 11 }, (_, index) => -1 + index * (2 / 10));
    // for (var p, _pj_c = 0, _pj_a = util.range(pieces_1.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
    //     p = _pj_a[_pj_c];
    //     pieces_1[p].pos = [x_coords[(p + 2)], 0];
    // }
    
    // keep track of which components have finished
    selectComponents = [];
    selectComponents.push(mouse_select);
    selectComponents.push(item__1);
    selectComponents.push(item__2);
    selectComponents.push(item__3);
    selectComponents.push(item__4);
    selectComponents.push(item__5);
    selectComponents.push(item__6);
    selectComponents.push(item__7);
    selectComponents.push(ask_for_select);
    selectComponents.push(endBtn_2);
    
    for (const thisComponent of selectComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function selectRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'select' ---
    // get current time
    t = selectClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_select* updates
    if (t >= 0.5 && mouse_select.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_select.tStart = t;  // (not accounting for frame time here)
      mouse_select.frameNStart = frameN;  // exact frame index
      
      mouse_select.status = PsychoJS.Status.STARTED;
      mouse_select.mouseClock.reset();
      prevButtonState = mouse_select.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_select.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_select.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [item__1, item__2, item__3, item__4, item__5, item__6, item__7]) {
            if (obj.contains(mouse_select)) {
              gotValidClick = true;
              mouse_select.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_select.getPos();
          mouse_select.x.push(_mouseXYs[0]);
          mouse_select.y.push(_mouseXYs[1]);
          mouse_select.leftButton.push(_mouseButtons[0]);
          mouse_select.midButton.push(_mouseButtons[1]);
          mouse_select.rightButton.push(_mouseButtons[2]);
          mouse_select.time.push(mouse_select.mouseClock.getTime());
        }
      }
    }
    // Run 'Each Frame' code from code_2
    let pieces_1 = [item__1, item__2, item__3, item__4, item__5, item__6, item__7];
    for (var p, _pj_c = 0, _pj_a = util.range(pieces_1.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        p = _pj_a[_pj_c];
        let piece_1 = pieces_1[p];
        if (mouse_select.isPressedIn(piece_1)) {
            piece_1.opacity = 0.2;
        }
    }
    
    
    
    // *item__1* updates
    if (t >= 0.5 && item__1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item__1.tStart = t;  // (not accounting for frame time here)
      item__1.frameNStart = frameN;  // exact frame index
      
      item__1.setAutoDraw(true);
    }

    
    // *item__2* updates
    if (t >= 0.5 && item__2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item__2.tStart = t;  // (not accounting for frame time here)
      item__2.frameNStart = frameN;  // exact frame index
      
      item__2.setAutoDraw(true);
    }

    
    // *item__3* updates
    if (t >= 0.5 && item__3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item__3.tStart = t;  // (not accounting for frame time here)
      item__3.frameNStart = frameN;  // exact frame index
      
      item__3.setAutoDraw(true);
    }

    
    // *item__4* updates
    if (t >= 0.5 && item__4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item__4.tStart = t;  // (not accounting for frame time here)
      item__4.frameNStart = frameN;  // exact frame index
      
      item__4.setAutoDraw(true);
    }

    
    // *item__5* updates
    if (t >= 0.5 && item__5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item__5.tStart = t;  // (not accounting for frame time here)
      item__5.frameNStart = frameN;  // exact frame index
      
      item__5.setAutoDraw(true);
    }

    
    // *item__6* updates
    if (t >= 0.5 && item__6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item__6.tStart = t;  // (not accounting for frame time here)
      item__6.frameNStart = frameN;  // exact frame index
      
      item__6.setAutoDraw(true);
    }

    
    // *item__7* updates
    if (t >= 0.5 && item__7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item__7.tStart = t;  // (not accounting for frame time here)
      item__7.frameNStart = frameN;  // exact frame index
      
      item__7.setAutoDraw(true);
    }

    
    // *ask_for_select* updates
    if (t >= 0.5 && ask_for_select.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ask_for_select.tStart = t;  // (not accounting for frame time here)
      ask_for_select.frameNStart = frameN;  // exact frame index
      
      ask_for_select.setAutoDraw(true);
    }

    
    // *endBtn_2* updates
    if (t >= 0.5 && endBtn_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endBtn_2.tStart = t;  // (not accounting for frame time here)
      endBtn_2.frameNStart = frameN;  // exact frame index
      
      endBtn_2.setAutoDraw(true);
    }

    if (endBtn_2.status === PsychoJS.Status.STARTED) {
      // check whether endBtn_2 has been pressed
      if (endBtn_2.isClicked) {
        if (!endBtn_2.wasClicked) {
          // store time of first click
          endBtn_2.timesOn.push(endBtn_2.clock.getTime());
          endBtn_2.numClicks += 1;
          // store time clicked until
          endBtn_2.timesOff.push(endBtn_2.clock.getTime());
        } else {
          // update time clicked until;
          endBtn_2.timesOff[endBtn_2.timesOff.length - 1] = endBtn_2.clock.getTime();
        }
        if (!endBtn_2.wasClicked) {
          // end routine when endBtn_2 is clicked
          continueRoutine = false;
        }
        // if endBtn_2 is still clicked next frame, it is not a new click
        endBtn_2.wasClicked = true;
      } else {
        // if endBtn_2 is clicked next frame, it is a new click
        endBtn_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if endBtn_2 hasn't started / has finished
      endBtn_2.clock.reset();
      // if endBtn_2 is clicked next frame, it is a new click
      endBtn_2.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of selectComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function selectRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'select' ---
    for (const thisComponent of selectComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_select.x', mouse_select.x);
    psychoJS.experiment.addData('mouse_select.y', mouse_select.y);
    psychoJS.experiment.addData('mouse_select.leftButton', mouse_select.leftButton);
    psychoJS.experiment.addData('mouse_select.midButton', mouse_select.midButton);
    psychoJS.experiment.addData('mouse_select.rightButton', mouse_select.rightButton);
    psychoJS.experiment.addData('mouse_select.time', mouse_select.time);
    psychoJS.experiment.addData('mouse_select.clicked_name', mouse_select.clicked_name);
    
    // Run 'End Routine' code from code_2
    // psychoJS.experiment.saveAsWideText("drag_check");
    
    psychoJS.experiment.addData('endBtn_2.numClicks', endBtn_2.numClicks);
    psychoJS.experiment.addData('endBtn_2.timesOn', endBtn_2.timesOn);
    psychoJS.experiment.addData('endBtn_2.timesOff', endBtn_2.timesOff);
    // the Routine "select" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}



var gotValidClick;
var textBoxComponents;
function textBoxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'textBox' ---
    t = 0;
    textBoxClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textbox.setText('');
    textbox.refresh();
    textbox.setText('...');
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    textBoxComponents = [];
    textBoxComponents.push(textbox);
    textBoxComponents.push(ask_for_resp);
    textBoxComponents.push(endBtn_3);
    textBoxComponents.push(mouse);
    
    for (const thisComponent of textBoxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function textBoxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'textBox' ---
    // get current time
    t = textBoxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox* updates
    if (t >= 0.5 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }

    
    // *ask_for_resp* updates
    if (t >= 0.5 && ask_for_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ask_for_resp.tStart = t;  // (not accounting for frame time here)
      ask_for_resp.frameNStart = frameN;  // exact frame index
      
      ask_for_resp.setAutoDraw(true);
    }

    
    // *endBtn_3* updates
    if (t >= 0.5 && endBtn_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endBtn_3.tStart = t;  // (not accounting for frame time here)
      endBtn_3.frameNStart = frameN;  // exact frame index
      
      endBtn_3.setAutoDraw(true);
    }

    if (endBtn_3.status === PsychoJS.Status.STARTED) {
      // check whether endBtn_3 has been pressed
      if (endBtn_3.isClicked) {
        if (!endBtn_3.wasClicked) {
          // store time of first click
          endBtn_3.timesOn.push(endBtn_3.clock.getTime());
          endBtn_3.numClicks += 1;
          // store time clicked until
          endBtn_3.timesOff.push(endBtn_3.clock.getTime());
        } else {
          // update time clicked until;
          endBtn_3.timesOff[endBtn_3.timesOff.length - 1] = endBtn_3.clock.getTime();
        }
        if (!endBtn_3.wasClicked) {
          // end routine when endBtn_3 is clicked
          continueRoutine = false;
        }
        // if endBtn_3 is still clicked next frame, it is not a new click
        endBtn_3.wasClicked = true;
      } else {
        // if endBtn_3 is clicked next frame, it is a new click
        endBtn_3.wasClicked = false;
      }
    } else {
      // keep clock at 0 if endBtn_3 hasn't started / has finished
      endBtn_3.clock.reset();
      // if endBtn_3 is clicked next frame, it is a new click
      endBtn_3.wasClicked = false;
    }


    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of textBoxComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function textBoxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'textBox' ---
    for (const thisComponent of textBoxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textbox.text',textbox.text)
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    psychoJS.experiment.addData('endBtn_3.numClicks', endBtn_3.numClicks);
    psychoJS.experiment.addData('endBtn_3.timesOn', endBtn_3.timesOn);
    psychoJS.experiment.addData('endBtn_3.timesOff', endBtn_3.timesOff);
    
    // the Routine "textBox" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp2_allKeys;
var bonusComponents;
function bonusRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bonus' ---
    t = 0;
    bonusClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from bonusCode
    // Select a number of random trials from an array
    function getRandomSubarray(arr, size) {
        var shuffled = arr.slice(0), i = arr.length, temp, index;
        while (i--) {
            index = Math.floor((i + 1) * Math.random());
            temp = shuffled[index];
            shuffled[index] = shuffled[i];
            shuffled[i] = temp;
        }
        return shuffled.slice(0, size);
    }
    
    // Store 10 random trials in a variable and check their accuracy
    var sampled_accuracies = getRandomSubarray(bonus_accuracies, 10);
    var countBonuses = 0;
    for(var i = 0; i < sampled_accuracies.length; ++i){
        if(sampled_accuracies[i] == 1)
            countBonuses++;
    }
    
    // Update messages depending on number of accurate responses
    if (countBonuses > 5) {
        msgBonus = "Ten random responses from the main task were selected. \nCONGRATULATIONS! More than half of your responses were correct. \nYou will receive the BONUS! \n[Press space to continue]";
        get_bonus = 1;
        psychoJS.experiment.addData("Bonus", get_bonus);
    } else {
        msgBonus = "Sorry! Unfortunately, at least half of the ten randomly picked responses from the main task were not correct. \nYou cannot not receive the bonus \n[Press space to continue]";
        get_bonus = 0;
        psychoJS.experiment.addData("Bonus", get_bonus);
    }
    
    key_resp2.keys = undefined;
    key_resp2.rt = undefined;
    _key_resp2_allKeys = [];
    presentBonus.setText(msgBonus);
    // keep track of which components have finished
    bonusComponents = [];
    bonusComponents.push(key_resp2);
    bonusComponents.push(presentBonus);
    
    for (const thisComponent of bonusComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function bonusRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bonus' ---
    // get current time
    t = bonusClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp2* updates
    if (t >= 0.0 && key_resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp2.tStart = t;  // (not accounting for frame time here)
      key_resp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp2.clearEvents(); });
    }

    if (key_resp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp2_allKeys = _key_resp2_allKeys.concat(theseKeys);
      if (_key_resp2_allKeys.length > 0) {
        key_resp2.keys = _key_resp2_allKeys[_key_resp2_allKeys.length - 1].name;  // just the last key pressed
        key_resp2.rt = _key_resp2_allKeys[_key_resp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *presentBonus* updates
    if (t >= 0 && presentBonus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentBonus.tStart = t;  // (not accounting for frame time here)
      presentBonus.frameNStart = frameN;  // exact frame index
      
      presentBonus.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of bonusComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function bonusRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bonus' ---
    for (const thisComponent of bonusComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp2.stop();
    // the Routine "bonus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}




var _key_respEnd_allKeys;
var finishExperimentComponents;
function finishExperimentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'finishExperiment' ---
    t = 0;
    finishExperimentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_respEnd.keys = undefined;
    key_respEnd.rt = undefined;
    _key_respEnd_allKeys = [];
    // keep track of which components have finished
    finishExperimentComponents = [];
    finishExperimentComponents.push(finalText);
    finishExperimentComponents.push(key_respEnd);
    
    for (const thisComponent of finishExperimentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function finishExperimentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'finishExperiment' ---
    // get current time
    t = finishExperimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *finalText* updates
    if (t >= 0.0 && finalText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      finalText.tStart = t;  // (not accounting for frame time here)
      finalText.frameNStart = frameN;  // exact frame index
      
      finalText.setAutoDraw(true);
    }

    
    // *key_respEnd* updates
    if (t >= 0.0 && key_respEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respEnd.tStart = t;  // (not accounting for frame time here)
      key_respEnd.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respEnd.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respEnd.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respEnd.clearEvents(); });
    }

    if (key_respEnd.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respEnd.getKeys({keyList: ['space', 'Escape'], waitRelease: false});
      _key_respEnd_allKeys = _key_respEnd_allKeys.concat(theseKeys);
      if (_key_respEnd_allKeys.length > 0) {
        key_respEnd.keys = _key_respEnd_allKeys[_key_respEnd_allKeys.length - 1].name;  // just the last key pressed
        key_respEnd.rt = _key_respEnd_allKeys[_key_respEnd_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of finishExperimentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function finishExperimentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'finishExperiment' ---
    for (const thisComponent of finishExperimentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_respEnd.stop();
    // the Routine "finishExperiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  await postData("../submit", psychoJS.experiment._trialsData)
  // Make sure, the HTTP-Request succeeded (200 response code)
  // See: https://developer.mozilla.org/en-US/docs/Web/API/Response
  .then(r => {
      switch (r.ok) {
          case true: return r
          case false: throw new Error(`${r.status} ${r.statusText}`)
      }
  })
  // Parse the response body as JSON
  .then(r => r.json())
  // Check, whether the Lou-Server accepted the data
  // See: https://arc-git.mpib-berlin.mpg.de/arc-support/public-projects/lou-server#post-submit
  .then(r => {
      switch (r.code) {
          case 0: return r
          default: throw new Error(`${r.code} ${r.message}`)
      }
  })
  // Display an alert, if any error occurred along the .then-chain:
  .catch(e => { alert(e.message) })
  
  // prevent auto download of data 
  psychoJS._serverMsg.set('__noOutput', true);
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

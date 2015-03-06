#!/bin/bash

folder=~/Documents/research/abstraction-extensive-form-games/imperfect_recall_with_bounds/data/correlatedDrp/
inputFolder=${folder}
outputFolder=~/Dropbox/christian-tuomas-shared/imperfect_recall_abstraction/figures

sn=s4e
en=r4i4.txt

python ~/github/Plotting/plotParameterized.py ${inputFolder}/${sn}0${en}  '' 'iterations' 'regret' ${outputFolder}/smallError.pdf 1 ${inputFolder}/${sn}0${en} 7 '0' ${inputFolder}/${sn}01${en} 7 '0.01' ${inputFolder}/${sn}02${en} 7 '0.02' ${inputFolder}/${sn}03${en} 7 '0.03'


python ~/github/Plotting/plotParameterized.py ${inputFolder}/${sn}0${en}  '' 'iterations' 'regret' ${outputFolder}/bigError.pdf 1 ${inputFolder}/${sn}04${en} 7 '0.04' ${inputFolder}/${sn}05${en} 7 '0.05' ${inputFolder}/${sn}06${en} 7 '0.06' ${inputFolder}/${sn}07${en} 7 '0.07'



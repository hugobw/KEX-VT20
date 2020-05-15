set datafile separator ',' # tells gnuplot comma is used to seperate data

set title "DWM n_estimators" noenhanced

set key autotitle columnhead noenhanced # use first line as legend keys
set key right bottom # legend placement

set ylabel "Accuracy"
set xlabel "Batches"

plot 'DWM_n_estimators_mod.csv' using 1:2 with lines, '' using 1:3 with lines, '' using 1:4 with lines, '' using 1:5 with lines, '' using 1:6 with lines

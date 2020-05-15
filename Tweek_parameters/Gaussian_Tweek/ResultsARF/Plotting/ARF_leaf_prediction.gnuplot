set datafile separator ',' # tells gnuplot comma is used to seperate data

set title "ARF leaf_prediction" noenhanced

set key autotitle columnhead noenhanced # use first line as legend keys
set key right bottom # legend placement

set ylabel "Accuracy"
set xlabel "Batches"

plot 'ARF_leaf_prediction_mod.csv' using 1:2 with lines, '' using 1:3 with lines, '' using 1:4 with lines

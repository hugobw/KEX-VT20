set datafile separator ',' # tells gnuplot comma is used to seperate data

set title "Average accuracy over 20 tests (Gaussian)" noenhanced

set key autotitle columnhead noenhanced # use first line as legend keys
set key right bottom # legend placement

set ylabel "Accuracy"
set xlabel "Batch"

plot 'avg_results.csv' using 1:2 with lines, '' using 1:3 with lines, '' using 1:4 with lines, '' using 1:5 with lines

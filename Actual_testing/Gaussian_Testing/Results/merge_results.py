# Script for modifying results from actual testing to contain
# a column for each algorithm and their average accuracy per batch
# Command line argument 1 to n: File to write to (modified .csv)

import csv
import sys

# Initialize arrays
ARF_avg = []
NB_avg = []
DWM_avg = []
KNNA_avg = []

# Open all necessary files and calculate average
sum = 0
with open('ARF.csv') as ARF:
    ARF_res = csv.reader(ARF)
    for data in ARF_res:
        for i in data:
            sum = sum + float(i)
        avg = sum/20                # in total, 20 tests were done
        ARF_avg.append(avg)
        sum = 0

sum = 0
with open('Bayes.csv') as NB:
    NB_res = csv.reader(NB)
    for data in NB_res:
        for i in data:
            sum = sum + float(i)
        avg = sum/20
        NB_avg.append(avg)
        sum = 0

sum = 0
with open('DWM.csv') as DWM:
    DWM_res = csv.reader(DWM)
    for data in DWM_res:
        for i in data:
            sum = sum + float(i)
        avg = sum/20
        DWM_avg.append(avg)
        sum = 0

sum = 0
with open('KNNA.csv') as KNNA:
    KNNA_res = csv.reader(KNNA)
    for data in KNNA_res:
        for i in data:
            sum = sum + float(i)
        avg = sum/20
        KNNA_avg.append(avg)
        sum = 0

output_file = open(sys.argv[1], mode='w')
output = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

batch = 1
for i in range(1,302):
    output.writerow([batch,
                     round(ARF_avg[i],6),
                     round(NB_avg[i],6),
                     round(DWM_avg[i],6),
                     round(KNNA_avg[i],6)
                    ])
    batch += 1

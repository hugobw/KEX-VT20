# Script for modifying results to contain an extra column for x-data
# Command line argument 1: File to open (.csv)
# Command line argument 2: File to write to (modified .csv)

import csv
import sys

input_file = open(sys.argv[1])
output_file = open(sys.argv[2], mode='w')

input = csv.reader(input_file, delimiter=',')
output = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

batch = 1
row = ''
for data in input:
    output.writerow([batch, data[0], data[1], data[2], data[3], data[4], data[5]])

    batch += 1

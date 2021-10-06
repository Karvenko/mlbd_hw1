#!/usr/bin/python3
import sys
import csv

mean = 0
count = 0
cur_val = 0
reader = csv.reader(sys.stdin, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
for line in reader:
    try:
        cur_val = float(line[9])
        mean += cur_val
        count += 1
    except:
        continue
mean /= count
output = str(mean) + '\t' + str(count) + '\n'
sys.stdout.write(output)

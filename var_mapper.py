#!/usr/bin/python3
import sys
import csv

mean = 0
mean_sq = 0
count = 0
cur_val = 0
reader = csv.reader(sys.stdin, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
for line in reader:
    try:
        cur_val = float(line[9])
        mean += cur_val
        mean_sq += cur_val ** 2
        count += 1
    except:
        continue
mean /= count
mean_sq = mean_sq / count - mean ** 2
output = str(mean) + '\t' + str(mean_sq) + '\t' + str(count) + '\n'
sys.stdout.write(output)

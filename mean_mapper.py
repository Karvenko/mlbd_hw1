#!/usr/bin/python3
import sys

mean = 0
count = 0
cur_val = 0
for line in sys.stdin:
    line = line.strip().split(',')
    try:
        cur_val = float(line[9])
        mean += cur_val
        count += 1
    except:
        continue
mean /= count
output = str(mean) + '\t' + str(count) + '\n'
sys.stdout.write(output)

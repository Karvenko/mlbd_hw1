#!/usr/bin/python3
import sys

total_mean = 0
total_var = 0
total_count = 0

for line in sys.stdin:
    mean, var, count = map(float, line.strip().split())
    total_var = (var * count + total_var * total_count) / (count + total_count) + \
        count * total_count * ((mean - total_mean) / (count + total_count)) ** 2
    total_mean = (mean * count + total_mean * total_count) / (count + total_count)
    total_count += count
output = str(total_mean) + '\t' + str(total_var) + '\n'
sys.stdout.write(output)

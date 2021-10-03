#!/usr/bin/python3
import sys

total_mean = 0
total_count = 0

for line in sys.stdin:
    mean, count = map(float, line.strip().split())
    total_mean = (mean * count + total_mean * total_count) / (count + total_count)
    total_count += count
output = str(total_mean) + '\n'
sys.stdout.write(output)

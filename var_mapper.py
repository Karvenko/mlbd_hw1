#!/usr/bin/python3
import sys

mean = 0
mean_sq = 0
count = 0
cur_val = 0
for line in sys.stdin:
    line = line.strip().split(',')
    # print(line[9])
    try:
        cur_val = float(line[9])
        # print(cur_val)
        mean += cur_val
        mean_sq += cur_val ** 2
        count += 1
    except:
        continue
    # print(cur_val)
mean /= count
mean_sq = mean_sq / count - mean ** 2
# sys.stdout.write(f'{mean}\t{mean_sq}{count}\t{count}\n')
output = str(mean) + '\t' + str(mean_sq) + '\t' + str(count) + '\n'
# sys.stdout.write(mean, '\t', mean_sq, '\t', count, '\n')
sys.stdout.write(output)

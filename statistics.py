# TODO: This file calculates some statistics about the result. Please change the path or other information if needed.

import numpy as np


def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]


seq_len = "192-12000"

path = "./results/" + str(seq_len) + "/running_time.txt"

times = []
with open(path, 'r') as _file:
    count = 0
    for line in _file.readlines():
        count += 1
        r = count % 2
        if r == 1:
            continue
        else:
            time = line[-12:-5]
            times.append(float(time))

print("Seq len: " + str(seq_len))

# get mean
print('Mean: ' + str(sum(times) / len(times)))

# get median
print('Median: ' + str(times[int(len(times) / 2)]))

new_times = reject_outliers(np.array(times))
print('Reject outliers mean: ' + str(sum(new_times) / len(new_times)))

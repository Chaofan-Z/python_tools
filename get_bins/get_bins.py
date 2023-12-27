import sys
cvr = []
with open("./cvr") as file:
  for line in file:
    line = float(line.strip())
    cvr.append(line)

cvr.sort()

num_bins = 10

step = len(cvr) // num_bins

bins = []
for i in range(0, len(cvr), step):
  bins.append(cvr[i])

print(bins)

# [3.34e-06, 0.00015237, 0.00028603, 0.00049881, 0.0008232, 0.00130619, 0.00206999, 0.00328358, 0.00581948, 0.01346539, 0.24338245]

# [0, 0.00015237, 0.00028603, 0.00049881, 0.0008232, 0.00130619, 0.00206999, 0.00328358, 0.00581948, 0.01346539, 1]
import pickle
import statistics
import matplotlib.pyplot as plt
import numpy as np

with open ('list2.txt', 'rb') as fp:
    losses = pickle.load(fp)

print(losses)
avg = statistics.mean(losses)
print(avg)
print(max(losses))
print(len(losses))
j = 0
for i in losses:
    if i > 20:
        j += 1
print(j)

with open('results.txt', 'w') as f:
    for item in losses:
        f.write("%s\n" % item)

np.random.seed(42)
x = np.random.normal(size=1000)
plt.hist(losses, density=False, bins=20)  # `density=False` would make counts
plt.ylabel('Frequency')
plt.xlabel('Max Fails');
plt.show()

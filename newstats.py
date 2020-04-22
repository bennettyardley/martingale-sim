import pickle
import statistics
import matplotlib.pyplot as plt
import numpy as np

with open ('all123.txt', 'rb') as fp:
    arr = pickle.load(fp)

print("Loss\tPercent\tProfit")
for x, y, z in arr:
    print(str(x) + "\t" + str(round(y,2)) + "\t" + str(z))

import pickle
with open ('profit.txt', 'rb') as fp:
    profits = pickle.load(fp)
with open ('fail.txt', 'rb') as fp:
    fails = pickle.load(fp)

for profit in profits:
    print(profit)
for fail in fails:
    print(fail)

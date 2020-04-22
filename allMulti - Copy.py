import random
import statistics
import pickle
from multiprocessing import Pool

def roll():
    dice = random.randint(1,1000)
    if dice <= 505:
        return False
    elif dice > 505:
        return True

def results():
    balance = 100000
    runs = 1000000
    looper = 10000
    losses = 36
    initial = balance / 2 ** (losses + 1)
    initial = round(initial,8)
    fails = []
    bal = balance
    last = True
    bet = initial
    for j in range(runs):
        result = roll()
        if result and last:
            bal += bet
            last = True
            bet = initial
        elif result and not last:
            bal += bet
            last = True
            bet = initial
        elif not result and last:
            bal -= bet
            if bal < bet:
                fails.append(1)
                break
            last = False
            bet = bet * 2
        elif not result and not last:
            bal -= bet
            if bal < bet:
                fails.append(1)
                break
            last = False
            bet = bet * 2

    return losses, failer, profiter

if __name__ == '__main__':
    with Pool() as pool:
        x = pool.map(results, range(20))
        print(x)
        with open('all.txt', 'wb') as fp:
            pickle.dump(x, fp)

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

def results(losser):
    balance = 54644
    losses = 10
    runs = 259200
    looper = 10000
    losses += losser
    initial = balance / 2 ** (losses + 1)
    initial = round(initial,8)
    profit = []
    fails = []
    wins = []
    for i in range(looper):
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
        profit.append(bal-balance)
    for win in profit:
        if win > 0:
            wins.append(win)
    if not wins:
        wins.append(0)
    failer = ((len(fails)/looper)*100)
    profiter = (float(statistics.mean(wins))*0.002038)
    return losses, failer, profiter

if __name__ == '__main__':
    with Pool() as pool:
        x = pool.map(results, range(20))
        print(x)
        with open('all.txt', 'wb') as fp:
            pickle.dump(x, fp)

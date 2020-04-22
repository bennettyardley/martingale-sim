import random
import statistics
import pickle

################################################################################
#Your starting balance (in doge)
balance = 54644
#The amount of successive fails you want to withstand (ex. losses=5 means you bust on the 6th)
#losses = 20
losses = 10
#The amount of rolls you want to simulate
runs = 259200
#The amount of players you want to simulate
looper = 100
################################################################################

def roll():
    dice = random.randint(1,1000)
    if dice <= 505:
        return False
    elif dice > 505:
        return True

profits = []
fail = []

for k in range(20):
    print("Losses: " + str(losses))
    initial = balance / 2 ** (losses + 1)
    initial = round(initial,8)
    print("Initial: $" + str(round(initial*0.002038,8)))
    profit = []
    fails = []
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
    wins = []
    for win in profit:
        if win > 0:
            wins.append(win)
    if not wins:
        wins.append(0)
    print("$"+str(round(float(statistics.mean(wins))*0.002038,2)))
    profits.append(float(statistics.mean(wins))*0.002038)
    print("Failed " + str(len(fails)) + " times (" + str((len(fails)/looper)*100) + "%)\n\n")
    fail.append((len(fails)/looper)*100)
    losses += 1

with open('profit2.txt', 'wb') as fp:
    pickle.dump(profits, fp)
with open('fail2.txt', 'wb') as fp:
    pickle.dump(fail, fp)

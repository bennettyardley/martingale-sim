import random
import time
import os

def roll():
    dice = random.randint(1,1000)
    if dice <= 505:
        return False
    elif dice > 505:
        return True

initial = 0.0032742
balance = 27466
bal = balance
last = True
bet = initial
runs = 259200

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
            print("OUT")
            break
        last = False
        bet = bet * 2
    elif not result and not last:
        bal -= bet
        if bal < bet:
            print("OUT")
            break
        last = False
        bet = bet * 2
#    print(bal)
print('PROFIT: ' + str(bal-balance))

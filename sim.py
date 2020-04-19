import random
import time
import os

def roll():
    dice = random.randint(1,1000)
    if dice <= 505:
        return False
    elif dice > 505:
        return True

initial = 0.000058000 #1 cents
bal = 1.16 #215 dollars
last = True
bet = initial
max_bet = 0
max_loss = 0
loss_count = 0
runs = 1000000
multiplier = 1000
losses = []

for i in range(multiplier):
    for j in range(runs):
        result = roll()
        if result and last:
            loss_count = 0
            bal += bet
        elif result and not last:
            loss_count = 0
            bal += bet
            last = True
            bet = initial
        elif not result and last:
            bal -= bet
            last = False
            bet = bet * 2
            if bet > max_bet:
                max_bet = bet
            loss_count += 1
            if loss_count > max_loss:
                max_loss = loss_count
        elif not result and not last:
            bal -= bet
            last = False
            bet = bet * 2
            if bet > max_bet:
                max_bet = bet
            loss_count += 1
            if loss_count > max_loss:
                max_loss = loss_count
    losses.append(max_loss)
    os.system('cls')
    print(str(i+1) + "/" + str(multiplier))
    print(max_loss)
print(max_bet)
print(max_loss)
print(losses)
print(avg(losses))

'''
start = float(input("USD: $"))
start = start * 0.0058
x = start

total = 0
win = .495
lose = .505

print("\n" + str(start) + "\n")

print("BET\t\tLOSS\t\tCHANCE")

print(str(start) + "\t\t" + str(1) + "\t\t50.5%")
for i in range(16):
    x = x * 2
    ud = x * 171.40
    total = total + x
    chance = .505 ** (i+2)
    percent = chance * 100
    print(str(round(ud,3)) + "\t\t" + str(i+2) + "\t\t" + str(round(percent,4)) + "%")

usd = total * 171.40
print("\n\nTotal: $" + str(usd) + "\n\nTotal: ETH" + str(total))

import random


def roll():
    dice = random.randint(1,1000)
    if dice <= 505:
        return False
    elif dice > 505:
        return True

bal = 80
firstBet = 0.00058000
bet = firstBet

previousWagerAmount = firstBet
previousWager = 'win'

wager_count = 10000
currentWager = 1

while currentWager <= wager_count:
    if previousWager == 'win':
        if roll():
            bal += bet
        else:
            bal -= bet
            previousWager = 'loss'
            previousWagerAmount = bet
            if bal < 0:
                print("LOSS")
    elif previousWager == 'loss':
        if roll():
            bet = previousWagerAmount * 2
            bal += bet
            bet = firstBet
            previousWager = 'win'
        else:
            bet = previousWagerAmount * 2
            bal -= bet
            if bal < 0:
                print("LOSS")
            previousWager = 'loss'
            previousWagerAmount = bet
            if bal < 0:
                print("LOSS")
    currentWager += 1

print(bal)
'''
check = 0.00000071
check = 0.025598871353022815 #49.5
check = 0.04790433229852053 #51
check = 157.6878280774863 #75
balance = 53684.7242557345
sum = 0
losses = 20.0

for i in range(20):
    check = check * 2
    print(check)
    sum += check

print(sum)

x = balance / 1.3200 ** (losses + 1)
print(x)

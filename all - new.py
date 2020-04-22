import random
import statistics
import pickle
import time

################################################################################
balance = 100000
runs = 1000000
looper = 10000
losses = 36
################################################################################

def roll():
    dice = random.randint(1,1000)
    if dice <= 505:
        return False
    elif dice > 505:
        return True

profits = []
fail = []

initial = balance / 2 ** (losses + 1)
initial = round(initial,8)
maxes = []
for i in range(looper):
    bal = balance
    last = True
    bet = initial
    print(i+1)
    max = []
    for j in range(runs):
        result = roll()
        if result and last:
            bal += bet
            last = True
            bet = initial
            max.append("Win")
        elif result and not last:
            bal += bet
            last = True
            bet = initial
            max.append("Win")
        elif not result and last:
            bal -= bet
            last = False
            bet = bet * 2
            max.append("Loss")
        elif not result and not last:
            bal -= bet
            last = False
            bet = bet * 2
            max.append("Loss")
    maxes.append(max)

def streakcounter(results):
    streak = []
    prevelem = results[0]
    counter = 1
    for i in range(1, len(results)):
        if results[i] == prevelem:
            counter += 1
        else:
            streak.append(counter)
            counter = 1
        prevelem = results[i]
        print(streak)
        time.sleep(1)
    time.sleep(1)
    return streak

def make_streak(S1):
    ''' This function takes the values of Win/Loss column as input and returns a list of streak values
    eg: input list : ['Loss', 'Win', 'Win', 'Win', 'Loss', 'Loss']
    output list : ['L1', 'W1', 'W2', 'W3', 'L1', 'L2'] '''
    S2 = []
    for i in range(len(S1)):
        if i==0:
            S2.append(S1[i][0]+'1');continue
        if S1[i] != S1[i-1]:
            S2.append(S1[i][0]+'1')
        if S1[i] == S1[i-1]:
            S2.append(S1[i][0]+str(int(S2[-1][-1])+1))
    return S2

maxy = []
for maxer in maxes:
    maxy.append(make_streak(maxer))

maxxer = []
for maxys in maxy:
    for maxx in maxys:
        if "L" in maxx:
            maxxer.append(maxx[1])

def get_streak(results):
    streak = []
    prevelem = results[0]
    counter = 1
    for i in range(1, len(results)):
        if results[i] >= prevelem:
            counter += 1
        else:
            streak.append(counter)
            counter = 1
        prevelem = results[i]
    return streak


streaksbby = []
streaksbby = get_streak(maxxer)
with open("streaks.txt", "w") as txt_file:
    for line in streaksbby:
        txt_file.write(str(line) + "\n")

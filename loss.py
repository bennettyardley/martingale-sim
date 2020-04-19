import random
import pickle


def roll():
    dice = random.randint(1,1000)
    if dice <= 505:
        return False
    elif dice > 505:
        return True

runs = 1000000
multiplier = 1000
losses = []

for i in range(multiplier):
    max_loss = 0
    loss_count = 0
    last = True
    for j in range(runs):
        result = roll()
        if result and last:
            loss_count = 0
            last = True
        elif result and not last:
            loss_count = 0
            last = True
        elif not result and last:
            last = False
            loss_count += 1
            if loss_count > max_loss:
                max_loss = loss_count
        elif not result and not last:
            last = False
            loss_count += 1
            if loss_count > max_loss:
                max_loss = loss_count
    losses.append(max_loss)
    print(str(i+1) + "/" + str(multiplier))

print(losses)
with open('list.txt', 'wb') as fp:
    pickle.dump(losses, fp)

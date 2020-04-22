#starting balance
balance110 = 54000.98183603338
balance200 = 98183.60333824251
balance500 = 245459.00834560627
balance = 100

#how many losses you want to be able to withstand
losses = 23
losses -= 1


#calculate the initial bet amount
initial = balance / 2 ** (losses + 1)
initial = round(initial,8)
print("\nINITIAL BET: " + str(initial))
print("\nLOSS\tBET")
print("1\t"+str(initial))

sum = 0
for i in range(int(losses)):
    initial = initial * 2
    initial = round(initial,8)
    print(str(i+2)+"\t"+str(initial))
    sum += initial

print("\nSum of losses: " + str(sum) + "\tBalance left: " + str(balance-sum))

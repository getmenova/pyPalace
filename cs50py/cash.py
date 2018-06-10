import cs50
while True:
    print("Enter Ch-Ch-Ch-Change: ", end="")
    dollars = cs50.get_float()
    if dollars >= 0.0:
        break

#make dollars cents
cents = round(dollars * 100)

#init counter
coins = 0

#elephant eats quarters
while cents >= 25:

 #push counter by 1 per coin
    coins += 1

    # reconcile change amnt
    cents -= 25

#elephant eats all remaining dimes
while cents >= 10:
    coins += 1
    cents -= 10

#eats remaining nickels
while cents >= 5:
    coins += 1
    cents -= 5

#pennies for dessert
while cents >= 1:
    coins += 1
    cents -= 1

# print coin number
print(coins)



#FYI - Familiarization with coins / counting required. Quarter = 25c .25 Dollar, Dime = 10c .1 Dollar, Penny = 1c .01 Dollar
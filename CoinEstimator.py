__author__ = 'stefan'

"""===================================================================================================

When some people receive change after shopping, they put it into a container and let it add up over time.
Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank
for what they are worth. While most banks will give away coin wrappers for free,
it's convenient to have an idea of how many you will need. Instead of counting how many coins you have,
it's easier to separate all of your coins, weigh them, and then estimate how many of each type you have and then
how many wrappers you'll need.

For example, if you weigh all of your dimes and see that you have 1276.9g of them,
you can estimate that you have about 563 dimes (since each one is 2.268g)
and you would be able to fill 11 dime wrappers.

Goal
 Create a program that allows the user to input the total weight of each type of coin they have
 (pennies, nickels, dimes, and quarters),
 and then print out how many of each type of wrapper they would need,
 how many coins they have, and the estimated total value of all of their money.

Weight of each coin and how many fit inside each type of wrapper.

Subgoals

    Round all numbers printed out to the nearest whole number.

    Allow the user to select whether they want to submit the weight in either grams or pounds.
================================================================================================================"""

print "This is a coin estimator"

def wahl():
    wahl=raw_input("weight in g or lbs: ")
    return wahl
wgt_coins=[2.5,5.,2.268,5.67]
worth_coins=[0.01,0.05,0.1,0.25]
wrapper_list=[50,40,50,40]
choice=wahl()

wgt_pennies=raw_input("weight of pennies: ")
wgt_nickels=raw_input("weight of nickels: ")
wgt_dimes=raw_input("weight of dimes: ")
wgt_quarters=raw_input("weight of quarters: ")

if choice=="g":
    amount_pennies=int(float(wgt_pennies)//wgt_coins[0])
    amount_nickels=int(float(wgt_nickels)//wgt_coins[1])
    amount_dimes=int(float(wgt_dimes)//wgt_coins[2])
    amount_quarters=int(float(wgt_quarters)//wgt_coins[3])
    money_pen=amount_pennies*worth_coins[0]
    money_nic=amount_nickels*worth_coins[1]
    money_dime=amount_dimes*worth_coins[2]
    money_qua=amount_quarters*worth_coins[3]
    money=money_pen+money_nic+money_dime+money_qua

    print "\npennies: "+str(amount_pennies)+"\nnickels: "+str(amount_nickels)+"\ndimes: "+str(amount_dimes)+"\nquarters: "+str(amount_quarters)+"\ntotal amount of money: "+str(money)
elif choice=="lbs":
    wgt_pennies*=453.592
    wgt_nickels*=453.592
    wgt_dimes*=453.592
    wgt_quarters*=453.592
    amount_pennies=int(float(wgt_pennies)//wgt_coins[0])
    amount_nickels=int(float(wgt_nickels)//wgt_coins[1])
    amount_dimes=int(float(wgt_dimes)//wgt_coins[2])
    amount_quarters=int(float(wgt_quarters)//wgt_coins[3])
    money_pen=amount_pennies*worth_coins[0]
    money_nic=amount_nickels*worth_coins[1]
    money_dime=amount_dimes*worth_coins[2]
    money_qua=amount_quarters*worth_coins[3]
    money=money_pen+money_nic+money_dime+money_qua
    print "\npennies: "+str(amount_pennies)+"\nnickels: "+str(amount_nickels)+"\ndimes: "+str(amount_dimes)+"\nquarters: "+str(amount_quarters)+"\ntotal amount of money: "+str(money)
else:
    print "Wrong Choice for weight unit"


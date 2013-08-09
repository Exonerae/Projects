cost = float(raw_input("Please input the cost: $")) * 100
payment = float(raw_input("Please input the payment: $")) * 100
print "Calculating change...\n"

change  = payment - cost

changepaid = float(change) / 100

dollars = int(change / 100)
change = change % 100
quarters = int(change / 25)
change = change % 25
dimes = int(change / 10)
change = change % 10
nickels = int(change  / 5)
change = change % 5
pennies = int(change / 1)

print "dollars: %d\nquarters: %d\ndimes: %d\nnickels: %d\npennies: %d\n" % \
    (dollars,quarters, dimes, nickels, pennies)
print "Total Change: $%.2f\n" % changepaid

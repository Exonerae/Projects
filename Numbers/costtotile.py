width = input("What is the width of the floor? (ft) ")
length = input("What is the length of the floor? (ft) ")
costperfoot = input("What is the cost per sq. ft? $")

totalcost = costperfoot * width * length
print "The cost to tile your floor is $%.2f" % totalcost

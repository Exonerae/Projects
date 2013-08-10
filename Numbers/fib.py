number = input("Up to which number in the fibonacci sequence would you like? ")
fibonacci = [0,1]
index = 0
print "START"
while index < number:
    print "#%d: %d" % (index+1, fibonacci[index])
    fibonacci.append(fibonacci[index]+fibonacci[index+1])
    index +=1
print "END"

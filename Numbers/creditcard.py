number = raw_input("Please enter a Visa number for validation: ")
number = list(number)[::-1]
sum = 0
count = 0

for i in range(0,len(number)):
    if count % 2 == 1:
        temp = int(number[i])*2
        templist = [int(x) for x in str(temp)]
        for x in range(0,len(templist)):
            sum += templist[x]
        count += 1
    else:
            sum += int(number[i])
            count += 1

if sum % 10 == 0:
    print "Credit card number is valid"
else:
    print "Credit card number is NOT valid"

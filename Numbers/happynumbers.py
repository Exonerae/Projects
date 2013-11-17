def isHappy(num):
	past = set()
	while True:
		total = sum(int(i)**2 for i in str(num))
		if total == 1:
			return 'a happy number!'
		if total in past:
			return 'an unhappy number.'
		num = total
		past.add(total)
number = raw_input("Please enter a number: ")
print "%s is %s" % (number, isHappy(number))

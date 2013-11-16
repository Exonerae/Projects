vowels = ['a','e','i','o','u','y']
def count_vowels(string):
	count = 0
	for letter in string:
		if letter in vowels:
			count += 1
	if count == 1:
		print "There is 1 vowel."
	else:
		print "There are %i vowels." % count


text = raw_input("Enter text: ")
count_vowels(text)

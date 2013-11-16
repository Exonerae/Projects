import string

def palindrome(text):
	userinput = text
	text = text.translate(string.maketrans(string.uppercase,string.lowercase), string.punctuation) # removes all punctuation
	text = ''.join(text.split()) # removes whitespace
	
	if (text == text[::-1]):
		print "'%s' is a palindrome!" % userinput
	else:
		print "'%s' is not a palindrome." % userinput


text = raw_input("Enter the text you want to check: ")
palindrome(text)

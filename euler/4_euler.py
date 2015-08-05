#  palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(number):
	str_number = str(number)
	if str_number == str_number[::-1]:
		return True
	else:
		return False 

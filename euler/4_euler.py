#  palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(number): 
	str_number = str(number)
	if str_number == str_number[::-1]:
		return True
	else:
		return False 
palindromics = []
i = 100
while 100 <= i and i <= 999:
	r = 100
	while 100 <= r and r <= 999:
		n_n = r * i
		r += 1
		if is_palindromic(n_n):
			print ("{} times {} = {}".format(i, r, n_n))
			palindromics.append(n_n)
	i +=1
print(max(palindromics))
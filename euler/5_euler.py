# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# This function actually checks if the number is divisible by all numbers form "1-10" (will elevate that shortly)
def is_devisible(number):
	flag = 0 # default for not devised
	for i in range(1, 11):
		if number % i == 0 :
			flag = 1
		else:
			flag = 0
			break
	if flag == 0:
		return False
	else:
		return True


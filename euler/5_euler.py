'''The Question HEAD'''
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''Coding HEAD'''
# This function actually checks if the number is divisible by all numbers form "1-10" (will elevate that shortly)
def is_devisible(number):
	flag = 0 # default for not devised
	for i in range(1, 21):
		if number % i == 0 :
			flag = 1
		else:
			flag = 0
			break
	if flag == 0:
		return False # The number is not devisible by every number from 1-10
	else:
		return True # The number is devisible by every number from 1-10
for i in range(100000000, 1000000000 ): #Set your desirewd range here!
	if is_devisible(i):
		print (i)
		break
	else:
		pass
print("Increase range!")

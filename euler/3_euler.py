# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#Let's write something that says if a number is prime or not 
def is_prime(number):
	i = 2
	flag = 0 #default for prime
	while i < number:
		if number%i == 0:
			flag = 1
			break
		i +=1
	if flag == 0:
		return True
	else: 
		return False
#This will find out a numbers factors
def factor (number):
	factor = 2
	factors = []
	while factor< (number/2):
		if number%factor == 0:
			factors.append(factor)
		else: 
			pass
		factor += 1
	return factors

print (factor(6000))
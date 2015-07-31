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

for i in range(30):
	print(i,is_prime(i))
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.



x, y , total= 1, 2, 0
j = 200

while y<j:
	if x % 2 == 0:
		total  = total + x
	elif y % 2 == 0:
		total = total + y
	x = x+ y
	y = x +y
	j = j + 1
print("The total is {} ".format(total))


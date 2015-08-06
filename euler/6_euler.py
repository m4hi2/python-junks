# The sum of the squares of the first ten natural numbers is,
# 										1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# 									(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

all_square = 0
each_square = 0
sum_number = 0
for x in range(1,101):
	each_square += x**2
for x in range(1, 101):
	sum_number +=x

print((sum_number**2) - each_square)
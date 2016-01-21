from math import sqrt

def num_factors(x):
	sum = 2
	for i in range(2, int(sqrt(x))+1):
		if x%i == 0:
			sum += 2
	return sum

x = 1
y = 2
while num_factors(x) < 500:
	x += y
	y += 1

print x
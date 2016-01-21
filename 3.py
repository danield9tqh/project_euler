from math import sqrt
def factor(x):
	for i in range(2, int(sqrt(x))+1):
		if x%i == 0:
			yield i
			for j in factor(x/i):
				yield j
			return
	yield x

for x in factor(600851475143):
	print x
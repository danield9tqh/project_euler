def primes_below(limit):
	a = [True] * limit
	a[0] = a[1] = False
	for (i, is_prime) in enumerate(a):
		if is_prime:
			yield i
			for j in xrange(i*i, limit, i):
				a[j] = False
				
sum = 0
for x in primes_below(2000000):
	sum += x
	
print sum
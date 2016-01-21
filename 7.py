#n must be a prime number 3 or greater
def next_prime(n):
	n+=2
	while not (is_prime(n)):
		n+=2
	return n
	
def is_prime(n):
	for i in range(2, n/2):
		if n%i == 0:
			return False
	return True

curr = 1
for i in range(1, 10001):
	curr = next_prime(curr)

print curr
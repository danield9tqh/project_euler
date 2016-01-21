def not_divisible(n):
	for i in range(11, 20):
		if n%i != 0:
			return True
	return False
	
curr = 2520
while not_divisible(curr):
	curr += 20
	
print curr
collatz_lengths = dict([(1, 1)])

def collatz_length(n):
	if n in collatz_lengths:
		return collatz_lengths[n]
	if n & 1:
		return 1 + collatz_length(3*n+1)
	else:
		return 1 + collatz_length(n/2)

for x in range(1, 1000001):
	if x in collatz_lengths:
		pass
	else:
		collatz_lengths[x] = collatz_length(x)

longest = max(collatz_lengths.values())

for x in collatz_lengths:
    if collatz_lengths[x] == longest:
        print x
sum = 0
i = 1
j = 2
while (i < 4000000):
	k = i+j
	i = j
	j = k
	if k%2 == 0:
		sum += k

print sum+2
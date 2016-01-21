def is_palindrome(n):
	n = str(n)
	for i in range(0, len(n)):
		if n[i] != n[-i-1]:
			return 0
	return 1

largest = 0
for i in range(100, 999):
	for j in range(100, 999):
		if is_palindrome(i*j) and i*j > largest:
			largest = i*j

print largest
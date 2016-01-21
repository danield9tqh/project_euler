d = dict()
d[0] = ''
d[1] = 'one'
d[2] = 'two'
d[3] = 'three'
d[4] = 'four'
d[5] = 'five'
d[6] = 'six'
d[7] = 'seven'
d[8] = 'eight'
d[9] = 'nine'
d[10] = 'ten'
d[11] = 'eleven'
d[12] = 'twelve'
d[13] = 'thirteen'
d[14] = 'fourteen'
d[15] = 'fifteen'
d[16] = 'sixteen'
d[17] = 'seventeen'
d[18] = 'eighteen'
d[19] = 'nineteen'
d[20] = 'twenty'
d[30] = 'thirty'
d[40] = 'forty'
d[50] = 'fifty'
d[60] = 'sixty'
d[70] = 'seventy'
d[80] = 'eighty'
d[90] = 'ninety'

def wordify(x):
	if x/1000 > 0:
		if x%1000 == 0:
			return wordify(x/1000) + " thousand"
		elif x%1000 < 100:
			return wordify(x/1000) + " thousand and " + wordify(x%1000)
		else:
			return wordify(x/1000) + " thousand " + wordify(x%1000)
	if x/100 > 0:
		if x%100 == 0:
			return wordify(x/100) + " hundred"
		else:
			return wordify(x/100) + " hundred" + " and " + wordify(x%100)
	if x/10 > 1:
		if x%10 == 0:
			return d[(x/10)*10]
		else:
			return d[(x/10)*10] + "-" +d[x%10]

	return d[x]

sum = 0
for x in range(1, 1001):
	sum += len(wordify(x).translate(None, ' -'))

print sum


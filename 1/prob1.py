
max_number = 1000

theNums = []
for val in range(max_number):
	if val%3 == 0:
		theNums.append(val)
	elif val%5 == 0:
		theNums.append(val)

print 'The answer is: '+str(sum(theNums))



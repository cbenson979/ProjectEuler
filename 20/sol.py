tempFile = open('./num.txt').read()
tempSum = 0
for aChar in tempFile:
	try:
		tempSum += int(aChar)
	except:
		pass
print 'Answer: '+str(tempSum)

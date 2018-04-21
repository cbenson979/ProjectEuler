import decimal


for d in range(2,1000):
	val = decimal.Decimal(1)/decimal.Decimal(d)
	print str(d)+' : '+str(val)+' : '+str(len(str(val)))
	if len(str(val)) < 30:
		continue
	
	tempStr = str(val).replace('0.','')
	
	# Remove leading 0s
	while True:
		if tempStr[0] == '0':
			tempStr = tempStr[1:]
		else:
			break
	print tempStr
	# Search for patterns in pairs of 2 strings
	for startingIndex in range(len(tempStr)-1):
		tempIndex = tempStr.find(tempStr[startingIndex:startingIndex+2],startingIndex+2)
		if tempIndex != -1:
			break
	print 'FOUND!! '+str(tempIndex)


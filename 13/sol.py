

def readData(fileName):
	tempData = open('./'+fileName,'r').read()
	return tempData.split('\n')

nums = readData('data.txt')

#### Loop though the numbers
currentDigitIndex = 50
remainder = 0
finalNum = ''
while currentDigitIndex != 0:
	currentDigitIndex -= 1
	tempSum = 0 + remainder
	for line in nums:
# 		print line
# 		print line[currentDigitIndex]
		tempSum += int(line[currentDigitIndex])
	tempSumStr = str(tempSum)
	if currentDigitIndex != 0:
		finalNum = tempSumStr[-1]+finalNum
	else:
		finalNum = tempSumStr+finalNum
	remainder = int(tempSumStr[:-1])

print finalNum
print 'first 10 digits: '+str(finalNum[-10:])
print 'last 10 digits: '+str(finalNum[:10])
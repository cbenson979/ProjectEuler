def findProperDivisors(n):
        if n == 1:
                return [1]
        currentN = n-1
        divisors = []
        while currentN != 0:
                if n%currentN == 0:
                        divisors.append(currentN)
                currentN -= 1

        return divisors

def classifyNum(n):
	intSum = sum(findProperDivisors(n))
	if n == intSum:
		return 'perfect'
	elif n > intSum:
		return 'deficient'
	elif n < intSum:
		return 'abundant'
		
upperLim = 28123

# Find all of the abundant ints under the upper limit
'''
abundantNums = []
for i in range(1,upperLim+1):
	if classifyNum(i) == 'abundant':
		print i
		abundantNums.append(i)

tempFile = open('abundantNums.txt','w+')
textOut = ''
for line in abundantNums:
	textOut += str(line)+'\n'
tempFile.write(textOut)
tempFile.close()
print abundantNums
'''
abundantNums = []
for line in open('abundantNums.txt','r').read().split('\n')[:-1]:
	abundantNums.append(int(line))
	
startVector = range(1,upperLim+1)
print 'Num we dealing with: '+str(len(abundantNums))
for index1,num1 in enumerate(abundantNums):
	print index1
	print len(startVector)
	for index2,num2 in enumerate(abundantNums[index1:]):
		tempSum = num1+num2
		if tempSum in startVector:
			startVector.pop(startVector.index(tempSum))
		elif tempSum > upperLim:
			break


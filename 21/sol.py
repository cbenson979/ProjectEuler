
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
	
def isAmicable(n):
	first = sum(findProperDivisors(n))
	second = sum(findProperDivisors(first))
	if first != second and second == n: # Amicable def
		return True, n, first
	else:
		return False, n, first

# Main code to hunt for the sum of amicable numbers below 100
topNum = 10000
amNums = []
currentNum = 1
while currentNum != topNum:
	currentNum += 1
	tempResult = isAmicable(currentNum)
	if tempResult[0] == True:
		for num in tempResult[1:]:
			if num in amNums:
				continue
			else:
				amNums.append(num)
				
print 'Amicable Nums: '+str(amNums)
print 'Sum of nums: '+str(sum(amNums))

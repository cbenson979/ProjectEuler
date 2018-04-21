

def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
# 		print '\t',f
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True  

def rotationThroughNumber(n,primeVect):
	tracker = []
	if len(str(n)) == 1:
		if is_prime(n) == True:
			primeVect.append(n)
	elif len(str(n)) > 1:
		theNum = str(n)
		if is_prime(n) == True:
			tracker.append(int(theNum))
		for i in range(len(theNum)-1):
			theNum = theNum[1:] + theNum[0]
			if is_prime(int(theNum)) == True:
				tracker.append(int(theNum))
		if len(tracker) == len(theNum):
			for val in tracker:
				if val not in primeVect:
					primeVect.append(val)
			


listOfPrimes = []

for i in range(2,1000000):
	if i in listOfPrimes:
		continue
	rotationThroughNumber(i,listOfPrimes)


'''
listOfPrimes = []
theDict = {}

for i in range(2,1000):
	if is_prime(i):
		listOfPrimes.append(i)
		tempList = list(str(i))
		tempList.sort()
		didIt = False
		for aName in theDict.keys():
			if tempList == theDict[aName]['vect']:
				theDict[aName]['count'] += 1
				didIt = True
		if didIt == False:
			theDict[str(i)] = {'vect':tempList[:],'count':1}

theCounter = 0
theNames = []
for aName in theDict.keys():
	if len(aName) == theDict[aName]['count']:
		theCounter += theDict[aName]['count']
		theNames.append(aName)
	stillTrue = True
	if len(aName) > 1:
		for s in aName:
			if s != aName[0]:
				stillTrue = False
				break
		if stillTrue == True:
			theCounter += 1
			theNames.append(aName)
			
# 		if tempList not in theList:
# 			theList.append(tempList)
'''






import math

def isPrime(n):
	upperLim = math.sqrt(n)

	i = 1
	isPrime = True
	while i < math.ceil(upperLim):
		i+=1
		if n%i == 0:
			isPrime = False
			break
		else:
			continue
	return isPrime


testNum = 600851475143

# find the smallest factor for the test number
factors = []

smallestFactor = 1
loopLim = 10000000000
while smallestFactor <= loopLim:
	smallestFactor += 1
	if testNum % smallestFactor == 0:
		if smallestFactor in factors:
			break
		factors.append(smallestFactor)
		factors.append(testNum/smallestFactor)
		print smallestFactor
		print testNum/smallestFactor

primeFactors = []
for val in factors:
	primeAnswer = isPrime(val)
	print str(val)+': '+str(primeAnswer)
	if primeAnswer:
		primeFactors.append(val)
		
print 'The Answer is: '+str(max(primeFactors))
	


# keepGoing = True
# 
# i = 1
# while keepGoing:
# 	i += 1
# 	if testNum%i == 0:
# 		other = testNum/i
# 		print other
# 		
# 		isOtherPrime = isPrime(other)
# 		if isOtherPrime == True:
# 			print 'We have found a large prime factor: '+str(i)
# 			keepGoing = False
# 		else:
# 			pass


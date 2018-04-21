import math

def is_prime(n):
	if n == 0 or n == 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0 and n > 2: 
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

def isSpecial(n):
	# forward
	str_n = str(n)
	for val in range(len(str_n)):
		tempNum = str_n[-1*val-1:]
		if is_prime(int(tempNum)) == False:
			return False		
	for val in range(len(str_n)):
		tempNum = str_n[:val+1]
		if is_prime(int(tempNum)) == False:
			return False
	return True

theList = []
for i in range(10,1000000):
	strNum = str(i)
	strNum_rev = str(i)[::-1]
	if int(strNum) in theList or int(strNum_rev) in theList:
		continue
	
	if isSpecial(int(strNum)) == True and isSpecial(int(strNum_rev)):
		theList.append(i)
		print theList

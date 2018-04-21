
def isPandigital(strIn):
	if len(strIn) != 9:
		return False
	for i in range(1,10):
		if str(i) not in strIn:
			return False
	return True
	
def eval(n):
	strOut = str(n)+str(n*2)
	factor = 3
	while len(strOut)<9:
		strOut += str(n*factor)
		factor += 1
		if len(strOut) >= 9:
			break

	if isPandigital(strOut):
		return int(strOut)
	else:
		return -1
		
results = []
for n in range(10000):
	tempResult = eval(n)
	if tempResult == -1:
		continue
	else:
		print(n,tempResult)
		results.append(tempResult)


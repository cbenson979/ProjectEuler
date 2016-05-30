
def evenCond(n):
	return n/2
	
def oddCond(n):
	return 3*n+1
	
def isOddTest(n):
	if n%2 == 0:
		return False
	else:
		return True
		
def seqGenerator(start_n):
	n = start_n
	
	counter = 1
# 	print n 
	while n != 1:
		counter += 1
		testt = isOddTest(n)
		if testt:
			n = oddCond(n)
		else:
			n = evenCond(n)
# 		print n
	return counter 
	
# haha = seqGenerator(13)
# print 'Num Terms = '+str(haha)

maxResult = {'num':0, 'iters':0}
for i in range(1,999999):
	tempResult = seqGenerator(i)
	
	if tempResult > maxResult['iters']:
		maxResult['num'] = i
		maxResult['iters'] = tempResult



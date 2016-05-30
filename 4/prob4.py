import math

def isPalodrome(n):
	strn = str(n)
	if strn == strn[::-1]:
		return True
	else:
		return False
	
######

startNumber = 999

num1 = startNumber
num2 = startNumber

stopNow = False
palodromeSet = []
while(not stopNow):
	tempProd = num1*num2
	if isPalodrome(tempProd):
# 		print 'Num1: '+str(num1)
# 		print 'Num2: '+str(num2)
# 		print 'Prod: '+str(tempProd)
		palodromeSet.append(tempProd)
# 		break
	num2 -= 1
	if num2 == 99:
		num1 -= 1
		num2 =num1
	if num2 == 99 and num1 == 99:
		stopNow = True
		
print palodromeSet
print 'The answer is: '+str(max(palodromeSet))
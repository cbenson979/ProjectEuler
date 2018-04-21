import math

def isPaladrome(strIn):
	if len(strIn) % 2 == 0: # even number
		firstHalf = len(strIn)/2
		front = strIn[:firstHalf]
		back = strIn[(firstHalf):][::-1]
	else: # Odd
		firstHalf = int(math.ceil(len(strIn)/2))
		front = strIn[:firstHalf]
		back = strIn[firstHalf+1:][::-1]
	
	if front == back:
		return True
	else:
		return False

numList = []
for i in range(1,1000000):
	tempInt = str(int(i))
	tempBin = str(bin(i)[2:])
	if isPaladrome(tempInt) == True and isPaladrome(tempBin) == True:
		numList.append(i)

print sum(numList)

import math

maxNum = 20	

divNums = range(1,maxNum+1)

stopLoop = False

i = maxNum
while(not stopLoop):
	i += 1
	youFail = False
	for val in divNums:
		if i%val == 0:
			continue
		else:
			youFail = True
			break
	if youFail == False:
		stopLoop = True

print 'The answer is: '+str(i)

upperLim = 4000000

fibSeq = [1,2]

while fibSeq[-1] < upperLim:
	fibSeq.append(fibSeq[-1]+fibSeq[-2])

runningSum = 0
for val in fibSeq[:-1]:
	if val%2 == 0:
		runningSum += val

print 'The Answer is: '+str(runningSum)


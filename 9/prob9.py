import math

sumConstraint = 1000
a = 1

foundIt = False
c = 0
while (not foundIt):
	a += 1
	b = a+1
	exitInner = False
	while (not exitInner):
		b += 1
		c = math.sqrt(a**2 + b**2)
		
		if (a + b + c == sumConstraint):
			foundIt = True
			break
		elif (a + b + c > sumConstraint):
			exitInner = True

print 'a = '+str(a)
print 'b = '+str(b)
print 'c = '+str(c)
print 'The Answer is: '+str(a*b*c)
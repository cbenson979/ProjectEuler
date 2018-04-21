
sum = 1

lastNumber = 1
for n in range(501):
	if n == 0:
		continue
# 	print 'n: '+str(n)
	for i in range(4):
# 		print 'i: '+str(i)
		lastNumber += 2*n
# 		print lastNumber
		sum += lastNumber
		
print sum


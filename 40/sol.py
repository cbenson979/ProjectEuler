

totalStr = ''
for i in range(1,1000000):
	totalStr += str(i)
	

result = int(totalStr[0])
for a in range(1,7):
	result *= int(totalStr[10**a-1])

print(result)



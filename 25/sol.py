import math

def calcFib(val1,val2):
	return math.log10(val1+val2)
	
results = [0,0]

for index in range(1470):
	results.append(calcFib(10**results[-2],10**results[-1]))
	
tempFile = open('results.txt','w+')
textOut = ''
for index,val in enumerate(results):
	print str(index)+' : '+str(val)
	textOut += str(val)+'\n'

tempFile.write(textOut)
tempFile.close()
	
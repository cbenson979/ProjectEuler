import math

def calcFib(val1,val2):
	#return math.log10(val1+val2)
	return val1 + val2

results = [1,1]

for index in range(1470):
	results.append(calcFib(results[-2],results[-1]))
	
tempFile = open('results.txt','w+')
textOut = ''
for index,val in enumerate(results):
	print str(index)+' : '+str(val)+' : '+str(len(str(val)))
	textOut += str(index)+';'+str(len(str(val)))+'\n'

tempFile.write(textOut)
tempFile.close()
	

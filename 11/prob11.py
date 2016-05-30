

fileData = open('dataIn.txt').read().split('\n')
dataSet = []
for line in fileData:
	dataSet.append(line.split(' '))
	
diagProdSet = []
for rowIndex in range(len(dataSet)-3):
	for index in range(len(dataSet[0])-3):
		tempProd = int(dataSet[rowIndex][index])
		for index2 in range(1,4):
			tempProd *= int(dataSet[rowIndex+index2][index+index2])
		diagProdSet.append(tempProd)

# print 'The Answer is: '+str(max(prodSet))
# now lets do left
leftProdSet = []
for rowIndex in range(len(dataSet)):
	for index in range(len(dataSet[0])-3):
		tempProd = int(dataSet[rowIndex][index])
		for index2 in range(1,4):
			tempProd *= int(dataSet[rowIndex][index+index2])
		leftProdSet.append(tempProd)
		
upProdSet = []
for rowIndex in range(len(dataSet)-3):
	for index in range(len(dataSet[0])):
		tempProd = int(dataSet[rowIndex][index])
		for index2 in range(1,4):
			tempProd *= int(dataSet[rowIndex+index2][index])
		upProdSet.append(tempProd)	
		
diagProdSet2 = []
for rowIndex in range(len(dataSet)-3):
	for index in range(3,len(dataSet[0])):
		tempProd = int(dataSet[rowIndex][index])
		for index2 in range(1,4):
			tempProd *= int(dataSet[rowIndex+index2][index-index2])
		diagProdSet2.append(tempProd)
		
print 'The answer is '+str(max([max(diagProdSet),max(leftProdSet),max(upProdSet), max(diagProdSet2)]))

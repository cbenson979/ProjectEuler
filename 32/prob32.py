
def isPandigital(one,two,prod):
	totalStr = str(one)+str(two)+str(prod)
	if len(totalStr) != 9:
		return False
	if '0' in totalStr:
		return False
	theList = []
	for aVal in totalStr:
		if aVal not in theList:
			theList.append(aVal)
	if len(theList) == 9:
		return True
	else:
		return False
		
yay = []
set = []
for i in range(1,999999):
	print i, len(yay), sum(yay)
	for j in range(99999):
		tempProd = i*j
		if len(str(i)+str(j)+str(tempProd)) > 9:
			break
		if isPandigital(i,j,tempProd):
			if tempProd not in yay:
				yay.append(tempProd)
				set.append([i,j,tempProd])

# 449061

def isSpecialFraction(num,denom):
	if len(str(num)) != 2 or len(str(denom)) != 2:
		return False
	
	num_s = str(num); denom_s = str(denom)
# 	if (num_s[0] in denom_s) or (num_s[1] in denom_s):
	if num_s[0] in denom_s:
		if num_s[0] == '0':
			return False
		denomList = list(denom_s)
		denomList.pop(denom_s.index(num_s[0]))
		num_s = num_s[1:]
	elif num_s[1] in denom_s:
		if num_s[1] == '0':
			return False
		denomList = list(denom_s)
		denomList.pop(denom_s.index(num_s[1]))
		num_s = num_s[:1]
	else:
		return False
	
	if float(denomList[0]) == 0.0:
		return False
	if float(num)/float(denom) == float(num_s)/float(denomList[0]):
		return True
	else:
		return False
		
# print isSpecialFraction(49,97)
denProd = 1
numProd = 1
for den in range(10,100):
	for num in range(10,100):
		if num >= den:
			break
		if isSpecialFraction(num,den):
			print num,den,float(num)/float(den)
			denProd *= den
			numProd *= num



import math

def findValidSolutionsForB(a,p):
	results = []
	for b in range(a,1000):
		if (math.sqrt(a**2 + b**2)) == (p - a - b):
			# This is a valid solution
			results.append((a,b))
	return results

def solutionsPerP(p):
	solCount = 0
	for a in range(1,1000):
		tempResult = findValidSolutionsForB(a,p)
		if len(tempResult) == 0:
			continue
		else:
			solCount += len(tempResult)
# 			print(tempResult)
	return solCount
			

countResults = []
for aP in range(1,999):
	print(aP)
	countResults.append(solutionsPerP(aP))
	





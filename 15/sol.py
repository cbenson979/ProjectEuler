### Grid problem - taxi cab routes.
import math

def middleNum(vectt):
	tempLen = len(vectt)
	return math.ceil(tempLen/2)

pascalsTriangle = [[1],[1,1],[1,2,1]]

while len(pascalsTriangle) < 50:
	tempRow = [1]
	for i in range(len(pascalsTriangle[-1])-1):
		tempRow.append(pascalsTriangle[-1][i]+pascalsTriangle[-1][i+1])
	tempRow.append(1)
	pascalsTriangle.append(tempRow)
	
for i in range(2,22):
	print i
	print 2*i
	print pascalsTriangle[2*i][int(middleNum(pascalsTriangle[2*i]))]
	print ''
	



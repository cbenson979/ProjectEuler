import math

def factSum(val):
	val_s = str(val)
	tempSum = 0
	for s in val_s:
		tempSum += math.factorial(int(s))
	if val == tempSum:
		return True
	else:
		return False
		
vals = []
for a in range(3,1000000):
	if factSum(a):
		vals.append(a)
		print a




theList = []
for i in range(10,1000000):
	tempSum = 0
	for j in str(i):
		dude = int(j)
		tempSum += dude**5
	if tempSum == i:
		theList.append(int(i))
		
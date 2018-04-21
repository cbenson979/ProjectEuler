
listOnums = []

for a in range(2,101):
	for b in range(2,101):
		tempVal = a**b;
		if tempVal not in listOnums:
			listOnums.append(tempVal)

print len(listOnums)

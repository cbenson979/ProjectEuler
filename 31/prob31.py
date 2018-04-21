
winningSum = 1

for n100 in range(3):
	for n50 in range(5):
		for n20 in range(11):
			for n10 in range(21):
				for n5 in range(41):
					for n2 in range(101):
						for n1 in range(201):
							tempSum = n100*100 + n50*50 + n20*20 + n10*10 + n5*5 + n2*2 + n1*1
							if tempSum == 200:
								winningSum += 1
							elif tempSum > 200:
								break


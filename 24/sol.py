import itertools

# print len(list(itertools.permutations(range(10),10)))
haha = list(itertools.permutations(range(10),10))

print haha[1000000-1]
strOut = ''
for val in haha[1000000-1]:
	strOut += str(val)
	
print strOut

# dude = list(itertools.permutations(range(4),3))
# print dude


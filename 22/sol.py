
def wordSum(word):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	tempSum = 0
	for letter in word:
			tempSum += alphabet.index(letter)+1
	return tempSum

tempFile = open('./p022_names.txt').read().replace('"','').split(',')
tempFile.sort()

scoreTotal = 0
for index,line in enumerate(tempFile):
	scoreTotal += (index+1)*wordSum(line)
print 'Answer: '+str(scoreTotal)


onesDict = {'one':len('one'), 'two':len('two'), 'three':len('three'), 'four':len('four'),'five':len('five'),'six':len('six'),'seven':len('seven'),'eight':len('eight'),'nine':len('nine')}

specialDict = {'ten':len('ten'),'eleven':len('eleven'),'twelve':len('twelve'),'thirteen':len('thirteen'),'fourteen':len('fourteen'),'fifteen':len('fifteen'),'sixteen':len('sixteen'),'seventeen':len('seventeen'),'eighteen':len('eighteen'),'nineteen':len('nineteen')}

tensDict = {'twenty':len('twenty'),'thirty':len('thirty'),'fourty':len('fourty'),'fifty':len('fifty'),'sixty':len('sixty'),'seventy':len('seventy'),'eighty':len('eighty'),'ninety':len('ninety')}

### sub 100

## 1 to 19
sub20 = sum(onesDict.values()) + sum(specialDict.values())

sum20To99 = 0
for i in tensDict.keys():
	sum20To99 += tensDict[i]
	for j in onesDict.keys():
		sum20To99 += tensDict[i] + onesDict[j]
		 
sum1To99 = sub20 + sum20To99
 
totalSum = sum1To99
for i in onesDict.keys():
	totalSum += onesDict[i]+len('hundred')
	totalSum += 100*len('hundredand')+sum1To99
	
totalSum += len('onethousand')

print 'solution: '+str(totalSum)




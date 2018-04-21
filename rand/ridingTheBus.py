import random
import matplotlib.pyplot as plt
import numpy as np

def rideTheBus():
	### Init the deck
	suits = ['s','c','d','h']
	cardVal = range(2,15)

	allCards = []
	for val in cardVal:
		for suit in suits:
			allCards.append(str(val)+suit)
		
	### init the 13 cards
	busDeck = []
	for i in range(13):
		randInt = random.randint(0,len(allCards)-1)
		busDeck.append(allCards[randInt])
		allCards.pop(randInt)
	
	### draw loop
	drinkCounter = 0
	faceCardsHit = 0
	outOfCards = False
	while len(busDeck) > 0:
		currentLength = len(busDeck)
		# Draw the last card in the sack
		currentCard = busDeck[currentLength-1]
		tempCardVal = int(currentCard[:-1])
		busDeck.pop(currentLength-1)
		if tempCardVal - 10 > 0: # if a face card
			faceCardsHit += 1
			drinkCounter += tempCardVal - 10
			for i in range(tempCardVal - 10):
				if len(allCards) == 0:
					outOfCards = True
					break
				# Draw correct number of cards from the deck and add to the bus.
				randInt = random.randint(0,len(allCards)-1)
				busDeck.append(allCards[randInt])
				allCards.pop(randInt)
		else:
			continue

	return drinkCounter

drinkDist = []
for i in range(100000):
	if i%100 == 0:
		print(i)
	drinkDist.append(rideTheBus())	

drinks_np = np.array(drinkDist)
expectedNumOfDrinks = drinks_np.mean()

fig,ax = plt.subplots()
ax.hist(drinkDist,bins=40,density=True,cumulative=True)
ax.set_xlabel('Number of Drinks')
ax.set_ylabel('Probability')
ax.set_title('Probability of getting screwed by the bus (1M simulations)')
fig.show()


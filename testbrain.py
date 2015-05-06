import brain
import random
import math
import card
b = brain.Brain()

own = []
desk = []
for i in range(7):
	r = random.random()*4
	if r < 1:
		suit = 'diamond'
	elif r < 2:
		suit = 'clubs'
	elif r < 3:
		suit = 'heart'
	else:
		suit = 'spade'
	rank = int(math.ceil(random.random() * 13))
	c = card.Card(suit, rank)
	if i < 2:
		own.append(c)
		# print 'own ',c
	else:
		desk.append(c)
		# print 'desk ',c

b.decide(1, own, desk, False)	
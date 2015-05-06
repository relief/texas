import card
def checkStraight(ranks):
	if ranks[0] == 13 and ranks[1] == 12 and ranks[2] == 11 and ranks[3] == 10 and ranks[4] == 1:
		return True
	for i in range(4):
		if ranks[i] != ranks[i+1] + 1:
			return False
	return True

def checkFlush(suits):
	for i in range(4):
		if suits[i] != suits[i+1]:
			return False
	return True

def checkNumSame(ranks):
	uniqueNum = len(set(ranks))
	if uniqueNum == 2: 
		if ranks[1] == ranks[2] and ranks[2] == ranks[3]:
			return 4 # four of a kind
		return 3.5 # full house
	if uniqueNum == 3:
		for i in range(3):
			if ranks[i] == ranks[i+1] and ranks[i+1] == ranks[i+2]:
				return 3 # three of a kind
		return 2.5	# two pairs
	if uniqueNum == 4:
		return 2	# one pair
	return 1 # high cards

class Hand:
	handOrder = {
		'High_Card':0, 'One_Pair':1, 'Two_Pair':2, 
		'Three_of_a_Kind':3, 'Straight':4,  'Flush': 5,
		'Full_House': 6, 'Four_of_a_Kind':7, 'Straight_Flush': 8
	}
	
	def __init__(self, card0, card1, card2, card3, card4):
		self.cards = [card0, card1, card2, card3, card4]
		self.ranks = [card0.rank, card1.rank, card2.rank, card3.rank, card4.rank]
		self.suits = [card0.suit, card1.suit, card2.suit, card3.suit, card4.suit]
		self.handtype = self.evaluate()

	def __str__(self):
		s = '\n---------------Begin of hand--------------\n'
		s += self.handtype + '\n'
		for c in self.cards:
			s += str(c) + ' '
		s += '\n--------------End of hand -----------------'
		return s


	def __ge__(self, comp):
		if self.handOrder[self.handtype] > self.handOrder[comp.handtype]:
			return True
		if self.handOrder[self.handtype] < self.handOrder[comp.handtype]:
			return False
		self_ranks = sorted(self.ranks, reverse = True)
		comp_ranks = sorted(comp.ranks, reverse = True)
		if self_ranks[0] != 5 or (self.handtype != 'Straight' and self.handtype != 'Straight_Flush'):
			while self_ranks[-1] == 1:
				# print "before trans self", self_ranks
				self_ranks.pop()
				self_ranks.insert(0, 14)
				# print "after trans", self_ranks
		if comp_ranks[0] != 5 or (comp.handtype != 'Straight' and comp.handtype != 'Straight_Flush'):
			while comp_ranks[-1] == 1:
				# print "before trans comp", comp_ranks
				comp_ranks.pop()
				comp_ranks.insert(0, 14)
				# print "after trans", comp_ranks
		for i in range(5):
			if self_ranks[i] > comp_ranks[i]:
				return True
			if self_ranks[i] < comp_ranks[i]:
				return False
		return True

	def evaluate(self):
		ranks = sorted(self.ranks, reverse=True)
		Straight = checkStraight(ranks)
		Flush = checkFlush(self.suits)
		maxNumSame = checkNumSame(ranks)
		if Straight and Flush:
			return 'Straight_Flush'
		elif maxNumSame == 4:
			return 'Four_of_a_Kind'
		elif maxNumSame == 3.5:
			return 'Full_House'
		elif Flush:
			return 'Flush'
		elif Straight:
			return 'Straight'
		elif maxNumSame == 3:
			return 'Three_of_a_Kind'
		elif maxNumSame == 2.5:
			return 'Two_Pair'
		elif maxNumSame == 2:
			return 'One_Pair'
		else:
			return 'High_Card'	
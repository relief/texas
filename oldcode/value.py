import card

class Evaluator:
	def __init__(self):
		pass

	def evaluate(self, card1, card2, card3, card4, card5):
		ranks = [card1.rank, card2.rank, card3.rank, card4.rank, card5.rank]
		suits = [card1.suit, card2.suit, card3.suit, card4.suit, card5.suit]
		ranks.sort(reverse=True)
		suits.sort()
		Straight = self.checkStraight(ranks)
		Flush = self.checkFlush(suits)
		maxNumSame = self.checkNumSame(ranks)
		if Straight and Flush:
			hand = 'Straight_Flush'
		elif maxNumSame == 4:
			hand = 'Four_of_a_Kind'
		elif maxNumSame == 3.5:
			hand = 'Full_House'
		elif Flush:
			hand = 'Flush'
		elif Straight:
			hand = 'Straight'
		elif maxNumSame == 3:
			hand = 'Three_of_a_Kind'
		elif maxNumSame == 2.5:
			hand = 'Two_Pair'
		elif maxNumSame == 2:
			hand = 'One_Pair'
		else:
			hand = 'High_Card'
		return hand, self.evaluateOnHand(hand)

	def checkStraight(self, ranks):
		for i in range(4):
			if ranks[i] + 1 != ranks[i+1]:
				return False
		return True

	def checkFlush(self, suits):
		for i in range(4):
			if suits[i] != suits[i+1]:
				return False
		return True

	def checkNumSame(self, ranks):
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

	def evaluateOnHand(self, ranks, hand):
		return self.handbase[hand]
		#val = 0
		# if hand == 'Straight_Flush':
		# 	val = 






class TwoCards:
	prob = dict()
	def __init__(self):
		with open('odds/2_cards_odds.dat','r') as dat:
			for line in dat:
				tokens = line.split(' ')
				self.prob[tokens[0],tokens[1],tokens[2]] = float(tokens[3]) + float(tokens[5])
				self.prob[tokens[1],tokens[0],tokens[2]] = float(tokens[3]) + float(tokens[5])
		print '---------Loading Two Cards Data----------'
		# print self.prob

	def getRate(self, card1, card2, my_turn_round):
		num1 = self.rankToSymbol(card1.rank)
		num2 = self.rankToSymbol(card2.rank)
		if card1.suit == card2.suit:
			suit = 'suited'
		else:
			suit = 'unsuited'
		raw_prob = self.prob[num1,num2,suit]
		print "	TwoCards: ", num1, num2, suit
		return raw_prob

	def rankToSymbol(self, num):
		if num == 1:
			return 'A'
		elif num == 13:
			return 'K'
		elif num == 12:
			return 'Q'
		elif num == 11:
			return 'J'
		elif num == 10:
			return 'T'
		return str(num)
		
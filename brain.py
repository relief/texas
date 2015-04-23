from dapai import qipai, genzhu, allin, addone
class Brain:
	def __init__(self):
		pass

	def print_current(self, game_round, own, desk, canRangpai):
		print "My turn: ", game_round
		print "Own: ",
		for o in own:
			print o,',',
		print "\nDesk: ",
		for d in desk:
			print d,',',
		print "\ncanRangpai: ", canRangpai
	def decide(self, game_round, own=[], desk=[], canRangpai=False):
		self.print_current(game_round, own, desk, canRangpai)
	 	if canRangpai:
			genzhu()
		else:
			if own[0].rank == own[1].rank:
				if own[0].rank > 12 or game_round > 5:
					genzhu()
				else:
					qipai()
			else:
				qipai()
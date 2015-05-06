Texas Holdem AI for Wechat

Model:
	Player Eyes:  Screenshot + simple CV
	Player Hands: Record and Replay 
	Player Brain: conservative Texas Holdem AI

Brain Version 1:
	Compare prob with threshold

	Only Own Cards: Look up prob on odds chart
	Three to five desk cards:
		enumerate all possible rivals' two cards. Compare it with own card to see out of what percentage we win.

Brain Version 2:
	Pursue highest expectation in each operation.

	Extra Infor needs:
		ChiDi
		Options []
		Num_of_rivals
		Own_total_gold

	Prob to win:
		raw_prob	Prob to win under 1 rival
		prob = raw_prob ^ num_of_rivals

	Expectation:
		E = prob * (ChiDi + opt) + (1 - prob)*(Own_total_gold - opt)	opt in Options[]
			Own_total_gold												qipai




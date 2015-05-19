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
		E = prob * (ChiDi(opt) + own - opt) + (1 - prob)*(Own_total_gold - opt)	, opt in Options[]
		  = prob * (ChiDi(opt)) + own - opt
		  
		Maximize -------------   prob * (ChiDi(opt)) - opt

			Own_total_gold							       , qipai

		ChiDi(opt)
			chidi_current + sum(opt - sofar) >= ChiDi(opt) >= chidi_current + opt - max(sofar)

		E1_upper, E1_lower, E2_upper, E2_lower.....

		E1 _________   |
		E2      _______|_
		E3 			 __|_______
					   |
					   0
		    ________       Choose E1
		    		___    Chosse E2
		    			   Attention: The last one may choose fold

	To-do:
		get num_of_rivals
		get chidi_current
		get each_put_money
		get opts






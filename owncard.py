import Image

import random

im = Image.open("own/all/0.272239950507.png")
im.show()
#region = im.crop(box_state)
#region.save('state/tmp.png')

box_card1_suit = (0,9,37,40)
card1_suit = im.crop(box_card1_suit)
#card1_suit.show()

box_card1_rank = (40,6,93,40)
card1_rank = im.crop(box_card1_rank)
#card1_rank.show()

box_card2_suit = (0,50,37,80)
card2_suit = im.crop(box_card2_suit)
#card2_suit.show()

box_card2_rank = (38,58,93,92)
card2_rank = im.crop(box_card2_rank)
#card2_rank.show()
import Image

import random

im = Image.open("r.png")
#im.show()
#region = im.crop(box_state)
#region.save('state/tmp.png')

box_card1_suit = (30,1200,125,1300)
card1_suit = im.crop(box_card1_suit)
card1_suit.save('state/rangpai.png')
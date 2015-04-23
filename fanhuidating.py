import Image

import random

im = Image.open("screen.png")
#im.show()
#region = im.crop(box_state)
#region.save('state/tmp.png')

box_card1_suit = (30,0,125,200)
card1_suit = im.crop(box_card1_suit)
card1_suit.show()
#card1_suit.save('state/rangpai.png')
import Image
import ImageComp as ic

width  = 180
height = 133
padding = 21
left = 500
next = height + padding
leftTop = [(left,522),(left,522+next),(left,522+2*next),(left,522+3*next),(left,522+4*next)]
box_num = (118,2,177,45)
box_type = (75,5,117,40)
box_state = (30,780,125,800)
box_own = (275,955,370,1050)

def getImage():
	mode = 'RGBA'
	size = (1080, 1920)
	f = open('data/screenshot.raw', 'rb')
	f.read(12)
	im = Image.frombuffer(mode, size, f.read(), "raw", mode, 0, 1)
	return im
# im.save('screenshot.png')

# All the parameters here


import random

region_state = im.crop(box_state)
region_state.save('state/tmp.png')
if ic.compareState() == 0:
	quit()

print 'Chu Pai Now!'

region_own = im.crop(box_own)
fn = str(random.uniform(0, 100))
region_own.save('own/all/'+fn+'.png')

i = 0
cards = []
for lt in leftTop:
	i += 1
	box = (lt[0],lt[1],lt[0]+width,lt[1]+height)
	region = im.crop(box)
	#fn = str(random.uniform(0, 100))
	#region.save('deskcard/20150416/'+fn+'.png')

	fn = 'num/tmp_'+str(i)+'.png'
	
	region_num = region.crop(box_num)
	region_num.save(fn)
	card_num = ic.compareNum(fn)

	fn = 'type/tmp_'+str(i)+'.png'
	
	region_type = region.crop(box_type)
	region_type.save(fn)
	card_type = ic.compareType(fn)
	#print card_num,'_',card_type
	if card_type != "unknown" and card_num != "unknown":
		cards.append(card_type+"_"+card_num)

print cards
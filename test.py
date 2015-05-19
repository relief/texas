import Image
import os
path = "all/"
dirs = os.listdir( path )
import random
box = (787, 880, 822, 980)
for file in dirs:
	print file
	if file[-1] != 'g':
		continue
	im = Image.open(path+file)
	nfn = 'pot/all/'+file
	im = im.crop(box).save(nfn)



# 	cimg = cv2.imread(path+file)
# 	cimg = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
# 	name = compareCard2Rank(cimg)
# 	os.rename(path+file, path+str(name)+"_"+str(random.uniform(0, 100))+".png")
# im = Image.open("record/2015-05-05 17:00:53.png")
# im = im.rotate(90).crop((800,230,1300,650)).show()
# box = (800,230,1300,650)
# im.crop(box).show()
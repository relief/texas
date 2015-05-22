import Image
import os
import cv2
import numpy
import random

def img2gray(img):
	cv2_data = numpy.array(img)
	# cv2_data = cv2.cvtColor(cv2_data, cv2.COLOR_RGB2GRAY)
	return cv2_data

path = "all/"
dirs = os.listdir( path )
width = 40
height= 10
box = [(214,339,214+width,339+height),(220,1488,220+width,1488+height)
,(400, 46, 400+width, 46+height),(410,1747,410+width,1747+height)
,(734,94,734+width,94+height),(738,1711,738+width,1711+height)
,(842,377,842+width,377+height),(853,1410,853+width,1410+height)]
low = 1
for file in dirs:
	print file
	low += 1
	if file[-1] != 'g' and low > 4:
		continue
	im = Image.open(path+file)
	# im.show()
	
	# continue
	# b = box[-1]
	numOfRivals = 0
	for b in box:
		img = im.crop(b)
		data = img2gray(img)
		s =  numpy.sum(img)
		
		if s > 260000 and s < 300000:
			numOfRivals += 1
		# img.show()
		# im.crop(b).show()
	print numOfRivals
	im.save('rivals/test/'+str(numOfRivals)+'_'+str(random.random())+'.png')
	# break
	# nfn = 'pot/all/'+file
	# im = im.crop(box).save(nfn)






# 	cimg = cv2.imread(path+file)
# 	cimg = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
# 	name = compareCard2Rank(cimg)
# 	os.rename(path+file, path+str(name)+"_"+str(random.uniform(0, 100))+".png")
# im = Image.open("record/2015-05-05 17:00:53.png")
# im = im.rotate(90).crop((800,230,1300,650)).show()
# box = (800,230,1300,650)
# im.crop(box).show()
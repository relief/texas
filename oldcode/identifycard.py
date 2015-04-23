import Image
import random
import os, sys

width  = 80
height = 33

path = "deskcard/"
dirs = os.listdir( path )
i = 0
for file in dirs:
	im = Image.open("deskcard/"+file)
	box_num = (118,2,177,45)
	region_num = im.crop(box_num)
	i += 1
	region_num.save('num/'+str(i)+'.png')
	#raw_input("asfdasdf")
	#region_type.save('type/tmp.png')
	# box_type = (75,5,117,40)
	# region_type = im.crop(box_type)
	# region_type.save('type/tmp.png')


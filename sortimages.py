import cv2
import sys
import readchar

if len(sys.argv) != 3:
	print('Too few arguments!')

filelist = open(sys.argv[1],'r').readlines()
startindex = int(sys.argv[2])

one_train_dir = '/Users/dhawal/Desktop/aqi/images.nosync/acapp_data/training_images/one_train/'
mul_trains_dir = '/Users/dhawal/Desktop/aqi/images.nosync/acapp_data/training_images/mul_trains/'
no_train_dir = '/Users/dhawal/Desktop/aqi/images.nosync/acapp_data/training_images/no_train/'
night_train_dir = '/Users/dhawal/Desktop/aqi/images.nosync/acapp_data/training_images/night_train/'
night_no_train_dir = '/Users/dhawal/Desktop/aqi/images.nosync/acapp_data/training_images/night_no_train/'

ch = 'n'
i = startindex

while ch!='q':
	print(i)
	line = filelist[i].split(',')
	img = cv2.imread(line[-1].split('\n')[0])
	cv2.imshow('is a train?',img)
	cv2.waitKey(1)
	name = line[0]
	if ch == '1':
		cv2.imwrite(one_train_dir+name+'.jpg',img)
	elif ch == '2':
		cv2.imwrite(mul_trains_dir+name+'.jpg',img)
	elif ch == '3':
		cv2.imwrite(no_train_dir+name+'.jpg',img)
	elif ch == '4':
		cv2.imwrite(night_train_dir+name+'.jpg',img)
	elif ch == '5':
		cv2.imwrite(night_no_train_dir+name+'.jpg',img)
	i += 1
	ch = readchar.readchar()
cv2.destroyAllWindows()
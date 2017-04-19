import pyscreenshot as ImageGrab

if __name__ == '__main__':
	img = ImageGrab.grab(bbox=(10,10,510,510)) # x1,y1,x2,y2
	img.show()
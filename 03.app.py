# take a shot

import pyscreenshot as ImageGrab

if __name__ == '__main__':
	#grab fullscreen
	im = ImageGrab.grab()
	#save
	im.save('screenshot.png')
	#show
	print dir(im)
	im.show()
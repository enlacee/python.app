import dropbox
import pyscreenshot as ImageGrab

client = dropbox.client.DropboxClient('Ml49Ttea9S0AAAAAAAAE2kxSlHilublhxej-5vxeXW3vELFtCU68vwEK-hNU9rZw')
print 'linked account: ', client.account_info()

img = ImageGrab.grab()
quality_val = 80
filename = 'screenshot.jpg'
img.save(filename, 'JPEG', quality=quality_val)

f = open(filename, 'rb')
response = client.put_file('/screenshot-upload.jpg', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

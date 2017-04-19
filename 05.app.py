import dropbox

client = dropbox.client.DropboxClient('Ml49Ttea9S0AAAAAAAAE2kxSlHilublhxej-5vxeXW3vELFtCU68vwEK-hNU9rZw')
print 'linked account: ', client.account_info()

f = open('txt.txt', 'rb')
response = client.put_file('/txt-opus.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/txt-opus.txt')
out = open('txt-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata
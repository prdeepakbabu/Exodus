from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
#gauth.LocalWebserverAuth()

#gauth.SaveCredentialsFile("mycreds.txt")
gauth.LoadCredentialsFile("mycreds.txt")
drive=GoogleDrive(gauth)
#file1 = drive.CreateFile({'title': 'Deepak.txt'})
#file1.SetContentString('Hello')
file1=drive.CreateFile()
file1.SetContentFile('dum.jpg')
file1.Upload() # Files.insert()
print 'title: %s' % file1['title']
print 	'id: %s' % file1['id'] 

import urllib2, os
import shutil, sys

def downloadImages(path, nameOfFile):
	
	'''opening list of url from the current working directory location
	   assuming the name of the file which contains the list of urls is the urls.txt'''

	if path.__len__() is 0:					#if the length of the path is empty it will take the  current working directory as path
		path = os.getcwd()

	'''checking for if the folder to download already exists and removing the folder if already present'''

	if not os.path.exists(path+'/downloaded_pics'):
		os.makedirs(path+'/downloaded_pics')
	else:		
		shutil.rmtree(path+'/downloaded_pics')					#if already folder exists deleting the entire folder for downloading afresh
		os.makedirs(path+'/downloaded_pics')
	try:
		inputFile = open(path+'/'+nameOfFile)					#reading from file assuming the name of the file is url.txt
	except (OSError, IOError):
		raise 'file mentioned is not present in the location'
												
	valid_file_extensions = ['jpg', 'jpeg', 'png', 'ico', 'gif', 'bmp']
	for line in inputFile:
		if line.strip().__len__()>0:
			image = urllib2.urlopen(line).read()
			tokens = line.split('/')													#splitting the URL by / as delimiter 
			filename = tokens[tokens.__len__()-1].split('.')[0]   						#taking the end of the url as the token to create a new file	
			extension = tokens[tokens.__len__()-1].split('.')[1].strip()				#assuming the end of url is the extension of the image type
			if extension in valid_file_extensions:
				pass
			else:
				extension = 'jpg'
			with open(path+'/downloaded_pics/'+filename+'.'+extension, 'wb') as f:		
			    f.write(image)
		else:
			pass
	print 'downloading images is completed'
	f.close()											#closing the filewriter

if __name__ == "__main__":
	path = sys.argv[1]								#mention the path where file which contains url is present
	nameOfFile = sys.argv[2]						#argument to fetch the name of the file which contains urls
	downloadImages(path, nameOfFile)
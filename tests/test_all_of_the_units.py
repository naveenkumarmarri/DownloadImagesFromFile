import urllib2, os
import shutil

if not os.path.exists(path+'/downloaded_pics'):
		os.makedirs(path+'/downloaded_pics')
else:		
		shutil.rmtree(path+'/downloaded_pics')					#if already folder exists deleting the entire folder for downloading afresh
		os.makedirs(path+'/downloaded_pics')
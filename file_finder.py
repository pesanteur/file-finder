#! python3 
# file_finder.py - Locates files or folders over 100mb in a tree 
# then prints the files with their absolute path to the screen

import os

def file_finder(folder):

	# Walk through various folders in the given path
	for foldername, subfolders, filenames in os.walk(folder):
		
		for filename in filenames:
			file_path = os.path.join(foldername, filename)
			file_size = os.path.getsize(file_path)
			if file_size > 100000000:
				print(os.path.abspath(filename))
		
file_finder(folder)
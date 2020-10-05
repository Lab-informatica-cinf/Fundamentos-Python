#!/usr/bin/python3

'''This script receive a path Directory, 
all file paths.
e.g: input '/MovieRecommendSystem' ie. via command line interface
	 return: [MovieRecommendSystem/data/fileone,
	 		  MovieRecommendSystem/data/filetwo,
	 		  MovieRecommendSystem/collectData/scriptone,
	 		  MovieRecommendSystem/collectData/scripttwo]

This scrip is build with os built-in python package from standar library, for parse paths;
and sys, for handle input via command line interface.	 		  
'''

import os
import sys

def walk_directory(path_to_directory):
	'''this function reveive a path directory, 
	and return a list of path files. '''
	
	global path_files
	path_files = []
	

	for root, dirs, files in os.walk(path_to_directory):
		for _file in file:
		path_files.append(os.path.join(root,_file))

	return path_files

def main():
	walk_directory(sys.argv[1])

if __name__ == '__main__':
	main()                  #activate main for run from terminal. std input ='path_to_directory'
	print(path_files)
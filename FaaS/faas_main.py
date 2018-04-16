import pickle
import sys
import os
from os import listdir
from os.path import isfile, join
import glob

read_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'CustomerInterface/WriteContent/'))

def does_file_exist_in_dir(path):
	return any(isfile(join(path, i)) for i in listdir(path))

while True:
	if not does_file_exist_in_dir(read_path):
		continue
	
	for infile in sorted(os.listdir(read_path)):
		print infile 
		os.remove(os.path.join(read_path, infile))
		break
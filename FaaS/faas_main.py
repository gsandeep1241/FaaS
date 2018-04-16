import cPickle as pickle
import sys
import os
from os import listdir
from os.path import isfile, join
import glob

read_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'CustomerInterface/WriteContent/'))
write_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'CustomerInterface/ReadContent/'))

def does_file_exist_in_dir(path):
	return any(isfile(join(path, i)) for i in listdir(path))

while True:
	if not does_file_exist_in_dir(read_path):
		continue
	
	file_name = ""
	for infile in sorted(os.listdir(read_path)):
		file_name = os.path.join(read_path, infile)
		event_obj = {}
		with open(file_name, 'rb') as f:
			event_obj = pickle.load(f)
			f.close()
			
		ID = event_obj['key']
		execute_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'Storage'))
		execute_path = os.path.join(execute_base_path, ID)
		sys.insert(0, execute_path)
		import main
		
		
		os.remove(file_name)
		file_name = os.path.join(write_path, infile)
		f = open(file_name, 'wb')
		pickle.dump(event_obj, f)
		f.close()
		print(infile + " file removed")
		break
		
	break
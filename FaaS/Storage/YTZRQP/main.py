import pickle
import ast
import os
import sys

ID = "YTZRQP"
db_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../Database/'))
db_path = os.path.join(db_base_path, (ID+'.pckl'))

dogs = {}

def init():
	try:
		with open(db_path, 'rb') as f:
			dogs = pickle.load(f)
			f.close()
		
	except IOError:
		dogs = {}

def dest():
	f = open(db_path, 'wb')
	pickle.dump(dogs, f)
	f.close()

def add(data):
	init()
	try:
		dict = ast.literal_eval(data)
		
	except StandardError:
		return "Error: Invalid data"
		
	dogs[dict["name"]] = dict
	
	dest()
	return "Post created successfully"

def delete(name):
	init()
	if name == "all":
		return "all"
	else:
		return name

def get(name):
	init()
	if name == "all":
		return dogs
	else:
		return dogs[name]

def update(name, data):
	init()
	return data
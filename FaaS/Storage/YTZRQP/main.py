import pickle
import ast
import os
import sys

ID = "YTZRQP"
db_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../Database/'))
db_path = os.path.join(db_base_path, (ID+'.pckl'))

dogs = {}

def init():
	global dogs
	try:
		with open(db_path, 'rb') as f:
			dogs = pickle.load(f)
			f.close()
		
	except IOError:
		dogs = {}

def dest():
	global dogs
	f = open(db_path, 'wb')
	pickle.dump(dogs, f)
	f.close()

def add(data):
	global dogs
	init()
	try:
		dict = ast.literal_eval(data)
		
	except StandardError:
		return "Error: Invalid data"
		
	dogs[dict["name"]] = dict
	
	dest()
	return "Post created successfully"

def delete(name):
	global dogs
	init()
	if name == "all":
		dogs = {}
	else:
		if name not in dogs:
			return "Name not found"
		del dogs[name]
	dest()
	return "Deleted successfully"

def get(name):
	global dogs
	init()
	if name == "all":
		return dogs
	else:
		if name not in dogs:
			return "Name not found"
		return dogs[name]

def update(name, data):
	global dogs
	init()
	return data
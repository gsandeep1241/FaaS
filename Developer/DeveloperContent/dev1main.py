import pickle

ID = "YTZRQP"
db_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../Database/'))
db_path = os.path.join(db_base_path, (ID+'.pckl'))

try:
	with open(db_path, 'rb') as f:
		dogs = pickle.load(f)
		f.close()
	
except IOError:
	dogs = {}

def add(data):
	return data

def delete(name):
	if name == "all":
		return "all"
	else:
		return name

def get(name):
	if name == "all":
		return "all"
	else:
		return name

def update(name, data):
	return data
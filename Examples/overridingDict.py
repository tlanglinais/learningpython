class GrumpyDict(dict):
	def __repr__(self):
		print("None of your business")
		return super().__repr__()
	
	def __missing__(self, key):
		print(f"{key} isn't here...")

	def __setitem__(self, key, value):
		print('You want to change the dictionary?')
		print('OK.....')
		super().__setitem__(key, value)

	def __contains__(self, item):
		print("It's not in here...")
		return False

data = GrumpyDict({'first': 'Tom', 'animal': 'cat'})
print(data)
data['city']
print(data)
'city' in data
def double(values):
	"""doubles the values in a list

	>>> double([1,2,3,4])
	[2, 4, 6, 8]
	
	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']
	"""
	return [2 * i for i in values] 
# class Counter:
# 	def __init__(self, low, high):
# 		self.low = low
# 		self.high = high

# 	# def __iter__(self):


# c = Counter(0, 10)
# iter(c)


class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration


for x in Counter(0, 10):
	print(x)
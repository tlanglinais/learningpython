import pdb

def divide(num, den):
	try:
		result = num/den
		pdb.set_trace()
	except ZeroDivisionError:
		print("Can't Divide by 0")
	except TypeError:
		print("a and b must be ints or floats")
	else:
		print(f"{num} divided by {den} is {result}")

divide(1,2)
divide('a', 2)
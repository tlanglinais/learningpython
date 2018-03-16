# from random import choice

# def make_laugh_func():
# 	def get_laugh():
# 		l = choice(('Ha', 'lol', '...'))
# 		return l
# 	return get_laugh

# laugh = make_laugh_func()
# print(laugh())

# def be_polite(fn):
# 	def wrapper():
# 		print('What a pleasure to meet you!')
# 		fn()
# 		print('Have a great day')
# 	return wrapper

# def greet():
# 	print('I forgot my own name...')


# greet = be_polite(greet)
# greet()
# print(type(greet))


# from functools import wraps
# def ensure_first_arg_is(val):
# 	def inner(fn):
# 		@wraps(fn)
# 		def wrapper(*args, **kwargs):
# 			if args and args[0] != val:
# 				return f"First arg needs to be {val}"
# 			return fn(*args, **kwargs)
# 		return wrapper
# 	return inner

# @ensure_first_arg_is('burrito')
# def fav_foods(*foods):
# 	print(foods)

# print(fav_foods('burrito', 'ice cream'))
# print(fav_foods('ice cream', 'burrito'))

def enforce(*types):
	def decorator(f):
		def new_func(*args, **kwargs):
			# convert args into something mutable
			newargs = []
			for (a, t) in zip(args, types):
				newargs.append(t(a))
			return f(*newargs, **kwargs)
		return new_func
	return decorator


@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a, b):
	print(a/b)

divide('1', '4')
import functools

def uppercase(func):
	"""Uppercase"""
	@functools.wraps(func)
	def wrapper():
		original = func()
		mod = original.upper()
		return mod
	return wrapper


def lowercase(func):
	"""Lowercase"""
	@functools.wraps(func)
	def wrapper():
		return func().lower()
	return wrapper


@uppercase
@lowercase
def hello_world():
	"""hello world function"""
	return "Hello_world"


def proxy(f):
	def wrapper(*args, **kwargs):
		return f(*args, **kwargs)
	return wrapper


def trace(func):
	def wrapper(*args, **kwargs):
		print("Trace: call: {}() with: {}, {}".format(func.__name__, args, kwargs))
		original = func(*args, **kwargs)
		print("Trace: {} return {}".format(func.__name__, original))
		return original
	return wrapper

@trace
def say(name, line):
	return "{}---{}".format(name, line)


if __name__ == "__main__":
	print(hello_world.__doc__)

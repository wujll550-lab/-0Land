import functools
import time


def log_time(func):
	"""Print the execution time of a function and return its result."""
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		start_time = time.perf_counter()
		try:
			return func(*args, **kwargs)
		finally:
			elapsed_time = time.perf_counter() - start_time
			print(f"{func.__name__} 执行耗时: {elapsed_time:.2f} 秒")

	return wrapper

import functools
import time


def retry(times=3, delay=1):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			for attempt in range(1, times + 1):
				try:
					return func(*args, **kwargs)
				except Exception:
					if attempt == times:
						raise
					print(f"重试第 {attempt} 次...")
					time.sleep(delay)

		return wrapper

	return decorator

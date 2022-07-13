cache = dict()


def check_cache(func):
	def wrapper(num):
		if num in cache:
			return cache[num]
		result = func(num)
		cache[num] = result
		return result
	return wrapper


@check_cache
def multiplier(number: int):
	return number * 2


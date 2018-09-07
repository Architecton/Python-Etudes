import itertools


# const: return generator that generates a stream of values n
def const(n):
	while True:
		yield n

# hd: return head of generator
def hd(generator):
	return list(itertools.islice(generator, 1))

# nats: return generator that generates natural numbers starting from n.
def nats(n):
	yield n
	yield from nats(n + 1)

# tl: returns the generator that results after removing the first element.
def tl(generator):
	list(itertools.islice(generator, 1))
	return generator

# map: returns the generator with function applied to each value generated
def map_gen(func, generator):
	return map(func, generator)

# take_n: take n elements from generator and return them in a list.
def take_n(n, generator):
	return list(itertools.islice(generator, n))

# filter: return generator that contains elemnts for which the function func returns True
def filter_gen(func, generator):
	return filter(func, generator)

# multiples: return generator that generates multiples of n.
def multiples(n):
	def multiples_aux(n, acc):
		yield acc
		yield from multiples_aux(n, acc + n)

	return multiples_aux(n, 0)

# concat: concatenate two generators and return result

# zip: take two generators and return a generator that alternatly returns element from each one.
def zip(generator_1, generator_2):
	def hd(generator):
		return list(itertools.islice(generator, 1))

	def zip_aux(generator_1, generator_2, fst):
		if fst == 0:
			yield hd(generator_1)[0]
			yield from zip_aux(generator_1, generator_2, 1)
		else:
			yield hd(generator_2)[0]
			yield from zip_aux(generator_1, generator_2, 0)

	return zip_aux(generator_1, generator_2, 0)

# zip_n: take two generators and return a generator that alternatingly returns n elements from each generator
def zip_n(n, generator_1, generator_2):
	def hd(generator):
		return list(itertools.islice(generator, 1))

	def zip_n_aux(generator_1, generator_2, left, total):
		if left > 0:
			yield hd(generator_1)[0]
			left -= 1
			if left == 0:
				yield from zip_n_aux(generator_1, generator_2, -total, total)
			else:
				yield from zip_n_aux(generator_1, generator_2, left, total)

		else:
			yield hd(generator_2)[0]
			left += 1
			if left == 0:
				yield from zip_n_aux(generator_1, generator_2, total, total)
			else:
				yield from zip_n_aux(generator_1, generator_2, left, total)
			
		
	return zip_n_aux(generator_1, generator_2, n, n)			

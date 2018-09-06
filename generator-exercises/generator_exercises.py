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

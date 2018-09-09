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

# unzip: take stream and return ordered pair of streams where the first stream contains the odd elements in stream and second stream even elements of stream.

# unzip_n: take stream and return ordered pair of streams where streams alternatingly contain elements of each stream.

# discard_n: return stream left after removing first n elements.
def discard_n(n, generator):
	itertools.islice(generator, n)
	return generator

# fold_n: perform fold on first n elements of list.


# fold_stream: perform fold operation on stream and return stream of accumulator values.

# rle: encode stream using the rle encoding algorithm. Return ordered pair (int * 'a).
# NOTE: A type with two quotation marks in front of it instead of one is an equality type, which means that the = operator works on it. 
# That also means that you can't call your function on things that are not equality types,  though.

# rle_decode: take a stream of ordered pairs (int * 'a) where the first element is the number of repetitions of element at second position and
# return a stream representing the decoded data (convert each ordered pair to n repetitions of elements and add to stream).

# The Sieve of Eratosthenes is possibly the oldest systematic method (algorithm) for generating the
# sequence of all prime numbers. The "sieve" can be described as follows:

# step 1: Generate the sequence of natural numbers starting at 2.
# step 2: Position yourself just before the beginning of the sequence.
# step 3: Find the next available number in the sequence. Write it down; it is prime.
# step 4: Cross out (delete) all multiples of the number identified in step 3.
# step 5: Continue with step 3.


# sieve: implement the Sieve of Eratosthenes. This function expects to be passed a stream of natural numbers starting with 2.
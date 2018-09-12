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
	next(generator)
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
	# Define auxiliary function that takes an additional parameter used for recursion.
	def multiples_aux(n, acc):
		yield acc 								# Yield accumulator value.
		yield from multiples_aux(n, acc + n) 	# Yield value with accumulator incremented by n (yielding sequence (n, n + n, n + n + n, ...)).

	return multiples_aux(n, 0)

# concat: concatenate two generators and return result
def concat(generator1, generator2): # itertools.chain() function does the same thing.
	for el in generator1:
		yield el
	for el in generator2:
		yield el

# zip: take two generators and return a generator that alternatly returns element from each one.
def zip(generator_1, generator_2):
	# Auxiliary function that returns the head of a generator.
	def hd(generator):
		next(generator)
	# Auxiliary function that contains an additional parameter used for recursion.
	def zip_aux(generator_1, generator_2, fst): # if fst == 1, yield from first generator. Else yield from second generator.
		if fst == 1:
			yield hd(generator_1)
			yield from zip_aux(generator_1, generator_2, 0) # Make recursive call with fst set to 0.
		else:
			yield hd(generator_2)
			yield from zip_aux(generator_1, generator_2, 1) # Make recursive call with fst set to 1.

	# Call auxiliary function.
	return zip_aux(generator_1, generator_2, 1)

# zip_n: take two generators and return a generator that alternatingly returns n elements from each generator
def zip_n(n, generator_1, generator_2):
	def hd(generator):
		return next(generator)

	# Define an auxiliary function that accepts additional parameters used for recursion.
	def zip_n_aux(generator_1, generator_2, left, total): # The parameter left represents how many more elements need to be yielded from the current generator.
		if left > 0: 									  # The parameter total represents the total number of elements to yield from each generator.
			yield hd(generator_1)
			left -= 1
			if left == 0:													  # If no more elements to be yielded from this generator...
				yield from zip_n_aux(generator_1, generator_2, -total, total) # ...make recursive call with left equal to negative total value.
			else:
				yield from zip_n_aux(generator_1, generator_2, left, total)   # Else make recursive call with new value of left.

		else:
			yield hd(generator_2)
			left += 1
			if left == 0: 													 # If no more elements to be yielded from this generator...
				yield from zip_n_aux(generator_1, generator_2, total, total) # ...make recursive call with left equal to negative total value.
			else:
				yield from zip_n_aux(generator_1, generator_2, left, total)  # Else make recursive call with new value of left.
			
	# Call auxiliary function.
	return zip_n_aux(generator_1, generator_2, n, n)

# discard_n: return stream left after removing first n elements.
def discard_n(n, generator):
	itertools.islice(generator, n)
	return generator


# odd_elements: function that returns a generator that generates odd elements of passed generator.
def odd_elements(generator):
	yield next(generator)
	next(generator)
	yield from odd_elements(generator)

# even elements: function that returns a generator that generates even elements of passed generator.
def even_elements(generator):
	next(generator)
	yield next(generator)
	yield from even_elements(generator)

# fold_n: perform fold on first n elements of list.
def fold_n(n, func, acc, generator):
	next_el = next(generator)
	if next_el == [] or n == 0: 			# If generator depleted or n == 0, return accumulator value.						
		return acc
	else:
		return func(next_el, fold_n(n - 1, func, acc, generator)) # Else make recursive call for accumulator value.

# fold_stream: perform fold operation on stream and return stream of accumulator values.
def fold(func, acc, generator):
	next_el = next(generator)
	if next_el == []: 			 # If generator depleted, yield accumulator value and end.
		yield acc
	else: 						 # Else get next generator value and yield it. Then make a recursive call for the rest of the generator
		acc = func(next_el, acc) # with the new accumulator value.
		yield acc
		yield from fold(func, acc, generator)

#############################################################################
# example of use of fold_n and fold
#
# nat_gen = nats(1)
# cum_sum_nats = fold(lambda el, acc : acc + el, 0, nat_gen)
#
# nat_gen = nats(1)
# sum_first_10_nats = fold_n(10, lambda el, acc : acc + el, 0, nat_gen)
#############################################################################

from more_itertools import peekable

# rle: encode stream using the rle encoding algorithm. Return generator of rle tuples.
# >>Ugly code warning<<
def rle_encode(generator):
	# rle_next: get next rle tuple (auxiliary function)
	def rle_next(generator):

		# encode next: encode next stream of elements in generator (auxiliary function)
		def encode_next(generator):
			next_el = next(generator, None) # Get next element in generator (None if generator is empty)
			if next_el == None:
				return None
			count = 1 						# Initialize occurrences counter.

			# Check if there are any more occurences of same element. StopIteration exception if generator is now empty.
			try:
				while(generator.peek() == next_el):
					count += 1
					next_el = next(generator)
			except StopIteration:
				pass
			finally:
				return (count, next_el)

		return encode_next(generator)

	# Check if generator has another element.
	try:
		generator = peekable(generator)
		generator.peek()
		# Yield next rle tuple.
		yield rle_next(generator)
		# Make recursive call.
		yield from test(generator)
	except StopIteration: 			# If generator exhausted, yield.
		pass


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
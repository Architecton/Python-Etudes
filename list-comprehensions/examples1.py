# Make a list of of words that are palindromes ###########################################
words = ["kajak", "Sara", "jabolko", "coffee", "Anna"]

# is_palindrome: check if a word is a palindrome
def is_palindrome(word):
	word = word.lower()
	return word == word[::-1]

palindromes = [word for word in words if is_palindrome(word)]

##########################################################################################

# Construct a function that returns a list of prime numbers in natural numbers up to n ###
def list_primes(n):
	import math
	# is_prime: check if number num is prime
	def is_prime(num):
		for el in range(2, math.ceil(math.sqrt(num)) + 1):
			if num % el == 0:
				return False
		return True

	return [num for num in range(2,n + 1) if is_prime(num)]

##########################################################################################

# Construct a function that returns a list of n occurences of element el #################

def expand(n, el):
	return [el for i in range(n)]

##########################################################################################

# Construct a function that returns a list of first n odd integers #######################
def n_odd(n):
	return [el for el in range(1, n*2) if el % 2 != 0]

##########################################################################################

# Construct a function that returns a list of first n even integers ######################

def n_even(n):
	return [el for el in range(1, n*2 + 1) if el % 2 == 0]

##########################################################################################

# Construct a function that takes a list of lowercase letters and returns a list of same letters in uppercase.S
def chars_to_upper(char_list):
	return [el.upper() for el in char_list]

## using map: ##

# list(map(lambda el : el.upper(), char_list))

##########################################################################################
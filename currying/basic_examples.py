# curry: take function and value of first argument. Return function that takes the
# second element to produce the final result (decompose binary function into two unary functions)
def curry(func, var):
    def res(y): 			# the curried function is the passed function with argument var substituted for the first argument.
        return func(var, y)
    return res 				# Return the curried function.



# Example of use ###################

# add: return a + b
def add(a, b):
	return a + b

# Convert a general function like add to a more specialized function that adds a number to 10 by currying.
add_to_10 = curry(add, 10)

# Test resulting function.
print(add_to_10(5))
####################################





# Using the partial function from functools
from functools import partial

# add_to_20: curried function add with first argument substituted with 20.
add_to_20 = partial(add, 20)

# return_sum: curried function with first argument of add_to_20 substituted with 80.
# This function takes no arguments (unit argument) and returns a constant value of 80.
return_sum = partial(add_to_20, 80)

###########################################################
# Nice example from dataquest.io (Spiro Sideris)
###########################################################
# A partial that grabs IP addresses using
# the `map` function from the standard library.
#
# extract_ips = partial(
#    map,
#    lambda x: x.split(' ')[0]
# )
# lines = read('example_log.txt')
# ip_addresses = list(extract_ip(lines))
###########################################################
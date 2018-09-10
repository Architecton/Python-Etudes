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
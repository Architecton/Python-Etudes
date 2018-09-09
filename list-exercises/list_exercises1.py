# Write a function that reverses a list
def reverse(l):
	return l[::-1]

# Write a function that checks if a list is a palindrome
def is_palindrome(l):
	return l == l[::-1]

# Write a function that returns every n-th element in the list
def every_nth(l):
	return l[::n]

# Write a function that checks if all elements in a list are equal
def all_equal(l):
	if l == []: 				# If list is empty, return True.
		return True
	else: 						# Else, compare each element in list to first element.
		reference = l[0]
		for el in l:
			if el != reference: 	# If any element does not equal the first element, return false.
				return False

		return True

# Write a function that returns a list of elements el of length n
def expand(el, n):
	result = [] 			# empty container list
	for i in range(n): 		# append n occurrences of element el to container
		result.append(el)
	return result 			# Return result

# Write a function sum_list which returns the sum of all the integers in the list xs
def sum_list(l):
	acc = 0 		# Initialize accumulator
	for el in l: 	# Go over elements in list and add them to accumulator.
		acc += el
	return acc 		# return accumulator. # NOTE: built-in function sum accomplished the same thing.

# Construct a function is_sorted_asc which returns true if the list of integers xs is sorted in ascending order
def is_sorted_asc(l):
	for i in range(len(l) - 2):	# Go from first element to second from last.
		if l[i + 1] < l[i]: 	# If any element is lesser than the precedi
			return False
	return True

# Construct a function is_sorted_desc which returns true if the list of integers xs is sorted in descending order.
def is_sorted_desc(l): 			# Similar
	for i in range(len(l) - 2):
		if l[i + 1] > l[i]:
			return False
	return True


# Construct a function intersection which returns a list of elements that are both in list of integers xs and list of integers ys
def intersection(l1, l2):
	result = []
	for el1 in l1:
		for el2 in l2:
			if el1 == el2:
				result.append(el1)
	return result


# Construct a funtion difference which returns a list of integers that are in xs but not also in ys
def difference(l1, l2):
	result = []
	for el1 in l1:
		for el2 in l2:
			if el1 == el2:
				break
		result.append(el1)
	return result

# Construct a function that returns the union of two lists (think of them as sets)
def union(l1, l2):
	# Auxiliary function contains - return true if list l contains element el.
	def contains(el, l):
		# Go over elements and compare to el.
		for e in l:
			if e == el:
				return True
		return False

	# Go over elements in l1. If element not found in l2, append.
	for el in l1:
		if not contains(el1, l2):
			l2.append(el1)

	return l2


# Construct a function that returns the symmetric difference of two lists
def symmetric_diff(l1, l2):
	diff1 = difference(l1, l2) # Symmetric differnece is the union of S1 \ S2 and S2 \ S1.
	diff2 = difference(l2, l1)
	return union(diff1, diff2)

# construct a function right which returns the element which is to the right of element el
def right_of(el, l):
	# Exception for signaling that there is no element el or no right element of el
	class EmptyException(Exception):
		pass

	# Go over elements in list.
	for i in range(len(l)):
		# If element same as el, check if right element exists.
		if l[i] == el:
			if i == len(l) - 1:
				return EmptyException
			else:
				return l[i + 1]
	raise EmptyException 		# Else raise exception.
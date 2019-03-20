import abc

# Abstract class that specifies the functionality that must be implemented by a linked list.
class Linked_list_abstract(abc.ABC, metaclass = abc.ABCMeta):
	
	# Check if linked list is empty
	@abc.abstractmethod
	def is_empty(self):
		''' data '''

	@abc.abstractmethod
	def first(self):
		''' data '''

	@abc.abstractmethod
	def last(self):
		''' data '''

	@abc.abstractmethod
	def nth(self, n):
		''' data '''

	@abc.abstractmethod
	def add(self, n, el):
		'''data'''

	@abc.abstractmethod
	def remove(self, n):
		''' data '''

# Node: represents a node in a linked list
class Node():
	def __init__(self, element):
		self.element = element
		self.next = None
	

# Linked_list: linked list implementation
class Linked_list(Linked_list_abstract):

	# Constructor: construct empty linked list with length 0 and head pointing to None.
	def __init__(self):
		self._length = 0
		self._head = None

	# is_empty: return True if linked list is empty, else return false.
	def is_empty(self):
		return self._length == 0

	# first: get first element in linked list.
	def first(self):
		return self._head

	# last: get last element in linked list.
	def last(self):
		current_node = self._head 					# Set current_node to head.
		if current_node == None: 					# If linked list is empty (head is None), return None.
			return None
		else: 										# While not reaching last element (while next pointer is not None)...
			while(current_node.next != None): 		# Go to next node.
				current_node = current_node.next
		return current_node.element 				# Return value stored in last node.

	# nth: get nth element in list.
	def nth(self, n):
		res_node = self._head 						# set res_node to head of linked list.
		if res_node == None: 						# if linked list is empty (head is None), return None
			return None

		for i in range(n):							# Traverse list to nth node.
			res_node = res_node.next
			if res_node == None: 					# If index over edge, return None.
				return None
		return res_node.element 					# Else return value stored in nth node.

	# add: add element el to position n in linked list.
	def add(self, n, el):
		new_node = Node(el) 						# Create new Node containing specified value.

		if self._head == None: 						# If linked list empty, make new_node new head.
			self._head = new_node
			self._length += 1 						# Increment linked list length.
		elif n == 0: 								# If adding element to head...
			prev = self._head 						# ...Relink and increment length.
			self._head = new_node
			self._head.next = prev
			self._length += 1
		else:
			prev = self._head						# Else iterate to one Node before the spot at which to insert the new Node.
			for i in range(n - 1):
				if prev.next == None:				# If index over edge, add as last Node in linked list.
					prev.next = new_node
					return
				else:
					prev = prev.next
				
			new_node.next = prev.next 				# Relink and increment length.
			prev.next = new_node
			self._length += 1

	# remove: remove nth element from linked list.
	def remove(self, n):
		if n == 0: 									# If removing head...
			if self._head == None: 					# If linked list is empty, return None.
				return None
			else:
				self._head = self._head.next 			# Else relink head pointer and decrement length.
				self._length -=1
		else:
			prev = self._head 						# Else traverse to one Node before the Node that is to be deleted.
			if prev == None:						# If linked list empty, return None.
				return None
			else:
				for i in range(n - 1):
					prev = prev.next
					if prev.next == None: 			# If index over edge, return None.
						return None

			if prev.next == None:
				return None
			else:
				prev.next = prev.next.next 			# Relink linked list by skipping over the Node after prev.
				self._length -= 1					# Decrement length.

	# to_list: convert this linked_list to a Python list.
	def to_list(self):
		next_el = self._head 			# Start at head.
		result = [] 					# Define list for storing the elements.
		while(next_el != None): 		# While end of linked list has not been reached...
			result += [next_el.element] # ...add element stored in next Node to list.
			next_el = next_el.next 		# Go to next Node.

		return result 					# Return resulting list.

	#
	def __len__(self):
		return self._length
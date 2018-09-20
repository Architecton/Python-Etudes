import abc

# Abstrack class that specifies methods that must be implemented by an inheriting class.
class Stack(abc.ABC, metaclass = abc.ABCMeta):

	@abc.abstractmethod
	def is_empty(self):
		''' data '''

	@abc.abstractmethod
	def push(self):
		''' data '''

	@abc.abstractmethod
	def pop(self):
		''' data '''

	@abc.abstractmethod
	def peek(self):
		''' data '''

# Stack implementation using a list.
class List_stack(Stack):

	# Constructor
	def __init__(self):
		self._l = []

	# Parent abstract class method implementations.
	def is_empty(self):
		if self._l == []:
			return True
		else:
			return False

	def push(self, el):
		self._l.append(el)

	def pop(self):
		if self._l == []:
			return None
		else:
			return self._l.pop()

	def peek(self):
		if self._l == []:
			return None
		else:
			return self._l[-1]
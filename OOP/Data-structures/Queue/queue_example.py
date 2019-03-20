import abc

# Abstract class that specifies the methods that must be implemented by an inheriting class.
class Queue(abc.ABC, metaclass = abc.ABCMeta):

	@abc.abstractmethod
	def is_empty(self):
		'''data'''

	@abc.abstractmethod
	def enqueue(self):
		'''data'''

	@abc.abstractmethod
	def dequeue(self):
		'''data'''

	@abc.abstractmethod
	def peek(self):
		'''data'''



# Implementation of the abstract class
class List_queue(Queue):

	# Constructor
	def __init__(self):
		self._l = []

	# Implementing abstract methods specified by the parent abstract class.
	def is_empty(self):
		return self._l == []

	def enqueue(self, el):
		self._l = [el] + self._l

	def dequeue(self):
		if self._l == []:
			return None
		else:
			return self._l.pop()
		
		

	def peek(self, el):
		return self._l[-1]
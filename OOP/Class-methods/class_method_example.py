# Rectangle class
class Rectangle:

	# Class constructor
	def __init__(self, width, height):
		self.width = width
		self.height = height

	# area: compute area of rectangle.
	def area(self):
		return self.width * self.height

	# Make a class method that is used to create a square (special instance of a rectangle)
	@classmethod
	def new_square(cls, side_length):
		return cls(side_length, side_length)

# Create a new Rectangle instance by calling the new_square class method.
square = Rectangle.new_square(5)

# Print computed area.
print(square.area())
# class A
class A():
    def __init__(self, l):
        self._chars = l

    # add_char: add an alphabetical character to _chars list.
    def add_char(self, char):
        if char.isalpha() and len(char) == 1:
            self._chars.append(char)
        else:
            raise ValueError(str(char) + " is not an alphabetical ASCII character.")
        
    # Static method that checks if character char is in list l.
    @staticmethod
    def contains(char, l):
        # Make a linear search in list l for char
        for el in l:
            if el == char:
                return True

        return False

    @property
    def chars(self):
        print("getter invoked.")
        return self._chars
    

# Create list of characters.
l = ['b', 'c', 'a', 'd', 'g']

# Check if list contains character 'a' using the static method of class A.
if A.contains('a', l):
    test = A(l)         # If it does contain 'a', create new instance of A.

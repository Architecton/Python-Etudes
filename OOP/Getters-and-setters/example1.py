# Define a class A
class A:

    def __init__(self):
        self._a = 1

    # the @property decorator calls the function a when accessing the attribute instance.a
    @property
    def a(self):
        return self._a

    # Same as:
    # def a(self):
    #   return self.__a
    # a = property(a)
    #
    
    # the @a.setter property allows us to implement a setter.
    @a.setter
    def a(self, value):
        # Do things...
        print('Setting value of a...')
        self.a_a = value

    # Same as:
    # def a(self, value):
    #   self._a = value
    # a = property(a).getter(a)
    #
    #


    # Similar for getters.
    @a.getter
    def a(self):
        # Do things...
        print('Getting value of a...')
        return self._a

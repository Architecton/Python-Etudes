"""
There is a saying in computer science that a class is “data with opera‐
tions attached” while a closure is “operations with data attached.” In
some sense they accomplish much the same thing of putting logic
and data in the same object. But there is definitely a philosophical
difference in the approaches, with classes emphasizing mutable or
rebindable state, and closures emphasizing immutability and pure
functions. Neither side of this divide is absolute-at least in Python
-but different attitudes motivate the use of each.
"""

# A class that creates callable adder instances
class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, m):
        return self.n + m

add5_i = Adder(5)
print(add5_i(10))
add5_i.n = 10
print(add5_i(10))


# Writing the same thing using a closure
def make_adder(n):
    return lambda m: n + m

add_f = make_adder(5)
print(add_f(10))

"""
There is a little "gotcha" about how Python binds variables in clo‐
sures. It does so by name rather than value, and that can cause con‐
fusion, but also has an easy solution. For example, what if we want
to manufacture several related closures encapsulating different data:
"""

# Demonstration of the problem

adders = []
for k in range(5):
    adders.append(lambda m: m + k)  # k in the lambda expression is bound to the value
                                    # of variable k in the current scope.

print([adder(10) for adder in adders])

# Solution

adders1 = []
for k in range(5):
    adders1.append(lambda m, k=k: m + k)

print([adder(10) for adder in adders1])

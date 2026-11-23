# Graph for constant time complexity
import matplotlib.pyplot as p

p.title('Constant Complexity')
p.xlabel('Input Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [1 for y in x]

p.plot(x, y, 'b', label='O(1)')
p.legend()
p.show()

# Graph for Linear time complexity
import matplotlib.pyplot as p

p.title('Linear Complexity')
p.xlabel('Input size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [y for y in x]

p.plot(x, y, 'r', label='O(n)')
p.legend()
p.show()

# Graph for Quadratic time complexity
import matplotlib.pyplot as p

p.title('Quadratic Complexity')
p.xlabel('Inputs size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [y**2 for y in x]

p.plot(x, y, 'g', label='O(n**2)')
p.legend()
p.show()

# Graph for Logarithmic time complexity
import matplotlib.pyplot as p
import math as m

p.title('Logarithmic Complexity')
p.xlabel('Inputs size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [m.log(y) for y in x]

p.plot(x, y, 'g', label='O(log(n))')
p.legend()
p.show()

# Graph for Exponential time complexity
import matplotlib.pyplot as p

p.title('Exponential Time Complexity')
p.xlabel('Inputs size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [2**y for y in x]

p.plot(x, y, 'r', label='O(2**n)')
p.legend()
p.show()
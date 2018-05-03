###############################################################################
# PH 150
# Kyle West
# Lab 1 Python Code
###############################################################################
import numpy as np
import matplotlib.pyplot as plt

def output(ans, goal):
   print("\t",goal, "=>", ans)

# -----------------------------------------------------------------------------
# P1.1 
# Read chapter 1 in the python book, performing all the prescribed tasks.
# -----------------------------------------------------------------------------
print("P1.1")
print(
"""
\tI have been developing in Python for about 3 years. I felt pretty good about the
\tbook, and have chosen not to do the problems because of their trivial nature. 
"""
)




# -----------------------------------------------------------------------------
# P1.2
# Read sections 3.1(integers),3.2(floats), and 4.2(importing libraries) in the
# python book, performing all example calculations. Then performthe following
# calculations:
# -----------------------------------------------------------------------------
print("P1.2")

# P1.2 (a) 
goal = "5*cos2(23deg) + e^10"
ans = 5.0 * np.cos(np.radians(23.0))**2 + np.e**10
output(ans, goal)

# P1.2 (b) 
goal = "5 * sqrt(50) * 67^(2/3)"
ans = 5.0 * np.sqrt(50.0) * 67.0**(2/3.0)
output(ans, goal)

# P1.2 (c)
goal = "5*cosh(20) + 8*sinh(9)"
ans = 5.0*np.cosh(20.0) + 8.0*np.sinh(9.0)
output(ans, goal)




# -----------------------------------------------------------------------------
# P1.3
# Read section 3.5(lists) and 4.1(native functions) in the python book, performing
# all of the example calculations. Then performthe following calculations:
# -----------------------------------------------------------------------------
print("\nP1.3")

# P1.3 (a) 
goal = "Sum of first 10 primes"
ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
output(sum(ans), goal)

# P1.3 (b) 
goal = "Sum of first 11 primes"
ans.append(31)
output(sum(ans), goal)

# P1.3 (c) 
goal = "3 thru 54 by threes"
ans = list(range(3, 55, 3))
output(ans, goal)

# P1.3 (d) 
goal = "Sum of those ^^^ numbers"
output(sum(ans), goal)




# -----------------------------------------------------------------------------
# P1.4
# Read section chapter 6(loops) in the python book, performing all example
# calculations. Then performthe following:
# -----------------------------------------------------------------------------
print("\nP1.4")

# P1.4 (a) 
goal = "Look for multiples of 5"
ans = "Below 101:"
output(ans, goal)
for i in range(2, 102, 2):
   if i % 5 == 0:
      print("\t\tFiver:", i)

# P1.4 (b) 
goal = "Find numerically the sum of n((3/4)^n) where n -> 1:1000"
ans = sum(list([n*((3/4.0)**n) for n in range(1,1001)]))
output(ans, goal)




# -----------------------------------------------------------------------------
# P1.5
# Read section chapter 6(loops) in the python book, performing all example
# calculations. Then performthe following:
# -----------------------------------------------------------------------------
print("\nP1.5")

# P1.5 (a) 
def some_function(a):
   # P1.5 (b) 
   tmp = range(4, a, 3)
   # P1.5 (c) 
   b = sum(tmp)
   # P1.5 (d) 
   return np.sqrt(b)

# P1.5 (e) 
output(some_function(7), "Test our function with a as 7")
output(some_function(15), "Test our function with a as 15")
output(some_function(25), "Test our function with a as 25")
output(some_function(1234), "Test our function with a as 1234")
output(some_function(54399), "Test our function with a as 54399")




# -----------------------------------------------------------------------------
# P1.6
# Read section chapter 6(loops) in the python book, performing all example
# calculations. Then performthe following:
# -----------------------------------------------------------------------------
print("\nP1.6")

# P1.6 (a) 
x = np.linspace(0, 3, 100)
y = np.sin(x**2) * np.e**(-x)

# P1.6 (b) 
plt.plot(x, y, 'r--')

# P1.6 (c)
plt.xlabel('X axis label')
plt.ylabel('Y axis label')

# P1.6 (d)
plt.title('Title goes here')

# P1.6 (e)
filename = 'lab1_P1.6e.png' 
plt.savefig(filename)

output(filename,"Plot found in")

# solve the quadratic equation: a * x**2 + b * x + c = 0

# import square root method from math module
from math import sqrt

# let the user enter the real parameters


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# calculate delta
d = b ** 2 - 4 * a * c

# find the solutions and output them to the screen
if d > 0:
    sol1 = (-b - sqrt(d)) / (2 * a)
    sol2 = (-b + sqrt(d)) / (2 * a)
    print("The solutions are", sol1 , "and", sol2)
elif d == 0:
    sol = -b / (2 * a)
    print("The solution is", sol)
else:
    print("There are no real solutions.")


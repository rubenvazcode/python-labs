'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
# import math library
import math
# Define radius
r = 3.14
# define height
h = 5
# calculate surface area of the cylinder
surface = (math.pi * (r ** 2))
print("The surface area is:",surface)
# calculate cylinder volume
print("The volume is:", (surface * h))
# calculate the sum of all surfaces areas
# calculate perimeter
p = (2 * math.pi * r)
# define variable to all sufaces
print("The area of all surfaces of the cylinder is:",(2 * surface) + (p * h))

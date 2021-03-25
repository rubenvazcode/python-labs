'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# convert an int to a float
x = 17
x = float(x)
print(x)
print(type(x))

# convert an float to a int
y = 2.7
y = int(y) # by converting this the number will be imprecise since we lost 0.7 of the value.
print(y)
print(type(y))

# Perform floor division using a float and an int.
print(x // y) # by doing this operation we can have a result far from from the real result.


# Use two user inputted values to perform multiplication.
n1 = float(input("Please enter first number for the multiplication: "))
n2 = float(input("Please enter second number for the multiplication: "))
r = (n1 * n2)
print("The result of the multiplication is : ", r)

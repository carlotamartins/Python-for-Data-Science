#Exercise 12: Define a function
print("------------------------\n")

def greet(name):
    return f"Hello, {name}"

print(greet("Carlota"))

#Printed output:
# Hello, Carlota




#Exercise 13: Function with Return Value
print("------------------------\n")

def square(number):
    return number**2

print(f"The square of 4 is : {square(4)}")
print(f"The square of 12 is: {square(12)}")

#Printed output:
# The square of 4 is : 16
# The square of 12 is: 144




#Exercise 14: Function with Default Parameters
print("------------------------\n")

def multiply(a, b = 1):
    return a*b

print(f"The product between 8 and 7 is: {multiply(8, 7)}")
print(f"The product between 8 and the default value of b is: {multiply(8)}")

#Printed output:
#The product between 8 and 7 is: 56
#The product between 8 and the default value of b is: 8


print("------------------------\n")

def fizzbuzz(n):
    if n%3 == 0 and n%5 != 0:
        return "Fizz"
    elif n%3 !=0 and n%5 == 0:
        return "Buzz"
    elif n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    else:
        return n

#Defining a counter that will print the function until reaching 20
counter = 1
while counter <= 20:
    print(fizzbuzz(counter))
    counter += 1

# Printed output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
def fizzbuzz(n):
    if n%3 == 0 and n%5 != 0:
        return "Fizz"
    elif n%3 !=0 and n%5 == 0:
        return "Buzz"
    elif n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    else:
        return n


counter = 1
while counter <= 20:
    print(fizzbuzz(counter))
    counter += 1

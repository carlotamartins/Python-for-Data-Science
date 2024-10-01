#Exercise 8: Conditional Statements
print("------------------------\n")

#Asking the user for a number and tranforming it into a float
user_input = input("Insert a number: ")
number = float(user_input)

#Checking if it's negative, positive or zero
if number > 0 :
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
elif number == 0:
    print("The number is zero.")




#Exercise 9: For Loop
print("------------------------\n")

#Creating the list
list = [1, 2, 3, 4, 5]

#Creating the for loop
for number in list:
    print(number)




#Exercise 10: While loop
print("------------------------\n")

#Defining the variable that will go through every number from 1 to 5
i = 1

#Defining the loop and incrementing 1 to i every time
while i<=5:
    print(i)
    i += 1



#Exercise 11: Match statement
print("------------------------\n")

#Creating the variable
grade = input("Insert a grade (A, B, C, D or F): ")

#Creating the match statement
match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Good job!")
    case "C":
        print("Fair.")
    case "A":
        print("Needs improvement.")
    case "A":
        print("Failing.")
    case _:
        print("Invalid input. Error.")


print("------------------------\n")

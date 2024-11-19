#Exercise 15: List Comprehension
print("------------------------\n")

#Creating a list from 1 to 10
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Creating a list that has the square number of every element in the previous list
squared_list = [number**2 for number in list] 

print(f"The new list that has the squared number for every element of the previous one is: {squared_list}")

#Printed output:
#The new list that has the squared number for every element of the previous one is: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]




#Exercise 16: Nested Data Structures
print("------------------------\n")
 
#Creating the dictionary with different students and corresponding lists of grades
grades = {"Carlota": [20, 15, 13, 10], "João": [20, 14, 15, 13], "Catarina": [8, 13, 15, 16], "Marta": [6, 12, 15, 16]}

#Defining the function
def average_grade(grades_dictionary):
    for student, grades in grades_dictionary.items():
        # Calculating the average grade
        average = sum(grades) / len(grades)  
        print(f"{student}: Average Grade = {average}")

print(average_grade(grades))

#Printed output:
# Carlota: Average Grade = 14.5
# João: Average Grade = 15.5
# Catarina: Average Grade = 13.0
# Marta: Average Grade = 12.25




#Exercise 17: Simple Calculator
print("------------------------\n")

#Defining the three-parameter funciton
def calculate(a, b, parameter):
    if parameter == "+":
        return a + b
    elif parameter == "-":
        return a - b
    elif parameter == "/":
        return a / b
    elif parameter == "*":
        return a * b
    

#Asking the user for inputs
user_input_a = float(input("Enter the first number: "))
user_input_b = float(input("Enter the second number: "))
user_input_parameter = input("Enter the parameter (+, -, / or *): ")

#Printing the final result
print(f"The result is {calculate(user_input_a, user_input_b, user_input_parameter)}")

#Printed output:
# Enter the first number: 3
# Enter the second number: -9
# Enter the parameter (+, -, / or *): *
# The result is -27.0


print("------------------------\n")

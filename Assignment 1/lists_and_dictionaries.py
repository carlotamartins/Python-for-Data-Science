#Exercise 4: Lists
print("------------------------\n")

universities = ["Nova", "Esade", "ISEG", "LSE", "Harvard", "IE"]

print(f"The list is the following: {universities}")

print(f"The first item of the list is {universities[0]}")
print(f"The last item of the list is {universities[-1]}")

#Printed output:
#The list is the following: ['Nova', 'Esade', 'ISEG', 'LSE', 'Harvard', 'IE']
#The first item of the list is Nova
#The last item of the list is IE




#Exercise 5: Dictionaries
print("------------------------\n")

students = {"name": "Jorge", "age": 21, "grade": 10}

for characteristic, value in students.items():
    print(f"{characteristic}: {value}")

#Printed output: 
#name: Jorge
#age: 21
#grade: 10
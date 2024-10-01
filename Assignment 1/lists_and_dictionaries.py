#Exercise 4: Lists
print("------------------------\n")

universities = ["Nova", "Esade", "ISEG", "LSE", "Harvard", "IE"]

print(universities)

print(f"The first item is {universities[0]}")
print(f"The last item is {universities[-1]}")


#Exercise 5: Dictionaries
print("------------------------\n")

students = {"name": "Jorge'", "age": 21, "grade": 10}

for characteristic, value in students.items():
    print(f"{characteristic}: {value}")
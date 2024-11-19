#Creating a mixed list
characteristics = ["Carlota", 21, 1.68, "Maribel", 63, 1.65, "Diogo", 21, 1.54]


#Creating a new list where only the integers are present and printing it
filtered_list = [item for item in characteristics if isinstance(item, int)]
print(f"The list that contains only the integers from the original list is: {filtered_list}")

#Printed output:
#The list that contains only the integers from the original list is: [21, 63, 21]
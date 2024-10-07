#Creating a mixed list
characteristics = ["Carlota", 21, 1.68, "Maribel", 63, 1.65, "Diogo", 21, 1.54]


#Creating a new list where only the integers are present and printing it
filtered_list = [item for item in characteristics if isinstance(item, str)]
print(filtered_list)
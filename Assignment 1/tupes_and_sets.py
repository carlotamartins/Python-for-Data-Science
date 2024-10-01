#Exercise 6: Tuples
print("------------------------\n")

    #Creating the tuple and printing it
coordinates = (125, 4839)
print(f"The coordinates are: {coordinates}")

    #Acessing the coordinates
print(f"X: {coordinates[0]}")
print(f"Y: {coordinates[1]}")






#Exercise 7: Sets
print("------------------------\n")

    #Defining set
colors = {"Red", "Green", "Blue"}

    #Adding a new color
colors.add("Pink")

    #Adding an already existing color and observing
colors.add("Red")
print(colors)

    #Removing a color
colors.discard("Green")
print(colors)


#Creating a new set and merging it
light_color = {"Magenta", "Black", "Grey"}

merged_set = colors.union(light_color)
print(merged_set)


print("------------------------\n")

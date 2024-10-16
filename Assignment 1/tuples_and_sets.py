#Exercise 6: Tuples
print("------------------------\n")

    #Creating the tuple and printing it
coordinates = (125, 4839)
print(f"The coordinates are: {coordinates}")

    #Acessing the coordinates
print(f"X: {coordinates[0]}")
print(f"Y: {coordinates[1]}")

#Printed output: 
# The coordinates are: (125, 4839)
# X: 125
# Y: 4839




#Exercise 7: Sets
print("------------------------\n")

    #Defining set
colors = {"Red", "Green", "Blue"}

    #Adding a new color
colors.add("Pink")

    #Adding an already existing color and observing
colors.add("Red")
print(f"The current set is {colors}")

    #Removing a color
colors.discard("Green")
print(f"The current set after removing the color green is {colors}")


#Creating a new set and merging it
light_color = {"Magenta", "Black", "Grey"}

merged_set = colors.union(light_color)
print(f"The final set after the merge is {merged_set}")

#Printed output: 
# The current set is {'Red', 'Pink', 'Green', 'Blue'}
# The current set after removing the color green is {'Red', 'Pink', 'Blue'}
# The final set after the merge is {'Pink', 'Grey', 'Black', 'Blue', 'Red', 'Magenta'}


print("------------------------\n")

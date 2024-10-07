#Defining the function

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

#Testing for 22ºF, 46ºF, 51ºF and 76ºF by reversing the calculation

fahrenheit_temps = [22, 46, 51, 76]

#Buiding a for loop to print all the elements in the list
for fahrenheit in fahrenheit_temps:
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F was converted from {celsius:.2f}°C, as the funcion celsius_to_fahrenheit indicates from performing the calculation again: {celsius_to_fahrenheit(celsius)}°F")
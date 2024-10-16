#Defining the function

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

#Testing for 22ºF, 46ºF, 51ºF and 76ºF by reversing the calculation

fahrenheit_temps = [22, 46, 51, 76]

#Buiding a for loop to print all the elements in the list
for fahrenheit in fahrenheit_temps:
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F was converted from {celsius:.2f}°C, as the funcion celsius_to_fahrenheit indicates from performing the calculation again: {celsius_to_fahrenheit(celsius)}°F")

#Printed output: 
# 22°F was converted from -5.56°C, as the funcion celsius_to_fahrenheit indicates from performing the calculation again: 22.0°F
# 46°F was converted from 7.78°C, as the funcion celsius_to_fahrenheit indicates from performing the calculation again: 46.0°F
# 51°F was converted from 10.56°C, as the funcion celsius_to_fahrenheit indicates from performing the calculation again: 51.0°F
# 76°F was converted from 24.44°C, as the funcion celsius_to_fahrenheit indicates from performing the calculation again: 76.0°F
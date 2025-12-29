 # This is meant for converting one temperature value to the other


import math

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

print(1, "Fahrenheit to Celsius")
print(2, "Celsius to Fahrenheit")
print(3, "Kelvin to Fahrenheit")
print(4, "Kelvin to Celsius")
print(5, "Fahrenheit to Kelvin")
print(6, "Celsius to Kelvin")

try:
    option = int(input("Enter your option: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    if option == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
    elif option == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
    elif option == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K is {kelvin_to_fahrenheit(kelvin)}°F")
    elif option == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K is {kelvin_to_celsius(kelvin)}°C")
    elif option == 5:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_kelvin(fahrenheit)}K")
    elif option == 6:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_kelvin(celsius)}K")
    elif option >= 7:
        print("Invalid option. Please try again.")



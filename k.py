import math
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Temperature Calculator")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = int(input("Enter your choice: "))

if choice == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")






import math
name = "Andy Miranda"
age = 23
height = 5.9
favorite_color = "Red"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"Hello: {name}, my age is {age:05d}, my height is {height:.2f}, my favorite color is {favorite_color}!")

print(f"""Name: {name}
age: {age}
height: {height:.2f}
favorite_color: {favorite_color}
""")

# r = int(input("Enter a circle radius:"))
r = 5
circle_area = math.pi * r**2
print (f"Cicle Area with radius {r} is {circle_area:.1f}")

print(f"Square root of my age is: {math.sqrt(age)}")

print(f"sin of height: {math.sin(height)}, cos of height: {math.cos(height)}")

print(f"Sum of the age and 5: {age + 5}")
print(f"Difference between my height and 4 is: {height - 4}")
print(f"Product of my age and height is: {age * height}")
print(f"Quotient of my height and 2 is: {height / 2}")
print(f"Remainder of my age divided by 3 is: {age % 3}")
print(f"My age raised to the 2 power is: {age**2}")


temp_farenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (temp_farenheit - 32) * 5/9
print(f"Temp Fareheit {temp_farenheit} in Celsius is {celsius}°C")


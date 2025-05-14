#User input for Arithmetic Operations
a = int(input("Enter a number"))
b = int(input("Enter another number"))

#Arithmectic Operators
print(f"Addition is: {a + b}")
print(f"Subtraction is: {a - b}")
print(f"Multiplication is: {a * b}")
print(f"Division is: {a / b}")
print(f"Floor Division is: {a // b}")
print(f"Modulus is: {a % b}")
print(f"Exponent is: {a ** b}")

#User input for Boolean Operations
condition1 = input("Enter True or False for condition1: ").strip().lower() == 'true'
condition2 = input("Enter True or False for condition2: ").strip().lower() == 'true'

# Logical operations
print(f"AND: {condition1 and condition2}")
print(f"OR: {condition1 or condition2}")
print(f"NOT of Condition 2: {not condition2}")
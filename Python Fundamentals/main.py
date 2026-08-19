# 1. Variables:
name = "Alice"
age = 25
height = 5.6

# 2. Data Types:
print(type(10))
# Output: <class 'int'>
print(type("Hello")) # Output: <class 'str'>

# 3. Typecasting:
# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int)  
# Convert integer to string
num = 25
num_str = str(num)
print(num_str)  
# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int) 

# 4. input() Function:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")

# 5. Comments, Escape Sequences & Print Statement:

# Comments:
# This is a single-line comment
'''
This is a
multi-line comment
'''

# Escape Sequences:
print("Hello\nWorld!")
print("This is a tab\tcharacter.")

# Print Statement
print("Hello", "World", sep=", ", end="!\n")

# 6. Operators:
# Arithmetic Operators
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)
print(10 % 2)
print(10 ** 2)

# Assignment Operators
x = 10 
x += 5
print(x)  

# Comparison Operators
print(10 > 5)  
print(10 == 5) 

# Logical Operators: 
print(True and False)  
print(True or False)  
print(not True)

# Membership Operators: 
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  

# Identity Operators:
x = 10
y = 10
print(x is y)  
 
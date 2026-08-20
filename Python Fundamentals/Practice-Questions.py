# Python Basics - Practice Set
# This set is based on the topics we’ve covered so far: installation, syntax, variables, typecasting, user input, comments, and operators.
# Try to solve each problem on your own before looking at the solution.

# Q1: Your First Program
# Write a program that prints:
# Hello, World! Welcome to Python.
print("Hello, World! Welcome to Python");

# Q2: Print a Poem
# Write a program that prints the following poem using a single print() statement:
# (Hint: Use \n for a new line.)
# Twinkle, twinkle, little star,
# How I wonder what you are!
print("\nTwinkle, twinkle, little star,")
print("How I wonder what you are!")

# Q3: Variables & Data Types
# Create variables to store:
# Your name (string)
# Your age (integer)
# Your height in meters (float)
# A boolean value representing whether you are a student
# Print all of them in one line.
name = "Anjali";
age = 22;
height = 4.9;
student = True;
print(name,age,height,student);

# Q4: Typecasting Practice
# You are given a string:
# num = "45"
# Convert it into an integer
# Add 10 to it
# Print the result
num = "45";
int_num = int(num);
print(int_num + 10);

# Q5: Taking User Input
# Write a program that:
# Asks the user for their favorite food.
# Prints:
# Wow! I also like <food>.
food = input("Enter your Favorite Food: ")
print(f"Wow! I also like {food}.")

# Q6: Simple Calculator
# Write a program that:
# Takes two numbers as input from the user.
# Prints their:
# Sum
# Difference
# Product
# Quotient

num1 = int(input("Enter a First Number:"));
num2 = int(input("Enter a Second Number:"));
print(f"Sum: {num1 + num2}");
print(f"Difference: {num1 - num2}");
print(f"Product: {num1 * num2}");
print(f"Quotient: {num1 / num2}");

# Q7: Escape Sequences
# Print the following output using escape sequences:
# Hello "Python" World!
# This is on a new line.
# This is a tab →	    after tab.
print("Hello \"Python\" World!");
print("This is on a new line.");
print("This is a tab →\t after tab.");
 
# Q8: Operator Challenge
# Write a program that:
# Takes an integer as input from the user.
# Prints the square and cube of that number.
num = int(input("Enter a Number:"));
print(f"Square: {num ** 2}");
print(f"Cube: {num  ** 3}");

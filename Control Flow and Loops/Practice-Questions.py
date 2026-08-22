# Python Conditionals & Loops - Practice Set
# This practice set is based on the topics we’ve covered so far:
# If-Else Conditional Statements, Match Case Statements, For Loops, While Loops, and Break/Continue/Pass Statements.
# Use these exercises to practice and solidify your understanding.

# 1. If-Else Conditional Statements:
# 1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
num = int(input("Enter a num:"));
if(num > 0):
    print("Number is Positive")
elif(num < 0):
    print("Number is Negative")
else :
    print("Number is Zero")

# 2. Create a program that checks if a person is eligible to vote (age >= 18).
age = int(input("Enter a person Age: "));
if(age >= 18):
    print("Eligible to vote")
else:
    print("Not Eligible")

# 3. Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
n = int(input("Enter a Number: "))
if(n % 2 == 0):
    print("Even ")
else:
    print("Odd")


# 2. Match Case Statements:
# 1. Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
# 2. Write a program using match case that simulates a simple calculator.
# 3. Ask the user for two numbers and an operation (+, -, *, /).
# 4. Perform the operation using match case.


# 3. For Loops:
# 1. Print numbers from 1 to 10 using a for loop.
# 2. Print the multiplication table of a number (entered by user).
# 3. Calculate the sum of all numbers from 1 to 100 using a for loop.
# 4. Print the following pattern using a for loop:
# *
# **
# ***
# ****


# 4. While Loops:
# 1. Print numbers from 1 to 10 using a while loop.
# 2. Write a program that keeps asking the user to enter a password until they enter the correct one.
# 3. Use a while loop to reverse a given number (e.g., 123 → 321).


# 5. Break, Continue, and Pass Statements:
# 1. Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).
# 2. Print numbers from 1 to 10, skipping the number 5 (use continue).
# 3. Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
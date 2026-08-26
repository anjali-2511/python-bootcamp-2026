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
DayNo = int(input("Enter a Day Number: "))
match DayNo:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")
      
# 2. Write a program using match case that simulates a simple calculator.
# - Ask the user for two numbers and an operation (+, -, *, /).
# - Perform the operation using match case.
 
calculator = input("Enter a Operator: ")
num1 = int(input("Enter a First Number: "))
num2 = int(input("Enter a Second Number: "))
match calculator:
    case "+":
        print(f"Addition: {num1 + num2}")
    case "-":
        print(f"Subtraction: {num1 - num2}")
    case "*":
        print(f"Multiplication: {num1 * num2}")
    case "/":
        print(f"Division:  {num1  / num2}")
    case "":
        print("Enter Valid Operator")

# 3. For Loops:
# 1. Print numbers from 1 to 10 using a for loop.
for i in range (1, 11):
    print(i)

# 2. Print the multiplication table of a number (entered by user).
table = int(input("Enter a Table: "))
for t in range(1, 11):
    print(t * table)

# 3. Calculate the sum of all numbers from 1 to 100 using a for loop.
sum = 0;
for num in range(1, 101):
    sum += num
    print(sum)

# 4. Print the following pattern using a for loop:
# *
# **
# ***
# **** 
for i in range(1, 5):
    print("*" * i)

# 5. Use a for loop to print the following pattern:
# 1
# 22
# 333
# 4444
# 55555
for i in range(1, 6):
    print(str(i) * i)

 
# 6. Use a for loop to print the following pattern:
# 1111111111111111111111111111111
for i in range(20):
    print(1 , end="") 
print()


# 4. While Loops: 
# 1. Print numbers from 1 to 10 using a while loop.
n = 1
while n < 11:
    print(n)
    n += 1; 

# 2. Print the multiplication table of a number  (entered by user) using a while loop
table = int(input("Enter a Table: "))
t = 1
while  t < 11:
    print(t * table)
    t += 1;

# 3. Write a program that keeps asking the user to enter a password until they enter the correct one.
password = "1234"
p = input("Enter a password: ")
while p != password:
    print("Incorrect password, try again")
    p = input("Enter a password: ")
print("Correct Password")

# 4. Use a while loop to reverse a given number (e.g., 123 → 321).
no = 123
reversed_no = 0
while no > 0:
    digit = no % 10
    reversed_no = reversed_no * 10 + digit
    no = no // 10
print(reversed_no)
    

# 5. Break, Continue, and Pass Statements:
# 1. Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 
# (use break).
userno = int(input("Enter a number: "))
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# 2. Use a while loop to print numbers from 1 to 10
n = 1
while n < 11:
    print(n)
    n += 1; 

# 2. Print numbers from 1 to 10, skipping the number 5 (use continue).
n = 1
while n < 11:
    if i == 5:
        continue
    print(n)
    n += 1; 

# 3. Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
n = 1
while n < 6:
    if i == 3:
        pass
    print(n)
    n += 1;

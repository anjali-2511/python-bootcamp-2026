# Function:

# 1. predefine function
# Syntax: 
# function_name(arguments)

# Example:
print("Hello")            
print(len("Python"))      
print(max(4, 9, 2))      
print(sum([1, 2, 3]))      
print(type(10))          
print(abs(-5))            
print(round(3.14159, 2))  

import math
print(math.sqrt(16))      

# 2. userdefine function
# Syntax: 
def function_name():
    # body
    statements
    return value 
   
# Example:
def greet():
    print("Welcome to Python!")

greet()     

# 3. Parameter function
# Syntax:
def function_name(param1, param2):
    # body
    return result

# Example:
def add(a, b):
    return a + b

print(add(5, 3))    


# Task1:
def Sum():
    a = 10
    b = 20
    sum = a + b
    print(sum)

def Sub():
    a = 10
    b = 20
    sub = a - b
    print(sub)

def Multi():
    a = 10
    b = 20
    multi = a * b
    print(multi)

def  Div():
    a = 10
    b = 20
    div = a / b
    print(div)

def Exit():
    print("Exit")

def main():
    atem = 100
    while atem > 0:
        choice = input("Enter a Choice: ")
        if choice == "1":
            Sum()
        elif choice == "2":
            Sub()
        elif choice == "3":
            Multi()
        elif choice == "4":
            Div()
        atem -= 1
    else:
        Exit()
        
    
username = "Anjali"
password  = "anjali123"
 

def login(username, password):
    atem = 3
    while atem > 0:
        name = input("Enter  your username: ")
        pin  = input("Enter your password: ") 
        if username == name and password == pin:
            print("Login Successfull!")
            main()
            break          

        atem -= 1
        print(f"Wrong pin {atem} tried left")
    else:
        print("Username and Password is Wrong")
        

login(username, password)

 

 
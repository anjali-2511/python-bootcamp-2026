# 1. Conditional Statement:



# 2. Conditional Loop:

# while loop: 
i=1
while i<=10:
    print(i)
    i=i+1

# for loop:
for i in range(1,11,1):
    print(i)



# Access Unlock:

atem = 3
while atem > 0:
    pin = input("Enter the pin: ")
    if pin == "1234":
        print("Access granted")
        break
    atem -= 1
    print(f"Wrong pin {atem} tried left")
else:
        print("Account lock To many wrong pin ")



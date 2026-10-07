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

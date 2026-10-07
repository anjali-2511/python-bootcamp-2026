# Access Grandted:

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


# for in Loop:
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print(fruits)
for fruit in fruits:
    print(fruit)

name = "Anjali"
for name in name:
    print(name)

 
products = ["laptop", "mobile", "tablet", "tv"]
avaible = input("Enter the product name: ")
for product in products: 
    if avaible == product:
        print("product is avilable")
        break
else:
     print("Product not found")


 
 
str = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","@","#","$","&"]
password = input("Enter the password:")

for i in password:
    if  i in str:
        print("Password is Strong")
        break
else:
    print("Password is weak")

    


 

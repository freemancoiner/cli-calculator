
from ast import Break
import math

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("select an operation: ")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print("5. Sqaure Root")
print("6. Raise To Power")

while True:
   
    choice = input("Enter choice(1/2/3/4/5/6): ")


    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", substract(num1, num2))
 
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    
    elif choice == '5':
        num = int(input("Enter number: "))
        print(num), "%", "=", math.sqrt(num),
  
    next_calculation = input("would you like to calculate again? (1.press any key/ 2.no) ")
    if next_calculation == "2":
        break 
    
    else:
        print("Invalid Entry")

 
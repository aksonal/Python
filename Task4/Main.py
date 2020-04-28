#main calculator program

from Packages import listoperation,calculator
#from listoperation import *
#from calculator import *

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice= listoperation.User_Choice()

if choice == '1':
   print(num1,"+",num2,"=", calculator.add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", calculator.subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", calculator.multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", calculator.divide(num1,num2))
else:
   print("Invalid input")

import logging
import sys
print("Tell us what do you want to do?")
logging.basicConfig(level=logging.DEBUG)


#Defining funtions
def number_add(x, y):
    return x + y


def number_subtract(x, y):
    return x - y


def number_multiply(x, y):
    return x * y


def number_divide(x, y):
    return x / y



print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


     
choice = input("Choose equation(1/2/3/4): ")

    
if choice in ('1', '2', '3', '4'):
        number1 = float(input("Please, enter the first number: "))
        number2 = float(input("Please, enter the second number: "))

if choice == '1':
   logging.info("Chosen equation: Add")
   print(number1, "+", number2, "=", number_add(number1, number2))
elif choice == '2':
   logging.info("Chosen equation: Subtract")
   print(number1, "-", number2, "=", number_subtract(number1, number2))

elif choice == '3':
   logging.info("Chosen equation: Multiply")
   print(number1, "*", number2, "=", number_multiply(number1, number2))

elif choice == '4':
   logging.info("Chosen equation: Divide")
   print(number1, "/", number2, "=", number_divide(number1, number2))
#break
else:
 print("Invalid Input")
#calculator:
number_1 = float(input("enter your required number_1:"))
number_2 = float(input("enter your required number_2:"))
print( " 1. Enter 1 for addition")
print( " 2. Enter 2 for subtraction")
print( " 3. Enter 3 for multiplication")
print( " 4. Enter 4 for division")
choice = int(input("Enter your preferred choice:"))
if choice == 1:
    print("The addition of both numbers is:", number_1 + number_2)
elif choice == 2:
    print("The subtraction of both numbers is:", number_1 - number_2)
elif choice == 3:
    print("The product of both numbers is:", number_1 * number_2)
elif choice == 4:
    print("The quotient of both numbers is:", number_1 % number_2)
else:
    print("There is an error in choosing operation, please choose a valid operation")
print("\n Thank You for using this calculator")
    
 

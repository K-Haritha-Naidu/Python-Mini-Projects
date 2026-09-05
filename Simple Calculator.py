#calculator:
def inputs():
    number_1 = float(input("enter your required number_1:"))
    number_2 = float(input("enter your required number_2:"))
    print( " 1. Enter 1 for addition")
    print( " 2. Enter 2 for subtraction")
    print( " 3. Enter 3 for multiplication")
    print( " 4. Enter 4 for division")
    choice = int(input("Enter your preferred choice:"))
    return(number_1 , number_2 , choice)
def addition(number_1 , number_2):
        add = number_1 + number_2
        print("The addition of both numbers is:", add)
        return(add)
def subtraction(number_1 , number_2):
        sub = number_1 - number_2
        print("The subtraction of both numbers is:", sub)
        return sub
def multiplication(number_1 , number_2):
       multiply = number_1 * number_2
       print("The product of both numbers is:",multiply)
       return multiply
def division(number_1 , number_2):
         divide = number_1 / number_2
         print("The quotient of both numbers is:", divide)
         return divide
def main():
    while True:
       number_1 , number_2 , choice = inputs()
       if choice == 1:
          add = addition(number_1 , number_2)
       elif choice == 2:
          sub = subtraction(number_1 , number_2)
       elif choice == 3:
          multiply = multiplication(number_1 , number_2)
       elif choice == 4:
          divide = division(number_1 , number_2)
       if choice not in (1 , 2 ,3 ,4) :
          print("There is an error in choosing operation, please choose a valid operation")

       again = input("\nDo you want to calculate again? (yes/no): ").lower()
       if again != "yes":
          break

    print("\n Thank You for using this calculator")
main()
 
       
    
 

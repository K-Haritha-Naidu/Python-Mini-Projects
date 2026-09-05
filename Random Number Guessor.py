# random number guesser
import random
def choose_difficulty_level(): 
    print(" DIFFICULTY LEVELS \n EASY - attempts = 10 , range  = 1-50 , enter 1")
    print(" \n MEDIUM - attempts = 7 , range  = 1-100, enter 2")
    print(" \n DIFFICULT - attempts = 5 , range  = 1-200 , enter 3")
    while True :
     difficulty_level = int(input("choose your difficulty level:"))
     if difficulty_level in (1,2,3):
        return(difficulty_level)
     else:
         print("the input is invalid please try again")
def level(difficulty_level):
    if difficulty_level == 1:
     max_number = 50
     max_attempts = 10
     print("you choose easy level")
    elif difficulty_level == 2:
     max_number = 100
     max_attempts = 7
     print("you choose medium level")
    elif difficulty_level == 3:
     max_number = 200
     max_attempts = 5
     print("you choose difficult level")
    return(max_attempts , max_number)
def assign_random_number(max_number):
    num = random.randint(1,max_number)
    return num
def guessing_game(num , max_attempts):
    count = 1
    guess = int(input("enter your guessing number:"))
    while guess != num and count < max_attempts:
        if num > guess:
          print("more higher")
        elif num < guess:
          print("more lower")
        print("take another guess")
        guess = int(input("enter your guessing number:"))
        count += 1
    return guess , count
def win_or_lose(num , guess , count):
   if num != guess:
       print("GAME OVER")
       print("your number was:", num)
   else:
       print("wohoo! you guessed it right. CONGRATULATIONS")
       print("\n you guessed it in", count,"attempts")
def main():
    difficulty_level = choose_difficulty_level()
    max_attempts , max_number = level(difficulty_level)
    num = assign_random_number(max_number)
    guess , count = guessing_game(num , max_attempts)
    win_or_lose(num , guess , count)
main()

import random
number = random.randrange(10)+1
guess = eval(input("Guess Please : "))
while(guess!=number):
     if guess>number:
      print ("Lower value than yours guess")
      
      guess=eval(input("Guess Please:"))

     if guess<number:
      print("Higher value than guess")

      guess=eval(input("Guess Please:"))
     if guess==number:
         
      print("Correct Guess")

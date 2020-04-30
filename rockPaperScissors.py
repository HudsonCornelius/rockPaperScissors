'''
Created on Apr 30, 2020

@author: ITAUser
'''
from lib2to3.tests.data.infinite_recursion import ssl_crock_st
keepPlaying = True

while keepPlaying == True:
    
    print("Welcome to Rock Paper Scissors.")
    print("Best two out of three. Press q to quit.")
    
    
    import random
    
    compScore = 0
    playerScore = 0

    Rock = 1
    Paper = 2
    Scissors = 3

    while (playerScore < 3) and (compScore < 3):
        compChoice = random.randint(1, 3)
        if (compChoice == 1):
            compChoice = "Rock"
        elif (compChoice == 2):
            compChoice = "Paper"
        else:
            compChoice = "Scissors"

        playerChoice = input("Choose Rock, Paper, or Scissors: ") 
        print("Your Choice: " + playerChoice)
        print("Computers Choice: " + compChoice)
        if playerChoice == "q":
            keepPlaying = False
            break
        elif (playerChoice == "Rock" and compChoice == "Rock") or (playerChoice == "Paper" and compChoice == "Paper") or (playerChoice == "Scissors" and compChoice == "Scissors"):
            print("Draw")
        elif (playerChoice == "Rock" and compChoice == "Paper") or (playerChoice == "Paper" and compChoice == "Scissors") or (playerChoice == "Scissors" and compChoice == "Rock"):
            print("Lose")
            compScore = compScore + 1
            print("Computers score: ")
            print(compScore)
            print("Your score: ")
            print(playerScore) 
        elif (playerChoice == "Paper" and compChoice == "Rock") or (playerChoice == "Scissors" and compChoice == "Paper") or (playerChoice == "Rock" and compChoice == "Scissors"):
            print("Win")
            playerScore = playerScore + 1
            print("Computers score: ")
            print(compScore)
            print("Your score: ")
            print(playerScore) 
        else:
            print("Your input was ivalid")   
  
    print("Thank you for playing")
    print("Computers score: ")
    print(compScore)
    print("Your score: ")
    print(playerScore) 
    if (playerScore == 3):
        print("You Won!")
    elif (compScore == 3):
        print("You Lost")
        
        
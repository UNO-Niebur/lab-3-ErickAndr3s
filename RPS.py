#RPS.py
#Name:Erick Andres
#Date:2/7/2026
#Assignment:Lab 3
#Purpose: Let the user play rock, paper, scissors against the computer while tracking wins, losses, and ties.

import random

def main():
    wins = 0
    ties = 0
    losses = 0

    playAgain = "Y" 
    while playAgain == "Y" :
        #Create a loop that continues as long as the user wants to play.
        #User can play as many games as they wish.
        
        #Randomly choose the computer between 'R', 'P', or 'S'
        computer = random.choice( ["R", "P", "S"] ) 

        #Prompt the user for their RPS selection
        player = input("Pick your weapon(R, P, S): ").upper()
       
        #Determine winner and state what happened to the user

        if computer == "R" :
            print("Computer chose Rock")
        elif computer == "P":
            print( "Computer chose Paper")
        else: 
            print ("Computer chose Scissors")


        if player == "R" :
            print("Player chose Rock")
        elif player == "P" :
           print( "Player chose Paper")
        elif player == "S" :
           print ("Player chose Scissors")
        else:
           print("Invalid input! Use R, P, or S.")
           continue 


        if player == computer : 
            print("Tie!")
            ties += 1

        elif(player == "R" and computer == "S") or \
            (player == "P" and computer == "R") or \
            (player == "S" and computer == "P"):
           print ("You win!")
           wins += 1

        else:
           print("Computer wins!")
           losses += 1
        

        #Ask the user if they would like to play again.
        playAgain = input("Play again? (Y/N): ").upper()

  #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
    main()

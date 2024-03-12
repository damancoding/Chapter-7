# RPS game
# Amanda M
# 2/28/2024

import random
rock = 1
paper = 2
scissors = 3

# global variable player_move
player_move = input("Please choose one of the following: {rock = 1, paper = 2, scissor = 3} ")
def vaild():
    if player_move != ["rock", "paper", "scissor", "1", "2", "3"]:
        player_move
    elif player_move != ["rock", "paper", "scissor", "1", "2", "3"]:
        print('Please input a valid term.')
        player_move

def pc():
    roll = random.randint(1,3)
    if roll == 1:
        print(f"The computer chose {1}.")
        
    elif roll == 2:
        print(f"The computer chose {2}.")
        
    elif roll == 3:
        print(f"The computer chose {3}.")
          
    if pc == player_move:
        print("Sorry no winners! It was a draw!")


def result(sum):
    if (player_move == {2} or "paper" and pc == {1}) or (pc == {1} or "rock" and player_move == {3}) or (player_move == {1} or "rock" and pc == {3}):
            print('The computer  wins.')
    else:
          print(f'Player wins!')        
    choice = input("Play again? Yes or No ")
    while choice != ["yes"]:
         print("Please enter a correct value. ")
         player_move
    if choice == ["yes", "Yes", "y"]:
                player_move
                

sum = pc()
result(sum)

# RPS game first, then modified to become Tic-Tac-Toe
# Amanda M
# 2/28/2024

import random
rock = 1
paper = 2
scissors = 3

# global variable player_move
player_move = input("Please choose one of the following: {rock = 1, paper = 2, scissor = 3} ")

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
    if player_move == {2} or "paper" and pc == {1}:
            print(f'{player_move} wins. Paper covers rock.')
    if pc == {1} or "rock" and player_move == {3}:
            print('The computer  wins. Rock smashes scissors.')
            
    if player_move == {3} or "scissors" and pc == {2}:
            print(f'{player_move} wins. Scissors cut paper.')
    if pc == {2} or "paper" and player_move == {1}:
            print('The computer wins. Paper covers rock.')

    if player_move == {1} or "rock" and pc == {3}:
            print(f'{player_move} wins. Rock smashes scissors.')
    if pc == {3} or "scissors" and player_move == {2}:
            print('The computer wins. Scissors cut paper.')


sum = pc()
result(sum)

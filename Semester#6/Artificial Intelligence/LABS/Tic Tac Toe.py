# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:41:32 2024

@author: Laiba Binta Tahir
"""

#Tic Tac Toe
# 0 |   |   |   
# 1 |   |   |   
# 2 |   |   |   
#   0   1   2
 

import random

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-----')

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def get_random_move(board):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if not empty_positions:
        return None
    return random.choice(empty_positions)

def get_human_move(board):
    while True:
        try:
            move = input("Enter your move (row and column separated by a space, e.g., '1 1' for top-left): ")
            row, col = map(int, move.split())
            if board[row][col] == ' ':
                return row, col
            else:
                print("The cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two integers between 0 and 2.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        current_player = players[turn % 2]
        print("Current board:")
        print_board(board)

        if current_player == 'X':
            # Human move
            row, col = get_human_move(board)
            board[row][col] = 'X'
            print("Human's turn")
        else:
            # Computer move
            row, col = get_random_move(board)
            if row is None:
                print("The game is a draw!")
                break
            board[row][col] = 'O'
            print("Computer's turn")

        if check_win(board, current_player):
            print("Current board:")
            print_board(board)
            print(f"{current_player} wins!")
            break
        if check_draw(board):
            print("Current board:")
            print_board(board)
            print("The game is a draw!")
            break

        turn += 1

# Start the game
play_game()

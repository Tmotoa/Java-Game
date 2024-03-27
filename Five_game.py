import numpy as np

def create_board():
    board = np.full((15, 15), '-', dtype=str)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (1-15): ")) - 1
            col = int(input("Enter column (1-15): ")) - 1

            if 0 <= row < 15 and 0 <= col < 15 and board[row][col] == '-':
                board[row][col] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, player):
    # Check for winning condition
    # Implement the logic to check for 5 in a row horizontally, vertically or diagonally
    return False

def computer_move(board):
    while True:
        row, col = np.random.randint(15, size=2)

        if board[row][col] == '-':
            board[row][col] = 'O'
            break

def main():
    board = create_board()
    print_board(board)

    while True:
        player_move(board)
        if check_win(board, 'X'):
            print("Congratulations! You win!")
            break

        computer_move(board)
        if check_win(board, 'O'):
            print("Computer wins! Try again.")
            break

if __name__ == "__main__":
    main()

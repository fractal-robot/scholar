def printBoard(board):
    print("┌───┬───┬───┐")
    for i, row in enumerate(board):
        print("│ {} │ {} │ {} │".format(row[0], row[1], row[2]))
        if i < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")


def getPlayerMove(board, player):
    validMove = False
    while not validMove:
        row = int(input(f"Player {player}, enter the row number (0-2): "))
        col = int(input(f"Player {player}, enter the column number (0-2): "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = player
                validMove = True
            else:
                print("Spot already taken.")
        else:
            print("Invalid input.")
    return board


def checkForWinner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def main():
    gameBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    currentPlayer = "X"
    while True:
        printBoard(gameBoard)
        gameBoard = getPlayerMove(gameBoard, currentPlayer)
        winner = checkForWinner(gameBoard)
        if winner:
            print(f"Player {winner} wins!")
            break
        elif all(cell != " " for row in gameBoard for cell in row):
            print("It's a tie!")
            break
        currentPlayer = "O" if currentPlayer == "X" else "X"


# ---

main()

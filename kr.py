X = "X"
O = "O"
EMPTY = " "
T="T"

def next_turn(turn):#смена хода
    if turn == X:
        return O
    else:
        return X

def new_board():#создали доску
    board = []
    for square in range(9):
        board.append(EMPTY)
    return board

def display_board(board):#показали доску
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])

def winner(board):#победитель
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
           return T
    return None

def legal_moves(board): #возможные ходы
    moves = []
    for square in range(9):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def computer_move(board, computer, human): # а вот тут начинается веселье, потому что я не знаю, как продумать на несколько ходов вперед
    board = board[:]
    variant = (0,1,2,3,4,5,6,7,8) #перебор по порядку
    # если сдедующим ходом может победить компьютер, выберем этот ход
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    # если следующим ходом может победить чегловек, не берем этот ход
    for moves in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    # поскольку следующим ходом ни одна из сторон не может победить,
    # выберем лучшее из доступных полей
    for move in variant:
        if move in legal_moves(board):
            print(move)
            return move

def congrat_winner(the_winner, computer, human):
    if the_winner != T:
        print("Выиграл", the_winner)
    else:
        print("Ничья!\n")

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Выбери одно из полей 0-8:", 0, 9)
        if move not in legal:
            print("\nЭто поле уже занято.\n")
    return move

def main():
    turn = X
    board = new_board()
    display_board(board)
    human = X
    computer = O
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
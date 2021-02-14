#TIC TAC TOE

def print_move_choices():
    print("Possible choices:")
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for n in board:
        limit = len(n)
        for element in n:
            limit -= 1
            if limit != 0:
                print(f'{element}|', end="")
            else:
                print(f'{element}', end="")
        print()


def print_current_board_state(board):
    print("Current board state:")
    for n in board:
        limit = len(n)
        for element in n:
            limit -= 1
            if element == 'x' or element == 'o':
                if limit != 0:
                    print(f'{element}|', end="")
                else:
                    print(f'{element}', end="")
            else:
                if limit != 0:
                    print(' |', end="")
                else:
                    print(' ', end="")
        print()


def user_move(board, sign):
    user_input = int(input("Please, enter the number of the pleace, where you want to put the sign: "))
    for n in board:
        for index in range(len(n)):
            if n[index] == user_input:
                n[index] = sign


def check_if_win(board):
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return True
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return True
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return True
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return True
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return True
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return True
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True


def check_if_draw(board):
    for n in board:
        for element in n:
            if element != 'x' and element != 'o':
                return False
    return True


def change_sign(current_sign):
    if current_sign == "x":
        current_sign = 'o'
        return current_sign
    else:
        current_sign = 'x'
        return current_sign


if __name__ == "__main__":
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    current_sign = "x"
    print(f'The {current_sign} is starting!')
    while True:
        print_move_choices()
        print_current_board_state(board)
        user_move(board, current_sign)
        if check_if_win(board):
            print(f'{current_sign} win!')
            break
        if check_if_draw(board):
            print('DRAW')
            break
        current_sign = change_sign(current_sign)
        print(f'{current_sign} moves')
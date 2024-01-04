board_size = 3
board = [1,2,3,4,5,6,7,8,9]

def drow_board():
    '''Выводим игровое поле'''
    print('_'* 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i*board_size], '|', board[1 + i*board_size], '|', board[2 + i*board_size], '|')
        print(('_' * 3 + '|') * 3)

def game_step(index,char):
    '''Выполняем ход'''
    if (index > 9 or index < 0 or board[index-1] in ('X', '0')):
        return False

    board[index-1] = char
    return True

def chech_win():
    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def start_game():
    current_player = 'X'
    step = 1
    drow_board()

    while (step <= 9) and (chech_win()== False):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход)*:')

        if (index == '0'):
            break

        if (game_step(int(index), current_player)):
            print("Удачный ход")

            if (current_player == 'X'):
                current_player = '0'
            else:
                current_player = 'X'

            drow_board()
            step += 1
        else:
            print("Неверный номер! Повторите!")
    if (step == 10):
        print("Игра окончена. Ничья.")
    else:
        print('Выиграл ' + chech_win())


print("Добро пожаловать в игру!")
start_game()
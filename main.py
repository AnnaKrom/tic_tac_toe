import random

# функция, рисующая поле
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    #print('\n'*100) # очищение ячейки

# функция, спрашивающая пользователя, какой символ он хочет использовать.
# она работает до тих пор, пока пользователь не введёт корректный символ.
def player_input():

    res = ''

    while res != 'X' and res != '0':
        res = input('Игрок 1 выберите символ "X" или "0": ').upper()

    player1 = res

    if res == 'X':
        player2 = '0'
    else:
        player2 = 'X'

    return (player1,player2)

# функция, принимающая игровое поле, символ и позицию и помещвет символ на поле
def place_marker(board,marker,position):
    board[position] = marker

# функция, проверяющая выигрывание
def win_check(border,mark):
    if border[1] == mark and border[2] == mark and border[3] == mark:
        print('Выиграл игрок с ' + mark)
    elif border[4] == mark and border[5] == mark and border[6] == mark:
        print('Выиграл игрок с ' + mark)
    elif border[7] == mark and border[8] == mark and border[9] == mark:
        print('Выиграл игрок с ' + mark)
    elif border[7] == mark and border[5] == mark and border[3] == mark:
        print('Выиграл игрок с ' + mark)
    elif border[9] == mark and border[5] == mark and border[1] == mark:
        print('Выиграл игрок с ' + mark)
    elif border[1] == mark and border[4] == mark and border[7] == mark:
        print('Выиграл игрок с ' + mark)
    elif border[8] == mark and border[5] == mark and border[2] == mark:
        print('Выиграл игрок с ' + mark)
    elif border[9] == mark and border[6] == mark and border[3] == mark:
        print('Выиграл игрок с ' + mark)

# функция рандомно определяет кто из игроков ходит первым
def choose_first():
    result = random.randint(0,1)
    if result == 0:
        return 'Игрок 1'
    else:
        return 'Игрок 2'

# функция, проверяет пустое ли место на поле
def space_check(board,position):
    return board[position] == ' '

# функция проверяет полностью ли заполнено поле
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board,i):
            return False
    return True

# функция спрашивает следующую позицию у игрока
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Введите поле: (1-9) '))

    return position


def replay():
        otvet = input('Хотите ли Вы сыграть снова? Введите yes или no ')
        otvet = otvet.lower()
        return otvet == 'yes'


print('Добро пожаловать в игру Крестики-Нолики!')

while True:
    the_board = [' ']*10 # начало игры, когда пробелы во всех клетках
    player1_marker, player2_marker = player_input()  # распаковка кортежа

    turn = choose_first()
    print(turn + ' ходит первым')

    play_game = input('Вы готовы играть? Yes или No: ')

    if play_game == "Yes":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок 1':
            # ход игрока 1
            # показать игровое поле
            display_board(the_board)

            # выбор следующего хода
            position = player_choice(the_board)

            # поместить символ на игровое поле
            place_marker(the_board,player1_marker,position)

            # проверить, выиграл ли игрок
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Игрок 1 выиграл')
                game_on = False
            # или, возможно ничья
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья')
                    game_on = False
                # если никто не выиграл и не ничья, то перейти к ходу следующего игрока
                else:
                    turn = 'Игрок 2'

        else:
            # ход игрока 2

            # показать игровое поле
            display_board(the_board)

            # выбор следующего хода
            position = player_choice(the_board)

            # поместить символ на игровое поле
            place_marker(the_board, player2_marker, position)

            # проверить, выиграл ли игрок
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Игрок 2 выиграл')
                game_on = False
            # или, возможно ничья
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья')
                    game_on = False
                # если никто не выиграл и не ничья, то перейти к ходу следующего игрока
                else:
                    turn = 'Игрок 1'

    if not replay():
        break
game_matrix = [
            [0, 'w', 0, 'w', 0, 'w', 0, 'w'],
            ['w', 0, 'w', 0, 'w', 0, 'w', 0],
            [0, 'w', 0, 'w', 0, 'w', 0, 'w'],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            ['b', 0, 'b', 0, 'b', 0, 'b', 0],
            [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
            ['b', 0, 'b', 0, 'b', 0, 'b', 0],
        ]


def print_game():
    letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print('   1   2   3   4   5   6   7   8')
    line_1 = '   1   2   3   4   5   6   7   8'
    game_arr = []
    index = 0
    for i in game_matrix:
        for block in i:
            if block == 0:
                print('⬜️', end='')
                game_arr.append('⬜️')
            elif block == 1:
                print('⬛️', end='')
                game_arr.append('⬛️')
            elif block == 'w':
                print('🔵', end='')
                game_arr.append('🔵')
            elif block == 'b':
                print('🔴', end='')
                game_arr.append('🔴')
        print(f' {letter_array[index]}', end=' ')
        game_arr.append(f' {letter_array[index]}')
        print('')
        index += 1


def return_game():
    ui_matrix = [[], [], [], [], [], [], [], []]
    order = 0
    for line in ui_matrix:
        for element in line:
            order += 1



print(return_game())

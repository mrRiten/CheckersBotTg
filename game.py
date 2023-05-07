# from threading import Thread
import threading as th


# Main Game Class for working with threads
class GamePlay(th.Thread):
    # Set game matrix
    def __init__(self, name_session=None, player1=None, player2=None, game_matrix=None):
        th.Thread.__init__(self)
        self.game_matrix = game_matrix
        self.name_session = name_session
        self.player1 = player1
        self.player2 = player2
        self.game_matrix = [
            [0, 'w', 0, 'w', 0, 'w', 0, 'w'],
            ['w', 0, 'w', 0, 'w', 0, 'w', 0],
            [0, 'w', 0, 'w', 0, 'w', 0, 'w'],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            ['b', 0, 'b', 0, 'b', 0, 'b', 0],
            [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
            ['b', 0, 'b', 0, 'b', 0, 'b', 0],
        ]

    # run game session
    def session_start(self):
        # TODO: run session with players
        print(f'\nSession: {self.name_session}: pl1: {self.player1}')
        print(f'\nSession: {self.name_session}: pl2: {self.player2}')

        return [self.name_session, self.player1, self.player2]

    # Print game for players and realize simple ui
    def print_game(self):
        letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        print('   1   2   3   4   5   6   7   8')
        line_1 = '   1   2   3   4   5   6   7   8'
        game_arr = []
        index = 0
        for i in self.game_matrix:
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

        print(*self.ui_output()[0])
        print(*self.ui_output()[1])

    # Get all positions of checkers
    def get_checkers(self):
        list_of_white = []
        list_of_black = []

        # Get all positions of white
        letter = 0
        for line in self.game_matrix:
            num = 0
            for block in line:
                if block == 'w':
                    position = [letter, num]
                    list_of_white.append(position)
                num += 1
            letter += 1

        # Get all positions of black
        letter = 0
        for line in self.game_matrix:
            num = 0
            for block in line:
                if block == 'b':
                    position = [letter, num]
                    list_of_black.append(position)
                num += 1
            letter += 1

        return [list_of_white, list_of_black]

    # Move checkers
    # WARNING: bad and hard code!
    def move_checkers(self, color, position_ui, step):
        position = self.ui_input(position_ui)
        if color == 'w':
            # move white checkers
            if step == 'l':
                # go left
                if self.game_matrix[position[0] + 1][position[1] - 1] == 1:
                    self.game_matrix[position[0] + 1][position[1] - 1] = 'w'
                    self.game_matrix[position[0]][position[1]] = 1
                # eat left
                elif self.game_matrix[position[0] + 1][position[1] - 1] == 'b':
                    self.game_matrix[position[0] + 1][position[1] - 1] = 1
                    self.game_matrix[position[0] + 2][position[1] - 2] = 'w'
                    self.game_matrix[position[0]][position[1]] = 1
            elif step == 'r':
                # go right
                if self.game_matrix[position[0] + 1][position[1] + 1] == 1:
                    self.game_matrix[position[0] + 1][position[1] + 1] = 'w'
                    self.game_matrix[position[0]][position[1]] = 1
                # eat right
                elif self.game_matrix[position[0] + 1][position[1] + 1] == 'b':
                    self.game_matrix[position[0] + 1][position[1] + 1] = 1
                    self.game_matrix[position[0] + 2][position[1] + 2] = 'w'
                    self.game_matrix[position[0]][position[1]] = 1

            # eat back
            # left
            elif step == 'bl':
                if self.game_matrix[position[0] - 1][position[1] - 1] == 'b':
                    self.game_matrix[position[0] - 1][position[1] - 1] = 1
                    self.game_matrix[position[0] - 2][position[1] - 2] = 'w'
                    self.game_matrix[position[0]][position[1]] = 1

            # right
            elif step == 'br':
                if self.game_matrix[position[0] - 1][position[1] + 1] == 'b':
                    self.game_matrix[position[0] - 1][position[1] + 1] = 1
                    self.game_matrix[position[0] - 2][position[1] + 2] = 'w'
                    self.game_matrix[position[0]][position[1]] = 1

        elif color == 'b':
            # move black checkers
            if step == 'l':
                # go left
                if self.game_matrix[position[0] - 1][position[1] - 1] == 1:
                    self.game_matrix[position[0] - 1][position[1] - 1] = 'b'
                    self.game_matrix[position[0]][position[1]] = 1
                # eat left
                elif self.game_matrix[position[0] - 1][position[1] - 1] == 'w':
                    self.game_matrix[position[0] - 1][position[1] - 1] = 1
                    self.game_matrix[position[0] - 2][position[1] - 2] = 'b'
                    self.game_matrix[position[0]][position[1]] = 1

            if step == 'r':
                # go right
                if self.game_matrix[position[0] - 1][position[1] + 1] == 1:
                    self.game_matrix[position[0] - 1][position[1] + 1] = 'b'
                    self.game_matrix[position[0]][position[1]] = 1
                # eat right
                elif self.game_matrix[position[0] - 1][position[1] + 1] == 'w':
                    self.game_matrix[position[0] - 1][position[1] + 1] = 1
                    self.game_matrix[position[0] - 2][position[1] + 2] = 'b'
                    self.game_matrix[position[0]][position[1]] = 1

            # eat back
            # left
            if step == 'bl':
                if self.game_matrix[position[0] + 1][position[1] - 1] == 'w':
                    self.game_matrix[position[0] + 1][position[1] - 1] = 1
                    self.game_matrix[position[0] + 2][position[1] - 2] = 'b'
                    self.game_matrix[position[0]][position[1]] = 1
            # right
            if step == 'br':
                if self.game_matrix[position[0] + 1][position[1] + 1] == 'w':
                    self.game_matrix[position[0] + 1][position[1] + 1] = 1
                    self.game_matrix[position[0] + 2][position[1] + 2] = 'b'
                    self.game_matrix[position[0]][position[1]] = 1

        self.print_game()

    # User interface for input actions
    @staticmethod
    def ui_input(position):
        key_letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        letter = int(key_letters.get(position[0]))
        num = int(position[1]) - 1
        return [letter, num]

    # Format user interface for output information
    def ui_output(self):
        white = self.get_checkers()[0]
        black = self.get_checkers()[1]
        white_out = []
        black_out = []
        key_letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        # for white
        for i in white:
            white_out.append([key_letters.get(i[0]), i[1] + 1])
        # for black
        for i in black:
            black_out.append([key_letters.get(i[1]), i[1] + 1])
        return [white_out, black_out]


game = GamePlay('123', 'rrr', 'www')
game.session_start()

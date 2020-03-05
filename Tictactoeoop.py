# Tic Tac Toe OOP
# Tic Tac Toe is a game that is played on a 3 by 3 grid, with two symbols O and X. A player wins onces you have 3 of the same symbols in a row. Aka you can draw a straight line through them
# What we need
# A way to display the grid
# A way for the player to choose the symbol, and assign it to player 1 and player 2
# A way to place something on the grid
# A way to check who won
# Game loop
import random


class Grid:

    def __init__(self):
        pass

    def display(self, board):
        print(board[1]+'|' + board[2]+'|'+board[3])
        print('------')
        print(board[4]+'|'+board[5]+'|'+board[6])
        print('------')
        print(board[7]+'|'+board[8]+'|'+board[9])

    def placement(self, board, position, mark):
        board[position] = mark

    def placement_avalible(self, board, position):
        # Returns a True value if the board[position] is equal to a blank space
        return board[position] == ' '

    def win_check(self, board, mark):  # returns a True or False statement to see who wins
        return ((board[1] == board[2] == board[3] == mark) or  # Checks first row
                # Checks second row
                (board[4] == board[5] == board[6] == mark) or
                # Checks third row
                (board[7] == board[8] == board[9] == mark) or
                # Checks first down
                (board[1] == board[4] == board[7] == mark) or
                # Checks second down
                (board[2] == board[5] == board[8] == mark) or
                # Checks third down
                (board[3] == board[6] == board[9] == mark) or
                (board[1] == board[5] == board[9] == mark) or  # First diagnol
                (board[3] == board[5] == board[7] == mark))  # Checks second diagnol

    def tie_game(self, board):
        for i in range(1, 10):
            if board[i] == ' ':
                return False

        else:
            return True


# CHECK!
# Test tie_game method
# x = Grid()
# a = ['X','O','X','X','O','X','X','O','X','O']
# print(x.tie_game(a))

# CHECK!
# Test Grid class and placement:
# x = Grid()
# a = ['X','O','X','X','O','X','X','O','X','O']
# x.placement(a,5,'HOLA')
# x.display(a)

# CHECK!
# Test board positon avalible
# x = Grid()
# a = ['X','O',' ','X','O','X','X','O','X','O']
# x.display(a)
# print(x.placement_avalible(a,2))

# CHECK!
# Test win_check method
# x = Grid()
# a = ['X','X','X','O','X','X','O','X','O','X']
# x.display(a)
# print(x.win_check(a,'X'))


class Player:

    def __init__(self):
        self.player1 = ''
        self.player2 = ''

    def symbol(self):

        try:
            x = 0
            while x != 'O' or x != 'X':  # Create a while loop so it keeps asking for a correct answer
                x = input('Player 1 pick a Character: X or O?').upper()

                # Once a correct answer is given it will add the values to the player1 and player2 attributes, and break out of the loop then
                if x == 'X':
                    self.player1 = 'X'
                    self.player2 = 'O'
                    break
                elif x == 'O':
                    self.player1 = 'O'
                    self.player2 = 'X'
                    break

        except:
            return self.symbol()  # if the player had put something else, or an error, it will recall the method thus reseting it asking the question again about what symbol the player wants

    def symbol_position(self):
        try:
            choice = 0
            while choice != range(1, 10):
                choice = int(
                    input('Pick a position to place your mark. (1-9)'))

                if choice in range(1, 10):
                    break
            return choice
        except:
            return self.symbol_position()  # calling back to the method incase of errors

# Check!
# Test Player class
# x = Player()
# x.symbol()
# print('Player 1: ',x.player1)
# print('Player 2: ',x.player2)

# Test symbol_position method
# x = Player()
# print(x.symbol_position())


class Game:

    def __init__(self):
        pass

    def play(self):
        playing = True

        while playing:
            print('Welcome to My Tic Tac Toe Game!')
            play = input('Do you want to play? y or n').lower()
            main_board = Grid()
            board = [' ']*10
            player = Player()
            flip = random.randint(0, 1)
            if play == 'y':
                player_one = input('Player 1: What is your name?')
                player_two = input('Player 2: What is your name?')
                print('\n'*100)
                player.symbol()
                main_board.display(board)
                play_game = True

            else:
                break

            while play_game:
                # Works but only puts 1 character at a time and doesn't check if there is a character already at the position fix!

                # player 1
                if flip == 0:
                    print(f'{player_one}: {player.player1}')
                    position = player.symbol_position()

                    while True:
                        if main_board.placement_avalible(board, position):
                            print('\n'*100)
                            main_board.placement(
                                board, position, player.player1)
                            main_board.display(board)
                            flip = 1
                            break
                        else:
                            position = player.symbol_position()

                    if main_board.win_check(board, player.player1):
                        print('\n'*100)
                        main_board.display(board)
                        print(f'{player_one} has won!: {player.player1}')
                        break

                    elif main_board.tie_game(board):
                        print('\n'*100)
                        main_board.display(board)
                        print('Tie Game!')
                        break

                # player 2
                if flip == 1:
                    print(f'{player_two}: {player.player2}')
                    position = player.symbol_position()
                    while True:
                        if main_board.placement_avalible(board, position):
                            print('\n'*100)
                            main_board.placement(
                                board, position, player.player2)
                            main_board.display(board)
                            flip = 0
                            break
                        else:
                            position = player.symbol_position()

                    if main_board.win_check(board, player.player2):
                        print('\n'*100)
                        main_board.display(board)
                        print(f'{player_two} has won!: {player.player2}')
                        break

                    elif main_board.tie_game(board):
                        print('\n'*100)
                        main_board.display(board)
                        print('Tie Game!')
                        break


# Plays the game
if __name__ == '__main__':
    g = Game()
    g.play()

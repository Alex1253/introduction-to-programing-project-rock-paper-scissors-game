#!/usr/bin/env python3

# Rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

moves = ['rock', 'paper', 'scissors']

# Parent Player class
class Player():

    def __init__(user):

        user.score = 0

    def move(user):

        return moves[0]

    def learn(user, learn_move):

        pass

# This class selects a random move choice
class RandomPlayer(Player):
    def move(user):
        choose = random.choice(moves)
        return (choose)

# This Class reflects the user 1st and 2nd moves
class ReflectPlayer(Player):

    def __init__(user):

        Player.__init__(user)
        user.learn_move = None

    def move(user):
        if user.learn_move is None:
            choose = moves[0]                      # First move is always rock
        else:
            choose = user.learn_move               # next move
            return (choose)                        # previous move

    def learn(user, learn_move):

        user.learn_move = learn_move

# This Class cycles through the moves list starting at rock
class Cycles(Player):

    def __init__(user):

        Player.__init__(user)
        user.step = 0

    def move(user):
        choose = None
        if user.step == 0:
            choose = moves[0]
            user.step = user.step + 1
        elif user.step == 1:
            choose = moves[1]
            user.step = user.step + 1
        else:
            choose = moves[2]
            user.step = user.step + 1
        return choose

# This class requests the user to make a selection
class HumanPlayer(Player):

    def move(user):
        # ask what the user wants to play
        choose = input('Please choose rock, paper or scissors? >')
        # Input Validation
        while choose != 'rock'and choose != 'paper'and choose != 'scissors':
            print('Invalid input, please try again!')
            choose = input('Enter rock, paper or scissors? >')
        return (choose)

# This class starts the game prints information and calls the playround class
class Game():

    def __init__(user, p2):
        user.p1 = HumanPlayer()
        user.p2 = p2

    def play_game(user):

        print("Rock Paper Scissors, Go!")
        for round in range(3):
            print (f"Round {round}:")
            user.play_round()
        if user.p1.score > user.p2.score:
            print('You won!')
        elif user.p1.score < user.p2.score:
            print('The computer won!')
            #  Prints out the final score
        else:
            print('The game was a tie!')
        print('The final score ' + str(user.p1.score) + ' TO ' +
              str(user.p2.score))

# This class will play a single round of RPS
    def play_single(user):
        print("Rock Paper Scissors, Go!")
        print (f"Round 1 of 1:")
        user.play_round()
        if user.p1.score > user.p2.score:
            print('You won!')
        elif user.p1.score < user.p2.score:
            print('The computer won!')
        else:
            print('The game was a tie!')
        print('The final score ' + str(user.p1.score) + ' TO ' +
              str(user.p2.score))

# This class calls the play class, sets the move 1 and 2 variables
    def play_round(user):
        move1 = user.p1.move()
        move2 = user.p2.move()
        result = Game.play(move1, move2)
        user.p1.learn(move2)
        user.p2.learn(move1)

# then sets the result variable. Plus stores the players move
    def play(user, move1, move2):
            print(f"You played {move1}")
            print(f"The computer played {move2}")
            if beats(move1, move2):
                print ("** YOU WON ! **")
                print(f"Score: You choose: {move1}  The computer choose: {move2}")
                user.p1.score += 1
                return 1
            elif beats(move2, move1):
                print ("** THE COMPUTER WON ! **")
                print(f"Score: You choose: {move1}  The computer choose: {move2}")
                user.p2.score += 1
                return 2
            else:
                print ("** It's A TIE **")
                print(f"Score: You choose: {move1}  The computer choose: {move2}")
                return 0

# This class calls the beats functions
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

if __name__ == '__main__':
    # play_style is the players class list
    play_style = [Player(), RandomPlayer(), Cycles(), ReflectPlayer()]
    p2 = input('Select the RPS game you would like to play: rock, random, reflective or cycles or just hit any key and enter for a random game >')

# p2 is output input from the user
    while p2 != 'rock' or p2 != 'random' or p2 != 'reflective' or p2 != 'cycles':
        # automatically selects a random choice
        p2 = random.choice(play_style)
        break

# Set the p2 variable to the correct player class
    if p2 == 'Rock':
        p2 = Player()
    elif p2 == 'Random':
        p2 = RandomPlayer()
    elif p2 == 'Cycles':
        p2 = Cycles()
    elif p2 == 'Reflective':
        p2 = ReflectPlayer()

# Ask to select the lenght of the game
    full_game_or_single_game = input('Enter for [s]ingle game or [f]ull game: >')
    Game = Game(p2)
    while True:
        if full_game_or_single_game == 's':
            Game.play_single()
            break
        elif full_game_or_single_game == 'f':
            Game.play_game()
            break
            # Input Validation
        else:
            print('Invalid input, please try again!')
            full_game_or_single_game = input('Enter s for a single game and f for a full game: >')

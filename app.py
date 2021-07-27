from phrasehunter.game import Game
from phrasehunter.phrases_list import list_of_phrases
from random import choice


if __name__ == '__main__':
    playing = True
    while playing:
        game = Game(list_of_phrases)
        game.start()
        again = input("Enter 'Y' if you would like to play again: ")
        if again.strip().lower() != 'y':
            print("Thanks for playing!")
            playing = False

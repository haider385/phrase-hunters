from phrasehunter.phrase import Phrase
from random import choice

class Game:
    def __init__(self, phrases):
        self.phrase = Phrase(choice(phrases))
        self.missed = 0
        self.guesses = []

    def get_guess(self):
        guess = input("\nGuess a letter: ").lower().strip()
        if len(guess) != 1 or guess.isalpha() == False:
            print("That is not a valid guess, try again.")
            return False
        elif guess.lower() in self.guesses:
            print("You have already guessed that letter, try again.")
            return False
        return guess

    def welcome(self):
        print("Hello! Welcome to the Phrase Hunter Game.\n" +
              "Guess a letter each turn. If incorrect, you will lose a life.\n" +
              "You have 5 lives. Can you guess the phrase?\n")

    def start(self):
        self.welcome()
        while not self.phrase.check_complete():
            self.phrase.display()
            guess = False
            while not guess:
                guess = self.get_guess()
            self.guesses.append(guess.lower())
            if self.phrase.check_letter(guess):
                print("Well done! You guessed a correct letter.\n")
            else:
                self.missed += 1
                print("Incorrect, you have {} out of 5 lives remaining.\n".format(
                    5 - self.missed))
            if self.missed == 5:
                break

        if self.phrase.check_complete():
            print("Congratulations, you guessed the phrase! It was '{}'".format(
                self.phrase.phrase))
        else:
            print("Game over. You ran out of lives. The phrase was '{}'".format(
                self.phrase.phrase))

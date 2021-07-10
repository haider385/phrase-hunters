from random import choice
from phrases import phrases

class Phrase:
    
    def __init__(self):
        self.phrase_list = list(choice(phrases))
        hidden = []
        for letter in self.phrase_list:
            if letter == ' ':
                hidden.append('/')
            else:
                hidden.append('_')
        self.hidden = hidden

    def __str__(self):
        return ' '.join(self.hidden)

    def check_guess(self, guess):
        """remember that each letter must have a space after
           it in order to be matched against letters in  list"""
        if guess.lower() in ''.join(self.phrase_list).lower():
            for i in range(len(self.phrase_list)):
                if self.phrase_list[i].lower() == guess.lower():
                    self.hidden[i] = f'{self.phrase_list[i]}'
            print(' '.join(self.hidden))
            return True
        return False

    def check_complete(self):
        if '_' not in hidden:
            return True
            
            
            
        

a = Phrase()
print(''.join(a.phrase_list))
a.check_guess('e')
print(' '.join(a.hidden))

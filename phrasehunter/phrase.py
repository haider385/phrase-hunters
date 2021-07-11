class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase_list = list(phrase)
        hidden = []
        for letter in self.phrase_list:
            if letter == ' ':
                hidden.append('/')
            else:
                hidden.append('_')
        self.hidden = hidden

    def check_letter(self, guess):
        if guess.lower() in ''.join(self.phrase_list).lower():
            for i in range(len(self.phrase_list)):
                if self.phrase_list[i].lower() == guess.lower():
                    self.hidden[i] = f'{self.phrase_list[i]}'
            return True
        return False

    def check_complete(self):
        if '_' not in self.hidden:
            return True

    def display(self):
        print(' '.join(self.hidden))

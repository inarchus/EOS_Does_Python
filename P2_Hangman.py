class HangmanGame:
    VICTORY = 1
    DEFEAT = 2

    def __init__(self, answer):
        self.answer = answer.lower()
        self.bad_guesses = []
        self.word_blanks = ['_' for _ in answer]

    def finished(self):
        if not any(c == '_' for c in self.word_blanks):
            return self.VICTORY
        elif len(self.bad_guesses) > 5:
            return self.DEFEAT

    def check_guess(self, guess):
        if guess in self.answer:
            for i in range(len(self.word_blanks)):
                if self.answer[i] == guess:
                    self.word_blanks[i] = guess
        elif guess not in self.bad_guesses:
            self.bad_guesses.append(guess)
            print(guess, 'is a bad guess.')
        else:
            print('You\'ve Guessed that before.')

    def play_game(self):

        while not self.finished():
            self.draw_word()
            self.draw_dude()
            new_guess = self.get_guess()
            self.check_guess(new_guess)

        if self.finished() == self.VICTORY:
            print('Victory, You Guessed the Word')
        else:
            print('Defeat, you\'ve been hanged\n', 'The word was', self.answer)

        self.draw_word()
        self.draw_dude()

    def draw_word(self):
        print('\n', ' '.join(self.word_blanks), '\n')

    def draw_dude(self, test_number=-1):
        out_grid = [[' ' for _ in range(3)] for _ in range(3)]
        man = [((0, 1), 'o'), ((1, 1), '|'), ((1, 0), '-'), ((1, 2), '-'), ((2, 0), '/'), ((2, 2), '\\')]

        for i in range(len(self.bad_guesses) if test_number == -1 else test_number):
            r, s = man[i][0]
            out_grid[r][s] = man[i][1]
        print('\n'.join([''.join(out_grid[i])for i in range(3)]))

    @staticmethod
    def get_guess():
        while True:
            c = input('Enter your guess: ')
            if len(c) == 1 and c.lower() in [chr(x) for x in range(97, 123)]:
                return c.lower()
            else:
                print('You have not entered a single character.')


hangman = HangmanGame('Hello')
hangman.play_game()

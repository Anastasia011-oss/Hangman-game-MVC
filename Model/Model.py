import random

class HangmanModel:
    def __init__(self):
        self.words = ["apple", "banana", "orange", "grape", "lemon", "tiger", "lion", "elephant"]
        self.reset()

    def reset(self):
        self.word = random.choice(self.words)
        print(f"[DEBUG] New word: {self.word}")
        self.guessed_letters = []
        self.wrong_attempts = 0
        self.max_attempts = 6
        self.game_over = False
        self.win = False

    def guess(self, letter):
        if self.game_over or letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.wrong_attempts += 1
            if self.wrong_attempts >= self.max_attempts:
                self.game_over = True
        else:
            if all(l in self.guessed_letters for l in self.word):
                self.game_over = True
                self.win = True

    def get_display_word(self):
        return " ".join([l if l in self.guessed_letters else "_" for l in self.word])



class HangmanController:
    def __init__(self, model, view=None):
        self.model = model
        self.view = view

    def on_guess(self):
        letter = self.view.entry.get().lower()
        if letter and letter.isalpha() and len(letter) == 1:
            self.model.guess(letter)
            self.view.entry.delete(0, "end")
            self.view.update(self.model)

    def on_reset(self):
        self.model.reset()
        self.view.update(self.model)

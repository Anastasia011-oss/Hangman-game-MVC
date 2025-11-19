import tkinter as tk

class HangmanView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        root.title("Hangman Game")
        root.geometry("450x500")
        root.configure(bg="#f0f8ff")

        self.title_label = tk.Label(root, text="Hangman Game", font=("Comic Sans MS", 24, "bold"), bg="#f0f8ff", fg="#2c3e50")
        self.title_label.pack(pady=20)

        self.word_label = tk.Label(root, text="", font=("Helvetica", 28), bg="#f0f8ff", fg="#34495e")
        self.word_label.pack(pady=20)

        entry_frame = tk.Frame(root, bg="#f0f8ff")
        entry_frame.pack(pady=10)
        self.entry = tk.Entry(entry_frame, font=("Helvetica", 18), width=5, justify="center")
        self.entry.pack(side="left", padx=5)
        self.entry.bind("<Return>", self.on_guess)
        self.guess_button = tk.Button(entry_frame, text="Guess", font=("Helvetica", 14), bg="#3498db", fg="white", command=self.on_guess)
        self.guess_button.pack(side="left", padx=5)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), bg="#e74c3c", fg="white", command=self.controller.on_reset)
        self.reset_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Attempts left: 6", font=("Helvetica", 16), bg="#f0f8ff", fg="#c0392b")
        self.status_label.pack(pady=10)

        self.message_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
        self.message_label.pack(pady=10)

    def on_guess(self, event=None):
        self.controller.on_guess()

    def update(self, model):
        self.word_label.config(text=model.get_display_word())
        self.status_label.config(text=f"Attempts left: {model.max_attempts - model.wrong_attempts}")

        if model.game_over:
            if model.win:
                self.message_label.config(text="You won! 🎉", fg="green")
            else:
                self.message_label.config(text=f"You lost! The word was '{model.word}'.", fg="red")
        else:
            self.message_label.config(text="")



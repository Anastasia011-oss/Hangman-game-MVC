import tkinter as tk
from Model.Model import HangmanModel
from View.View import HangmanView
from Controller.Controller import HangmanController

if __name__ == "__main__":
    root = tk.Tk()
    model = HangmanModel()
    controller = HangmanController(model)
    view = HangmanView(root, controller)
    controller.view = view
    view.update(model)
    root.mainloop()

import tkinter as tk
from game import ReactionGame
from score import ScoreChecker

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.start_screen()

    def start_screen(self):
        self.clear_screen()
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)
        self.score_button = tk.Button(self.root, text="Check the Score", command=self.check_score)
        self.score_button.pack(pady=20)
        self.quit_button = tk.Button(self.root, text="Quit Game", command=self.root.quit)
        self.quit_button.pack(pady=20)

    def start_game(self):
        self.clear_screen()
        ReactionGame(self.root, self.start_screen)

    def check_score(self):
        self.clear_screen()
        ScoreChecker(self.root, self.start_screen)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    menu = MainMenu(root)
    root.mainloop()
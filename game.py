import tkinter as tk
from tkinter import messagebox
import random
import time

class ReactionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaction Game")
        self.target_key = None
        self.keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.instruction_label = tk.Label(root, text="Press the key: ")
        self.instruction_label.pack(pady=10)
        self.time_label = tk.Label(root, text="Time left: 0.0s")
        self.time_label.pack(pady=10)
        self.start_time = None
        self.time_limit = 2  # seconds
        self.remaining_time = self.time_limit
        self.level = 0
        self.score = 0
        self.results = []
        self.root.bind('<KeyPress>', self.check_reaction)
        self.start_game()

    def start_game(self):
        if self.level < 4:
            self.target_key = random.choice(self.keys)
            self.instruction_label.config(text=f"Press the key: {self.target_key}")
            self.time_label.config(text="Time left: 0.0s")
            self.root.after(random.randint(1000, 3000), self.enable_key_press)
        else:
            result_message = "\n".join(self.results)
            messagebox.showinfo("Game Over", f"Your score: {self.score}\n\nResults:\n{result_message}")
            self.root.quit()

    def enable_key_press(self):
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        self.remaining_time = self.time_limit - elapsed_time
        if self.remaining_time > 0:
            self.time_label.config(text=f"Time left: {self.remaining_time:.1f}s")
            self.root.after(100, self.update_timer)
        else:
            self.time_label.config(text="Time left: 0.0s")
            self.check_reaction(None)

    def check_reaction(self, event):
        if event is not None:
            pressed_key = event.keysym.upper()
            if pressed_key == self.target_key:
                reaction_time = time.time() - self.start_time
                if reaction_time <= self.time_limit:
                    self.score += 1
                    self.results.append(f"Level {self.level + 1}: Passed")
                else:
                    self.results.append(f"Level {self.level + 1}: Failed (Time out)")
            else:
                self.results.append(f"Level {self.level + 1}: Failed (Wrong key)")
        else:
            self.results.append(f"Level {self.level + 1}: Failed (Time out)")
        
        self.level += 1
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = ReactionGame(root)
    root.mainloop()
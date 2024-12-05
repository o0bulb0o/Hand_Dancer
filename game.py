import tkinter as tk
import random
import time

class ReactionGame:
    def __init__(self, root, back_to_menu_callback):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
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
        self.bind_keys()
        self.next_level()

    def bind_keys(self):
        for key in self.keys:
            self.root.bind(f'<KeyPress-{key}>', self.check_reaction)

    def unbind_keys(self):
        for key in self.keys:
            self.root.unbind(f'<KeyPress-{key}>')

    def next_level(self):
        if self.level < 4:
            self.target_key = random.choice(self.keys)
            self.instruction_label.config(text=f"Press the key: {self.target_key}")
            self.time_label.config(text="Time left: 0.0s")
            self.root.after(random.randint(1000, 3000), self.enable_key_press)
        else:
            self.end_game()

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
        self.next_level()

    def end_game(self):
        self.clear_screen()
        result_message = "\n".join(self.results)
        result_label = tk.Label(self.root, text=f"Game Over\nYour score: {self.score}\n\nResults:\n{result_message}")
        result_label.pack(pady=20)
        play_again_button = tk.Button(self.root, text="Play Again", command=self.restart_game)
        play_again_button.pack(pady=20)
        quit_button = tk.Button(self.root, text="Quit Game", command=self.back_to_menu_callback)
        quit_button.pack(pady=20)

    def restart_game(self):
        self.clear_screen()
        self.__init__(self.root, self.back_to_menu_callback)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
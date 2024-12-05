import tkinter as tk

class ScoreChecker:
    def __init__(self, root, back_to_menu_callback):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
        self.display_scores()

    def display_scores(self):
        self.clear_screen()
        # 假設這裡有一些分數數據，這裡用靜態數據作為示例
        scores = [
            "Player 1: 3",
            "Player 2: 4",
            "Player 3: 2"
        ]
        score_label = tk.Label(self.root, text="Scores:\n" + "\n".join(scores))
        score_label.pack(pady=20)
        back_button = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu_callback)
        back_button.pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
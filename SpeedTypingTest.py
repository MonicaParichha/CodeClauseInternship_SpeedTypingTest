import time
import random
import tkinter as tk
from tkinter import ttk, messagebox

class SpeedTypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Speed Typing Test")
        self.master.geometry("400x200")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Pack my box with five dozen liquor jugs.",
            "How razorback-jumping frogs can level six piqued gymnasts!",
            "The five boxing wizards jump quickly.",
            "Jinxed wizards pluck ivy from the big quilt.",
            "The lazy dog slept on the rug.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question."
        ]

        self.label = ttk.Label(master, text="")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(master)
        self.entry.pack(pady=10)

        self.start_button = ttk.Button(master, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=10)

        self.style = ttk.Style()
        self.style.configure("TButton", padding=10, font=("Helvetica", 12))

    def start_typing_test(self):
        self.sentence = random.choice(self.sentences)
        self.label.config(text=f"TYPE:\n{self.sentence}")
        self.start_button.config(state="disabled")

        self.start_time = time.time()

        self.master.bind("<Return>", self.check_input)

    def check_input(self, event):
        user_input = self.entry.get().strip()
        elapsed_time = time.time() - self.start_time
        wpm = (len(self.sentence.split()) / elapsed_time) * 60

        if user_input == self.sentence:
            messagebox.showinfo("Result", f"Your typing speed is {wpm:.1f} words per minute.")
        else:
            messagebox.showerror("Result", "Oops! Doesn't match, Try again!")

        self.label.config(text="")
        self.entry.delete(0, tk.END)
        self.start_button.config(state="normal")
        self.master.unbind("<Return>")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()

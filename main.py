import tkinter as tk
from tkinter import messagebox
import threading


class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing App with Timeout")

        self.label = tk.Label(root, text="Start typing below:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.textbox = tk.Entry(root, width=50, font=("Arial", 14))
        self.textbox.pack(pady=10)
        self.textbox.bind("<KeyRelease>", self.on_key_release)

        self.timer = None

    def on_key_release(self, event):
        if self.timer:
            self.timer.cancel()

        self.timer = threading.Timer(5.0, self.clear_textbox)
        self.timer.start()

    def clear_textbox(self):
        self.textbox.delete(0, tk.END)
        messagebox.showinfo("Timeout", "Text cleared due to inactivity!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    app.run()

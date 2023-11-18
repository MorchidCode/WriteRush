import tkinter as tk
from tkinter import messagebox

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        root.title("WriteRush")

        self.text_area = tk.Text(root, height=20, width=60)
        self.text_area.pack(padx=10, pady=10)

        self.timer_label = tk.Label(root, text="Time Left: 5s")
        self.timer_label.pack()

        self.countdown_time = 5000  # 5 seconds in milliseconds
        self.timer_id = None

        self.text_area.bind("<Key>", self.reset_timer)

    def reset_timer(self, event=None):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)

        self.timer_label.config(text="Time Left: 5s")
        self.countdown_time = 5000
        self.timer_id = self.root.after(self.countdown_time, self.delete_text)

    def delete_text(self):
        self.text_area.delete("1.0", tk.END)
        messagebox.showinfo("Time's Up!", "You stopped writing. All text has been deleted.")

def main():
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

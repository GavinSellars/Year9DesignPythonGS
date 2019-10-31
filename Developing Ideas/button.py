import tkinter as tk

root = tk.Tk()

button=tk.Button(root)
button.config(text = "I am a button", width = 100, height = 10)
button.pack()


root.mainloop()
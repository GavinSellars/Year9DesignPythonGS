import tkinter as tk

root = tk.Tk()

title=tk.Label(root, text = "Title")
title.config(fg = "red", bg = "black", width = 40, height = 30)
title.pack(fill = tk.BOTH)


root.mainloop()
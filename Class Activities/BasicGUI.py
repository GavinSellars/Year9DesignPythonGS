import tkinter as tk

print("Start Program")
root = tk.Tk() #builds your main window

#Widget/Element is an element in a GUI, Button, Textbox, input box, slider

#Step 1: Construct the widget.
btn1 = tk.Button(root)
#Step 2: Configure the widget.
btn1.config(text = "I am a button", width = 100, height = 10)
#Step 3: Place the widget - pack(), grid(),
btn1.pack()

output = tk.Text()
output.config(width = 100, height = 20)
output.pack()

check = tk.Checkbutton(root, text = "Make checkmark appear")
check.config(anchor=tk.W)
check.pack(fill = tk.BOTH)


root.mainloop()

print("END PROGRAM")

import tkinter as tk




titlesize=38
labelsize=20
labelcolour="#6fa8dc"


itemcat1_1 = "sunchips"
itemcat1_2 = "popcorners"

itemcat2_1 = "white milk"
itemcat2_2 = "chocolate milk"


var=tk.StringVar() 




root = tk.Tk()

title = tk.Label(root, text = "Lower Dining Hall Expense Tracker", bg = "#3d85c6", font = ("arial", titlesize))
title.grid(row = 0, column = 0, columnspan = 4)

itemcats = tk.Label(root, text = "Item Categories", bg =labelcolour, font = ("arial", labelsize))
itemcats.grid(row = 1, column = 0, ) 

budquestion = tk.Label(root, text = "Have you gone over your budget?", bg =labelcolour, font = ("arial", labelsize))
budquestion.grid(row = 1, column = 1)

currentbud = tk.Label(root, text = "Current Budget", bg = labelcolour, font = ("arial", labelsize))
currentbud.grid(row = 1, column = 2)

budleft= tk.Label(root, text = "How much left", bg = labelcolour, font = ("arial", labelsize))
budleft.grid(row = 1, column = 3)

itemcat1=tk.OptionMenu(root,var,itemcat1_1, itemcat1_2)
itemcat1.grid(row = 2, column = 0)

itemcat2=tk.OptionMenu(root, var, itemcat2_1, itemcat2_2)
itemcat2.grid(row = 2, column = 1)

budanswer = tk.Text(root, state = disables)












root.mainloop()
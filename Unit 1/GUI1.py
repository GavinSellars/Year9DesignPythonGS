import tkinter as tk


#variables
titlesize=38
labelsize=20
labelcolour="#6fa8dc"


itemcat1_1 = "sunchips"
itemcat1_2 = "popcorners"

itemcat2_1 = "white milk"
itemcat2_2 = "chocolate milk"


#functions

def changebudgetfunction():
	currentbudget = input()
	int(currentbudget)







root = tk.Tk()

var=tk.StringVar() 

title = tk.Label(root, text = "Lower Dining Hall Expense Tracker", bg = "#3d85c6", font = ("arial", titlesize))
title.grid(row = 0, column = 0, columnspan = 5, sticky = "nesw")

itemcats = tk.Label(root, text = "Item Categories", bg =labelcolour, font = ("arial", labelsize))
itemcats.grid(row = 1, column = 0, columnspan = 2, sticky = "nesw") 

budquestion = tk.Label(root, text = "Have you gone over your budget?", bg =labelcolour, font = ("arial", labelsize))
budquestion.grid(row = 1, column = 2, sticky = "nesw")

currentbud = tk.Label(root, text = "Current Budget", bg = labelcolour, font = ("arial", labelsize))
currentbud.grid(row = 1, column = 3, sticky = "nesw")

budleft= tk.Label(root, text = "How much left", bg = labelcolour, font = ("arial", labelsize))
budleft.grid(row = 1, column = 4, sticky = "nesw")

itemcat1=tk.OptionMenu(root,var,itemcat1_1, itemcat1_2)
itemcat1.grid(row = 2, column = 0)

itemcat2=tk.OptionMenu(root, var, itemcat2_1, itemcat2_2)
itemcat2.grid(row = 2, column = 1)

budanswer = tk.Text(root, state = "disabled", height = 1, width = 4)
budanswer.grid(row = 3, column = 2)

currentbud = tk.Text(root, state = "disabled", height = 1, width = 4)
currentbud.grid(row = 2, column = 3)

budchange = tk.Text(root, state = "disabled", height = 1, width = 4)
budchange.grid(row = 2, column = 4)

itemcat3=tk.OptionMenu(root,var, itemcat1_1)
itemcat3.grid(row = 3, column = 0)

itemcat4=tk.OptionMenu(root, var, itemcat1_1)
itemcat4.grid(row = 3, column = 1)















root.mainloop()
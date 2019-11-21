import tkinter as tk




#variables
titlesize=36
labelsize=18
labelcolour="#6fa8dc"
submitcolour="#9fc5e8"
weeklyspending = 0
schoolyearspending = 0
totalspending = 0


#items
itemcat1_1 = "sunchips"
itemcat1_2 = "popcorners"

itemcat2_1 = "white milk"
itemcat2_2 = "chocolate milk"


#functions

def changebudgetfunction():
	currentbudget = input()
	int(currentbudget)


def resetweek():
	weeklyspending.set(0.0)
	monthlyspendingprediction.set(0.0)

def resetmonth():
	monthlyspending.set(0.0)











root = tk.Tk()
root.configure(background = 'grey')

totalspending = tk.DoubleVar(root)
str(totalspending)

weeklyspending = tk.DoubleVar(root)
str(weeklyspending)

monthlyspending = tk.DoubleVar(root)
str(monthlyspending)


monthlyspendingprediction = tk.DoubleVar(root)
str(monthlyspendingprediction)
monthlyspendingprediction = weeklyspending*30/28
monthlyspendingprediction = round(monthlyspendingprediction, 2)


schoolyearspendingprediction = tk.DoubleVar(root)
str(schoolyearspendingprediction)
schoolyearspendingprediction = monthlyspending*10
schoolyearspendingprediction = round(monthlyspendingprediction, 2)


#stringvar fuctions for my item categories
var3=tk.StringVar() 
var4=tk.StringVar() 
var5=tk.StringVar() 
var6=tk.StringVar() 
var7=tk.StringVar() 
var8=tk.StringVar() 


#title
title = tk.Label(root, text = "Lower Dining Hall Expense Tracker", bg = "#3d85c6", font = ("georgia", titlesize))
title.grid(row = 0, column = 0, columnspan = 6, sticky = "nesw")

#label saying item Categories
itemcats = tk.Label(root, text = "Item Categories", bg =labelcolour, font = ("georgia", labelsize))
itemcats.grid(row = 1, column = 0, columnspan = 2) 

#Budget related
budquestion = tk.Label(root, text = "Have you gone over your budget?", bg =labelcolour, font = ("georgia", labelsize))
budquestion.grid(row = 1, column = 2)

currentbud = tk.Label(root, text = "Current Budget", bg = labelcolour, font = ("georgia", labelsize))
currentbud.grid(row = 1, column = 3)

budleft= tk.Label(root, text = "How much left", bg = labelcolour, font = ("georgia", labelsize))
budleft.grid(row = 1, column = 4)

budanswer = tk.Text(root, bg = "white", highlightbackground = "grey", state = "disabled", height = 2, width = 10)
budanswer.grid(row = 3, column = 2, rowspan = 3, sticky = "nesw")

currentbud = tk.Text(root, bg = "white", highlightbackground = "grey", state = "disabled", height = 2, width = 10)
currentbud.grid(row = 3, column = 3, rowspan = 3, sticky = "nesw")

budleft = tk.Text(root, bg = "white", highlightbackground = "grey", state = "disabled", height = 2, width = 10)
budleft.grid(row = 3, column = 4, rowspan = 3, sticky = "nesw")

budchange = tk.Label(root, text = "Change the weekly budget to...", bg = labelcolour, font = ("georgia", labelsize))
budchange.grid(row = 1, column = 5)

budchangevalue = tk.Text(root, bg = "white", highlightbackground = "grey", height = 2, width = 10)
budchangevalue.grid(row = 3, column = 5, rowspan = 3, sticky = "nesw")

#items
itemcat3=tk.OptionMenu(root,var3, itemcat1_1)
itemcat3.configure(bg="grey")
itemcat3.grid(row = 3, column = 0)

itemcat4=tk.OptionMenu(root, var4, itemcat1_1)
itemcat4.configure(bg="grey")
itemcat4.grid(row = 3, column = 1)

itemcat5=tk.OptionMenu(root,var5,itemcat1_1, itemcat1_2)
itemcat5.configure(bg="grey")
itemcat5.grid(row = 4, column = 0)

itemcat6=tk.OptionMenu(root, var6, itemcat2_1, itemcat2_2)
itemcat6.configure(bg="grey")
itemcat6.grid(row = 4, column = 1)

itemcat7=tk.OptionMenu(root,var7, itemcat1_1)
itemcat7.configure(bg="grey")
itemcat7.grid(row = 5, column = 0)

itemcat8=tk.OptionMenu(root, var8, itemcat1_1)
itemcat8.configure(bg="grey")
itemcat8.grid(row = 5, column = 1)

#submit buttons
submititems = tk.Button(root, text = "submit", highlightbackground = submitcolour)
submititems.grid(row = 7, column = 0, columnspan = 2, sticky = "nesw")

submitbudchangevalue = tk.Button(root, text = "submit", highlightbackground = submitcolour)
submitbudchangevalue.grid(row = 7, column = 5, columnspan = 2, sticky = "nesw")

#spacing
spacing1 = tk.Text(root, bg = "grey", highlightbackground = "grey", state = "disabled", height = 1, width = 10)
spacing1.grid(row = 6, column = 0)

spacing2 = tk.Text(root, bg = "grey", highlightbackground = "grey", state = "disabled", height = 1, width = 10)
spacing2.grid(row = 2, column = 0)

spacing3 = tk.Text(root, bg = "grey", highlightbackground = "grey", state = "disabled", height = 1, width = 10)
spacing3.grid(row = 8, column = 0)



#expense tracking
totalspendingwidget = tk.Label(root, text = "Current total spending", bg =labelcolour, font = ("georgia", labelsize))
totalspendingwidget.grid(row = 9, column = 0, columnspan = 4, sticky = "nesw")

totalspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", state = "disabled", height = 2, width = 10, textvariable = weeklyspending, font = ("goergia", 20))
totalspendingvalue.grid(row = 10, column = 0, columnspan = 4, rowspan = 2, sticky = "nesw")

weekspending = tk.Label(root, text = "Spending this week", bg =labelcolour, font = ("georgia", labelsize))
weekspending.grid(row = 12, column = 0, columnspan = 4, sticky = "nesw")

weekspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", state = "disabled", height = 2, width = 10, textvariable = weeklyspending, font = ("goergia", 20))
weekspendingvalue.grid(row = 13, column = 0, columnspan = 4, sticky = "nesw")

monthspending = tk.Label(root, text = "Spending this month", bg =labelcolour, font = ("georgia", labelsize))
monthspending.grid(row = 15, column = 0, columnspan = 4, sticky = "nesw")

monthspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", state = "disabled", height = 2, width = 10, textvariable = monthlyspending, font = ("goergia", 20))
monthspendingvalue.grid(row = 16, column = 0, columnspan = 4, sticky = "nesw")





#predictions
predictions = tk.Label(root, text = "Predictions", bg =labelcolour, font = ("georgia", labelsize))
predictions.grid(row = 9, column = 4, columnspan = 2, sticky = "nesw")

totalspendingvalue = tk.Label(root, text = "If you continue spending at this rate...", bg = "white", height = 2, width = 10)
totalspendingvalue.grid(row = 10, column = 4, columnspan = 4, rowspan = 2, sticky = "nesw", ipady = 10)

predictionsmonth = tk.Label(root, text = "In a month you will have spent...", bg =labelcolour, font = ("georgia", labelsize))
predictionsmonth.grid(row = 12, column = 4, columnspan = 2, sticky = "nesw")

predictionsmonthvalue = tk.Label(root, bg = "white", state = "disabled", height = 2, width = 10, highlightbackground = "grey", textvariable = monthlyspendingprediction, font = ("goergia", 20))
predictionsmonthvalue.grid(row = 13, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)

predictionsschoolyear = tk.Label(root, text = "In a year you will have spent...", bg =labelcolour, font = ("georgia", labelsize))
predictionsschoolyear.grid(row = 15, column = 4, columnspan = 2, sticky = "nesw")

predictionsschoolyearvalue = tk.Label(root, bg = "white", state = "disabled", height = 2, width = 10, highlightbackground = "grey", textvariable = schoolyearspendingprediction, font = ("goergia", 20))
predictionsschoolyearvalue.grid(row = 16, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)


#resets
resetweek = tk.Button(root, text = "Reset Week", highlightbackground = "grey", command = resetweek)
resetweek.grid(row = 18, column = 0)

resetmonth = tk.Button(root, text = "Reset Month", highlightbackground = "grey", command = resetmonth)
resetmonth.grid(row = 18, column = 1)

#dont forget to say thank you message

thankyoumessage = tk.Label(root, text = "Don’t forget say thank you after you purchase your items!", bg = "grey", font = ("georgia", 12, "bold"))
thankyoumessage.grid(row = 18, column = 3, columnspan = 2)















root.mainloop()
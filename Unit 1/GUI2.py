import tkinter as tk




#variables
titlesize=50
labelsize=20
labelcolour="#6fa8dc"
submitcolour="#9fc5e8"
weeklyspending = 0
monthlyspending = (0+weeklyspending)
totalspending = (0+weeklyspending)
monthlyspendingprediction = (weeklyspending*30/7)
monthlyspendingprediction = round(monthlyspendingprediction, 2)
schoolyearspendingprediction = (monthlyspending*10)
newbudget = 0
budgetleft = (newbudget-weeklyspending)


#items
chips = ("Chips", "Sunchips", "Popcorners", "Hardbite")

drinks = ("Drinks","Herbal Tea", "Coffee", "Chocolate milk", "White milk", "xmL perrier", "perrier ymL")

wheat = ("Wheat", "Cookie", "Muffin", "Croissant")

frozen = ("Frozen", "Rasberry ice cream", "Lemon ice cream", "Chocolate ice cream")

example = ("Example")






#functions
def resetweek():
	global weeklyspending

	weeklyspending =  0.00
	weekspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = weeklyspending, font = ("georgia", 35))
	weekspendingvalue.grid(row = 13, column = 0, columnspan = 4, sticky = "nesw")
	
	global monthlyspendingprediction
	monthlyspendingprediction = 0.00
	predictionsmonthvalue = tk.Label(root, bg = "white", height = 2, width = 10, highlightbackground = "grey", text = monthlyspendingprediction, font = ("georgia", 35))
	predictionsmonthvalue.grid(row = 13, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)

	global budgetleft

	budgetleft = (newbudget-weeklyspending)
	budleft = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = budgetleft, font = ("georgia", 35))
	budleft.grid(row = 3, column = 4, rowspan = 3, sticky = "nesw")

def resetmonth():
	global monthlyspending

	monthlyspending = 0.00
	monthspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = monthlyspending, font = ("georgia", 35))
	monthspendingvalue.grid(row = 16, column = 0, columnspan = 4, sticky = "nesw")

	global schoolyearspendingprediction

	schoolyearspendingprediction = 0.00
	predictionsschoolyearvalue = tk.Label(root, bg = "white", height = 2, width = 10, highlightbackground = "grey", text = schoolyearspendingprediction, font = ("georgia", 35))
	predictionsschoolyearvalue.grid(row = 16, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)

	global weeklyspending

	weeklyspending =  0.00
	weekspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = weeklyspending, font = ("georgia", 35))
	weekspendingvalue.grid(row = 13, column = 0, columnspan = 4, sticky = "nesw")
	
	global monthlyspendingprediction
	monthlyspendingprediction = 0.00
	predictionsmonthvalue = tk.Label(root, bg = "white", height = 2, width = 10, highlightbackground = "grey", text = monthlyspendingprediction, font = ("georgia", 35))
	predictionsmonthvalue.grid(row = 13, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)

def changeweeklybudget():
	try:
		budchangevalue.config(bg = "white")
		global newbudget
		newbudget = float(budchangevalue.get())

		currentbud = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = newbudget, font = ("georgia", 35))
		currentbud.grid(row = 3, column = 3, rowspan = 3, sticky = "nesw")

		budchangevalue.delete(0, tk.END)
		budgetleft = (newbudget-weeklyspending)
		budleft = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = budgetleft, font = ("georgia", 35))
		budleft.grid(row = 3, column = 4, rowspan = 3, sticky = "nesw")

		invalidvalue = tk.Label(root, bg = "grey", width = 10, font = ("georgia", 35))
		invalidvalue.grid(row = 6, column = 5, sticky = "nesw")

		
		if newbudget >= weeklyspending:
			budanswer = tk.Label(root, bg = "green", highlightbackground = "grey", text = "You are under budget!", height = 2, width = 10, font = ("georgia", 30))
			budanswer.grid(row = 3, column = 2, rowspan = 3, sticky = "nesw")

		else:
			budanswer = tk.Label(root, bg = "red", highlightbackground = "grey", text = "You are over budget!", height = 2, width = 10, font = ("georgia", 30))
			budanswer.grid(row = 3, column = 2, rowspan = 3, sticky = "nesw")






	except:

		budchangevalue.config(bg = "red")
		budchangevalue.delete(0, tk.END)
		invalidvalue = tk.Label(root, bg = "red", text = "Numbers Only", width = 10, font = ("georgia", 35))
		invalidvalue.grid(row = 6, column = 5, sticky = "nesw")


def submititems():
	if var3.get()!=chips[0]:
		if var3.get()==chips[1]:
			var3.set(chips[0])
			global weeklyspending
			weeklyspending = weeklyspending + 2
			global monthlyspending
			monthlyspending = monthlyspending + 2
			global totalspending
			totalspending = totalspending + 2
			global monthlyspendingprediction
			monthlyspendingprediction = (weeklyspending*30/7)
			monthlyspendingprediction = round(monthlyspendingprediction, 2)
			global schoolyearspendingprediction
			schoolyearspendingprediction = (monthlyspending*10)
			global budgetleft
			budgetleft = (newbudget-weeklyspending)

			totalspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = totalspending, font = ("georgia", 35))
			totalspendingvalue.grid(row = 10, column = 0, columnspan = 4, rowspan = 2, sticky = "nesw")


			weekspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = weeklyspending, font = ("georgia", 35))
			weekspendingvalue.grid(row = 13, column = 0, columnspan = 4, sticky = "nesw")

			monthspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = monthlyspending, font = ("georgia", 35))
			monthspendingvalue.grid(row = 16, column = 0, columnspan = 4, sticky = "nesw")

			predictionsmonthvalue = tk.Label(root, bg = "white", height = 2, width = 10, highlightbackground = "grey", text = monthlyspendingprediction, font = ("georgia", 35))
			predictionsmonthvalue.grid(row = 13, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)

			predictionsschoolyearvalue = tk.Label(root, bg = "white", height = 2, width = 10, highlightbackground = "grey", text = schoolyearspendingprediction, font = ("georgia", 35))
			predictionsschoolyearvalue.grid(row = 16, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)

			budleft = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = budgetleft, font = ("georgia", 35))
			budleft.grid(row = 3, column = 4, rowspan = 3, sticky = "nesw")

			if newbudget >= weeklyspending:
				budanswer = tk.Label(root, bg = "green", highlightbackground = "grey", text = "You are under budget!", height = 2, width = 10, font = ("georgia", 30))
				budanswer.grid(row = 3, column = 2, rowspan = 3, sticky = "nesw")

			else:
				budanswer = tk.Label(root, bg = "red", highlightbackground = "grey", text = "You are over budget!", height = 2, width = 10, font = ("georgia", 30))
				budanswer.grid(row = 3, column = 2, rowspan = 3, sticky = "nesw")











root = tk.Tk()
root.configure(background = 'grey')





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

budleftquestion= tk.Label(root, text = "How much left", bg = labelcolour, font = ("georgia", labelsize))
budleftquestion.grid(row = 1, column = 4)

budanswer = tk.Label(root, bg = "white", highlightbackground = "grey", text = "", height = 2, width = 10, font = ("georgia", 30))
budanswer.grid(row = 3, column = 2, rowspan = 3, sticky = "nesw")

currentbud = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = newbudget, font = ("georgia", 35))
currentbud.grid(row = 3, column = 3, rowspan = 3, sticky = "nesw")

budleft = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = budgetleft, font = ("georgia", 35))
budleft.grid(row = 3, column = 4, rowspan = 3, sticky = "nesw")

budchange = tk.Label(root, text = "Change the weekly budget to...", bg = labelcolour, font = ("georgia", labelsize))
budchange.grid(row = 1, column = 5)

budchangevalue = tk.Entry(root, bg = "white", width = 10, font = ("georgia", 35))
budchangevalue.grid(row = 3, column = 5, rowspan = 3, sticky = "nesw")

invalidvalue = tk.Label(root, bg = "grey", width = 10, font = ("georgia", 35))
invalidvalue.grid(row = 6, column = 5, sticky = "nesw")

#items
itemcat3=tk.OptionMenu(root,var3, chips[0], chips[1], chips[2])
itemcat3.configure(bg="grey")
itemcat3.grid(row = 3, column = 0)
var3.set(chips[0])

itemcat4=tk.OptionMenu(root, var4, frozen[0], frozen[1], frozen[2], frozen[3])
itemcat4.configure(bg="grey")
itemcat4.grid(row = 3, column = 1)
var4.set(frozen[0])

itemcat5=tk.OptionMenu(root,var5, wheat[0], wheat[1], wheat[2], wheat[3])
itemcat5.configure(bg="grey")
itemcat5.grid(row = 4, column = 0)
var5.set(wheat[0])

itemcat6=tk.OptionMenu(root, var6, drinks[0], drinks[1], drinks[2], drinks[3], drinks[4], drinks[5])
itemcat6.configure(bg="grey")
itemcat6.grid(row = 4, column = 1)
var6.set(drinks[0])

itemcat7=tk.OptionMenu(root,var7, example)
itemcat7.configure(bg="grey")
itemcat7.grid(row = 5, column = 0)
var7.set(example)

itemcat8=tk.OptionMenu(root, var8, example)
itemcat8.configure(bg="grey")
itemcat8.grid(row = 5, column = 1)
var8.set(example)

#submit buttons
submititems = tk.Button(root, text = "submit", highlightbackground = submitcolour, command = submititems)
submititems.grid(row = 7, column = 0, columnspan = 2, sticky = "nesw")

submitbudchangevalue = tk.Button(root, text = "submit", highlightbackground = submitcolour, command = changeweeklybudget)
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

totalspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = totalspending, font = ("georgia", 35))
totalspendingvalue.grid(row = 10, column = 0, columnspan = 4, rowspan = 2, sticky = "nesw")

weekspendinglabel = tk.Label(root, text = "Spending this week", bg =labelcolour, font = ("georgia", labelsize))
weekspendinglabel.grid(row = 12, column = 0, columnspan = 4, sticky = "nesw")

weekspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = weeklyspending, font = ("georgia", 35))
weekspendingvalue.grid(row = 13, column = 0, columnspan = 4, sticky = "nesw")

monthspending = tk.Label(root, text = "Spending this month", bg =labelcolour, font = ("georgia", labelsize))
monthspending.grid(row = 15, column = 0, columnspan = 4, sticky = "nesw")

monthspendingvalue = tk.Label(root, bg = "white", highlightbackground = "grey", height = 2, width = 10, text = monthlyspending, font = ("georgia", 35))
monthspendingvalue.grid(row = 16, column = 0, columnspan = 4, sticky = "nesw")





#predictions
predictions = tk.Label(root, text = "Predictions", bg =labelcolour, font = ("georgia", labelsize))
predictions.grid(row = 9, column = 4, columnspan = 2, sticky = "nesw")

totalspendingvalue = tk.Label(root, text = "If you continue spending at this rate...", bg = "white", height = 2, width = 10, font = ("georgia", 20))
totalspendingvalue.grid(row = 10, column = 4, columnspan = 4, rowspan = 2, sticky = "nesw", ipady = 10)

predictionsmonth = tk.Label(root, text = "In a month you will have spent...", bg =labelcolour, font = ("georgia", labelsize))
predictionsmonth.grid(row = 12, column = 4, columnspan = 2, sticky = "nesw")

predictionsmonthvalue = tk.Label(root, bg = "white", height = 2, width = 10, highlightbackground = "grey", text = monthlyspendingprediction, font = ("georgia", 35))
predictionsmonthvalue.grid(row = 13, column = 4, columnspan = 4, sticky = "nesw", ipady = 10)

predictionsschoolyear = tk.Label(root, text = "In a school year you will have spent...", bg =labelcolour, font = ("georgia", labelsize))
predictionsschoolyear.grid(row = 15, column = 4, columnspan = 2, sticky = "nesw")

predictionsschoolyearvalue = tk.Label(root, bg = "white", height = 2, width = 10, highlightbackground = "grey", text = schoolyearspendingprediction, font = ("georgia", 35))
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
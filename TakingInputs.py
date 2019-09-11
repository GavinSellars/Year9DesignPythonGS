#This program will take two integers and multiply them

#Input
#All inputs start as strings
name = input("Please input your name: ")

a = input("Please input first number: ")
a = int(a) #self-referencing assignment statement
b = input("Please input second number: ")
b = int(b)
#Process
product = a * b
#Output
print("Hi, "+name)
print("The product of "+str(a)+" and "+str(b)+" is "+str(product)+".")
print("Thank you")
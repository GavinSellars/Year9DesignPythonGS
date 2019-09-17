import math
#Input
#What inputs are needed to calculate the volume of a cylinder?
print("Volume of a Cylinder Formula: ")
name = input("What is your name: ")   #takes users name

radius = input("Input radius(cm): ")  #input
radius = (float)(radius)     #cast to int

height = input("Input height(cm): ") #input
height = (float)(height)     #cast to int
#Process
#What formula is used to calculate the volume of a cylinder?

volume = math.pi*radius*radius*height 
#Output
#What is important about the output?


print("The volume is:",volume)
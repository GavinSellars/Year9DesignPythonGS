import math

#Input
#What inputs are needed to calculate the volume of a cylinder?
print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")
name = input("\tWhat is your name: ")   #takes users name

radius = input("\n\tInput radius(cm): ")  #input
radius = (float)(radius)     #cast to int

height = input("\tInput height(cm): ") #input
height = (float)(height)     #cast to int
#Process
#What formula is used to calculate the volume of a cylinder?

volume = math.pi*radius*radius*height 
volume=round(volume,2)
#Output
#What is important about the output?

print("\n\t\tHi "+name+"!")
print("\t\tGiven a cylinder with:")
print("\t\tRadius = ", radius)
print("\t\tHeight = ", height)
print("\n\t\tThe volume is: "+str(volume))
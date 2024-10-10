# using a function create a program that calculates the volume of a cylinder.

radius=int(input("enter the radius:"))
height=int(input("enter the height:"))
import math
pie= math.pi
volume= pie * radius ** 2 * height
print(volume)
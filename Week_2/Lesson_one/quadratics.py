# writing a program to solve the quadratic equation
# name: Kiptoo
# date: 2/20/2024
import math
a = float(input("enter the coeficient of first term"))
b = float(input("enter the coefficient of second term"))
c = float(input("enter the constant"))

d =(b**2) - 4*a*c
x_1=(-b + math.sqrt(d))/(2*a)
x_2=(-b - math.sqrt(d))/(2*a)
print("the equation of the quadratic equation",x_1)
print("the equation of the quadratic equation",x_2)
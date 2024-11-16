'''AREA OF SHAPES'''
import math
print("c=circle\nt=triangle\ns=square\nr=rectangle\np=parallelogram\nz=trapezoid")
shape=input("Enter the shape code  : ")
if shape=="c":
	r=float(input("Enter the radius of the circle (cm): "))
	area=math.pi*(r**2)
	print("Area of the circle is ",area,"cm")
elif shape=="t":
	b=float(input("Enter the base of the triangle(cm) : "))
	h=float(input("Enter the height of the triangle(cm) : "))
	area=(1/2)*b*h
	print("Area of the triangle is ",area,"cm")
elif shape=="s":
	side=float(input("Enter the side of the square(cm): "))
	area=side**2
	print("Area of the square is",area,"cm")
elif shape=="r":
	l=float(input("Enter the length of the rectangle (cm): "))
	b=float(input("Enter the width of the rectangle (cm): "))
	area=l*b
	print("Area of the rectangle is ",area,"cm")
elif shape=="p":
	b=float(input("Enter the base of the parallelogram(cm) : "))
	h=float(input("Enter the height of the parallelogram (cm): "))
	area =b*h
	print("Area of the parallelogram is ",area,"cm")
elif shape=="z":
	a=float(input("Enter the short base of the trapezoid (cm): "))
	b=float(input("Enter the long base of the trapezoid(cm) : "))
	h=float(input("Enter the height of the trapezoid(cm) : "))
	area=(1/2)*(a+b)*h
	print("Area of the trapezoid is",area,"cm")
else:
	print("invalid shape")

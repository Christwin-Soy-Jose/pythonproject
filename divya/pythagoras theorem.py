'''
Author:Divya Kuriakose
Date:16-11-2024
Program to find hypotenuse using pythagoras theorem
'''

import math
base=int(input("Enter the base:"))
altitude=int(input("Enter the altitude:"))
hypotenuse=math.sqrt(base*base + altitude*altitude)
print(f"The hypotenuse of the given right angled triangle is: {hypotenuse}")
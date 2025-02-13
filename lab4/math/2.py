#Write a Python program to calculate the area of a trapezoid.

import math

height ,first, second = map(int,input().split())

def trap(a,b,h):
    area = ((a+b)/2)*h
    return area

print(trap(height,first,second))

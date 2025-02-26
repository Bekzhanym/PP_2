#Write a Python program to write a list to a file.
items = ['Conor','Pourier','Islam','Shavkat']

import os 
file = open('2.txt','w')
for i in items:
    file.write(i + "\n")
file.close

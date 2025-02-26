#Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path
import os

path = r'C:\Users\bekzh\Desktop\flutter\flutter_application_1\android'

print('Exist', path, os.F_OK)
print ('Readable', path, os.R_OK)
print('Writable', path, os.W_OK)
print('Executable', path, os.EX_OK)



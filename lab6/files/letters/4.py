#Write a Python program to count the number of lines in a text file.

with open('2.txt', 'r') as file:
    contents = file.read()
    line_count = contents.count('\n')
    print("Total lines:", line_count)
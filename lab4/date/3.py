#Write a Python program to drop microseconds from datetime.
from datetime import date, timedelta
delta = timedelta(
     days=50,
     seconds=27,
     microseconds=10,
     milliseconds=29000,
     minutes=5,
     hours=8,
     weeks=2
)

print(delta.microseconds)

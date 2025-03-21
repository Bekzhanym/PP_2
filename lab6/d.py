#Write a Python program that invoke square root function after specific milliseconds.
#Sample Input:
#25100
#2123
#Sample Output:
#Square root of 25100 after 2123 miliseconds is 158.42979517754858

import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Переводим миллисекунды в секунды
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

# Ввод данных
num = int(input())
delay = int(input())

# Вызываем функцию
delayed_sqrt(num, delay)
#delay отложенный
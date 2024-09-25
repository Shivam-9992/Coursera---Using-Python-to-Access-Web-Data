'''
In this assignment you will read through and parse a file with text and numbers.
You will extractall the numbers in the file and compute the sum of the numbers.
'''

import re

file = open("py.txt")

text = file.read()

number_final = re.findall('[0-9]+',text)

total = 0
for i in number_final:
    i = int(i)
    total = total + i;

print(total)

file.close()

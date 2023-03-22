# Python has many built-in modules
import sys

print(sys.path)

import re # import the regular expressions module
text = "Mi numero de teléfono es 311 213 312, el código del país es 57, mi numero de la suerte es 3"
result = re.findall('[0-9]+', text)
print(result)

import time # import the time module to work with dates a timezones in python
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1, 1, 2, 2, 1, 1, 3, 3, 4, 21]
counter = collections.Counter(numbers) # Counts how many times an item in the iterable apears
print(counter)
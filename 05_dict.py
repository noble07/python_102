# Dictionaries comprehensions
import random

my_dict = {}
for i in range(1, 5):
    my_dict[i] = i*2

print(my_dict)

# With comprehension
my_dict_v2 = {i: i*2 for i in range(1, 5)}
print(my_dict_v2)

countries = ['col', 'mex', 'bol', 'pe']
print({country: random.randint(1, 100) for country in countries})

names = ['juan', 'camilo', 'patricia']
ages = [25, 56, 12]

print({name: age for name, age in zip(names, ages) })
# or
print(dict(zip(names, ages)))
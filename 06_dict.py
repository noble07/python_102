import random

countries = ['col', 'mex', 'bol', 'pe']
population_dict = {country: random.randint(1, 100) for country in countries}
print(population_dict)

# Dictionary comprehension with an if statement
result = {country: population for country, population in population_dict.items() if population >= 20}
print(result)

text = 'Hola, soy Juan'
unique = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique)
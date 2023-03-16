# Sets are an unordered collection with no duplicates elements
set_countries = {'col', 'mex', 'bol', 'col'} # Only store one 'col' element
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 234, 676}
print(set_numbers)

set_types = {1, 'hello', False, 12.45}
print(set_types)

# Transforming to sets
set_from_string = set('hoola') # Creates a set each character separated and with no duplicates
print(set_from_string)
print(type(set_from_string))


set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)
print(type(set_from_tuples))

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
print(type(set_numbers))

unique_numbers = list(set_numbers)
print(unique_numbers)
print(type(unique_numbers))
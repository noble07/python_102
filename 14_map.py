numbers = [1, 2, 3 ,4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i*2)

print(numbers_v2)

# map() applies a function to each element of an iterable
# list() is used for better printing beacause map returns a map object reference
print(list(map(lambda x: x*2, numbers)))

number_2 = [5, 6, 7]

# It also can take multiples iterables, stops when the shortest iterable is exhausted
result = map(lambda x, y: x + y, numbers, number_2)
print(list(result))
import functools

numbers = [1, 2, 3, 4]

# reduce() works similar to the reduce function of JS
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)
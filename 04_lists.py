# List comprehension
numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)

# With lists comprehension
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

# We can also operate with the elements as the loop
print([element*2 for element in range(1, 11)])

# Also we can add logical statments
print([i*2 for i in range(1, 11) if i%2 == 0])
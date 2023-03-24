for i in range(1, 10):
    print(i)

my_iter = iter(range(1, 4)) # Allows to manage the iteration manually
print(my_iter)

print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3
print(next(my_iter)) # Throws exception (StopIteration)
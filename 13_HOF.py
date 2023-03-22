# Higher Order Functions

def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)


# Using lambdas
print(high_ord_func(2, lambda x: x + 1))
print(high_ord_func(2, lambda x: x + 3))
print(high_ord_func(2, lambda x: x * 3))
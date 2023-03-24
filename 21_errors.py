# Errors examples

# print(0 / 0)) SyntaxError
# print(0 / 0) ZeroDivisionError
# print(result) NameError

""" suma = lambda x, y: x + (y * 2)
assert suma(2, 2) == 4 # AsseirtionError """

# Throw Exceptions
age = 10
if age < 18:
    raise Exception("No se permite menores de edad")
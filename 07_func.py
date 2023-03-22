print("Hola")

# def is used to create a function
def my_print(text):
    print(text * 2)

my_print("Este es mi texto")
my_print("Hola")

a = 10
b = 23

# A function can return parameters as a tuple
def suma(a, b):
    my_print(a+b)
    return a + b, a - b

# Here we depackage the tuple
res_sum, res_resta = suma(a, b)

print(res_sum, res_resta)
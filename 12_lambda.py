# Normal function
def increment(x):
    return x + 1

result = increment(10)
print(result)

# Lambdas con be assing to variables
# Normally lambdas are use as first-class citizens for higher order functions
increment_v2 = lambda x: x + 1

print(increment_v2(11))

# You can use multiples arguments inside a lambda
full_name = lambda name, last_name: f"{name.title()} {last_name.title()}"
print(full_name('juan', 'muñoz'))
""" price = 100 # Global scope

def increment():
    # price = price + 10 throws an UnboundLocalError because it redefined price as a local variable
    # and it's referenced before assignment
    print(price) # It prints price because is of global scope

print(price)
increment() """

price = 100

def increment():
    price = 200 # Defined price as a variable with a local scope
    price += 10
    return price

print(price)
price_2 = increment()
print(price_2)
print(price)

# test = 2
# there is no block scope
if True:
    test = 4
    print(test)

print(test)

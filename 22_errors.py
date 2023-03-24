# Catches the error and logs it in the except block
try:
  int(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
      raise Exception("No se permite menores de edad")
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
else:
  print("No exceptions were found") # Only executes this line if the try code didn't throw exceptions
finally:
  print("Always executes")

print("Hola")
from pkg.mod_1 import func_1, func_2 # Importing from packages from pkg.mod_2 import func_3, func_4
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())

print(func_3())
print(func_4())

import pkg
import pkg.mod_1 as mod1
print(pkg.URL) # URL it's a variable initialize on the __init__.py file
print(pkg.mod_1.func_1()) # Without the import on __init__.py this doesn't work
print(mod1.func_1()) # Also we can use aliases
# Default values to parameters
def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola' # Returning different values as a tuple

result, width, text = find_volume(width=10)
print(result, width, text)
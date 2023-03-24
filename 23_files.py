# Reading a file from python
file = open("./text.txt")
# print(file.read()) # Read the whole file
""" print(file.readline())
print(file.readline()) # Reads line per line
print(file.readline())
print(file.readline()) """

for line in file: # Iterates each line of the file
    print(line)

file.close() # Close the file stream

# A better way to open/close a file stream is:
with open("./text.txt") as file: # open the file stream and close it by itself
  for line in file: # Iterates each line of the file
      print(line)
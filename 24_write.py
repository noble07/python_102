with open("./text.txt", "r+") as file: # r+ mode allows to read and write the file 
  # w+ mode open the file with read and write mode but overwrites the whole file (creates a new file if not exist)
  for line in file:
      print(line)
  file.write("Nuevas cosas en este archivo\n")
  file.write("otra cosa\n")
  file.write("más lienas\n")
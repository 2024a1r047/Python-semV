# reate a text file “MyFile.txt” in python and ask the user to write separate 3 lines with three input statements from the user. 
file = open("MyFile.txt", "w")

line1 = input("Enter first line: ")
line2 = input("Enter second line: ")
line3 = input("Enter third line: ")

file.write(line1 + "\n")
file.write(line2 + "\n")
file.write(line3 + "\n")

file.close()

print("Data successfully written to MyFile.txt")
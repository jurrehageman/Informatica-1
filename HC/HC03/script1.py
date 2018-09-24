file_name = "input1.txt" #note that this is just a string.
file_object = open(file_name) #now a file object will be created.
#The file is not read yet.
print(file_object)

for line in file_object:
    line_cleaned = line.strip() #new lines stripped off
    print(line_cleaned)

file_object.close()

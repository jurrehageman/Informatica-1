#solution to excercise 2
#Jurre Hageman

#open file object
file_name = 'excercise2.txt'
file_object = open(file_name)

#loop through each line
for line in file_object:
    #print each line without empty lines
    print(line, end="")
#close the file_object
file_object.close()


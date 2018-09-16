#solution to excercise 2
#Jurre Hageman



#Define the filename 
file_name = "dna_sequence.txt"
#open file object
file_object = open(file_name)

#loop through each line
for line in file_object:
    #print each line without empty lines
    print(line, end="")
#close the file_object
file_object.close()


file_name = "input_sequence.txt"
file_name_output = "output_gc_content.txt"
file_obj = open(file_name)
GC_max = 0 #set variable GC max to 0
highest_GC_sequence = "" #this is set to an empty string

for line in file_obj:
    line = line.strip()
    G = line.count("G")
    C = line.count("C")
    GC = G + C
    perc_GC = GC / len(line) * 100
    perc_GC = round(perc_GC)
    print("processing", line, ", GC percentage:", perc_GC)
    if perc_GC > GC_max: #if the percentage is the highest
        GC_max = perc_GC #overwrite the highscore
        highest_GC_sequence = line #overwrite the sequence with the highest GC
        print("New record, highest GC sequence is:", highest_GC_sequence)
        print("New record, highest GC percentage:", GC_max)
file_obj.close() #close the file
print() #print empty line
print("The sequence with the highest GC value is:", highest_GC_sequence)
print("The Highest GC percentage is:", GC_max)

file_obj_out = open(file_name_output, "w")
print("The sequence with the highest GC value is:", highest_GC_sequence, file=file_obj_out)
print("The Highest GC percentage is:", GC_max, file=file_obj_out)
file_obj_out.close() #do not forget to close the file object!
print("Data written to:", file_name_output)

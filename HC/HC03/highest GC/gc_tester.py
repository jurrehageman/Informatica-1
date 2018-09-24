file_name = "input_sequence.txt"
file_name_output = "output_sequence.txt"
file_obj = open(file_name)
file_obj_out = open(file_name_output, "w")

#print(file_obj)
record_GC = 0
record_GC_seq = ""
for regel in file_obj:
    regel = regel.strip()
    G = regel.count("G")
    C = regel.count("C")
    GC = G + C
    nucleotides = len(regel)
    perc_GC = GC / nucleotides * 100
    perc_GC = round(perc_GC)
    print(regel, perc_GC)
    
    if perc_GC > record_GC:
        record_GC = perc_GC
        record_GC_seq = regel

        print("Joepie, een record",record_GC_seq, record_GC)
    #print(regel)
print()

print("record is:", record_GC_seq, record_GC)
print("record is:", record_GC_seq, record_GC, file=file_obj_out)
file_obj.close()
file_obj_out.close()
print("data written to:", file_name_output)
print("shutdown...")
        
    

# solution for excersize 04 from Python lecture1

# define a DNA sequence and assign it to a variable
my_dna = "atagcaggagtagccaggag"
# convert to RNA
my_rna = my_dna.replace('t', 'u')
# make upper case
my_rna_upper = my_rna.upper()
# print to screen
print("RNA sequence: ", my_rna_upper)

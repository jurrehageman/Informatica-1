#solution for DNA convert

#imports
import sys

#ask user input
dna = "caacttttttt"
#now convert to upper:
dna = dna.upper()
#reverse
rev_dna = dna[::-1]
#complement:
bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
comp_dna = ""
for base in dna:
    comp_base = bases[base]
    #The following might look bad but the Python interpreter is optimized for string concatination
    comp_dna += comp_base 
#reverse complement:
rev_comp_dna = comp_dna[::-1]

print("original:", dna)
print("reverse:", rev_dna)
print("complement:", comp_dna)
print("reverse complement:", rev_comp_dna)


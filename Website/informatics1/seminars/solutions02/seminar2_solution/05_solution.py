# solution for excersize 05 from lecture1

# define a sequence and assign it to a variable
#seq = "ATGAGTAGGATAGGCTAGATGGCGATGAATT"
seq = "UCAUUAUCAGACGGCAGUUUAUUAUAUAUAU"

# convert to upper case:
seq_up = seq.upper()
# Always check variables by printing them to screen!
print("original sequence:", seq_up)

# check if we have a DNA sequence and not DNA
# DNA does not have the U in the sequence, so lets check this
# we use the string method find() to look for the U character
# find() returns a -1 if nothing was found, so we should set our condition equal to this value
if seq_up.find("U") == -1:
    # Using indentation we can define here our block that should be executed if the previous line evaluated to true

    # print that the sequence is DNA and print the sequence to the screen
    print("Sequence is DNA: ", seq_up)

else:
    # Change the U from RNA to the T in DNA and save it in a new variable
    DNA = seq_up.replace("U", "T")

    # Lastly, print that the sequence is RNA and print the sequence
    print("Sequence is RNA")
    print("Original sequence:", seq_up)
    print("DNA sequence:", DNA)

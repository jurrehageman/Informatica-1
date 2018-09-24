from random import randint,choice

def main():
    for x in range(1000):
        seq= ""
        for x in range(20):
            bases = 'TCAG'
            position = randint(0, 3)
            seq2 = bases[position]
            seq += seq2
        # open a file
        outfile = open('input_sequence.txt', 'a')
        outfile.write((seq) + '\n')
    # close the output file
    outfile.close()
    print("The data have been written to: input_sequence.txt")
main()




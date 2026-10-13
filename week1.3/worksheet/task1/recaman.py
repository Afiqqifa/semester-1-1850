# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
i=0
sequence=[0]

while len(sequence)<L:
    k=len(sequence)
    if sequence[-1]-k>0 and sequence[-1]-k not in sequence:
        sequence.append(sequence[-1]-k)
    else:
        sequence.append(sequence[-1]+k)

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
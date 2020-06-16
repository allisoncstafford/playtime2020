import sys

# write to a file
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
with open(output_file, 'w') as f:
    for i in range(len(my_letters)):
        if i < max_index -1:
            f.write(my_letters[i] + '\t')
        else:
            f.write(my_letters[i] + '\n')
print("Output written to file")
# import necessary packages
import sys
import glob
import os

# Read a single text file
# input_file = sys.argv[1]

# # print from file
# with open(input_file) as f:
#     for row in f:
#         print(row.strip())


# Read multiple text files
input_path = sys.argv[1]
for input_file in glob.glob(os.path.join(input_path, '*.txt')):
    with open(input_file, 'r', newline='') as f:
        for row in f:
            print(row.strip())
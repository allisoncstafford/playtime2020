list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
string = ''

for l in list_of_lists:
    max_i = len(l)
    for i in range(len(l)):
        if i < max_i - 1:
            string += l[i]+','
        else:
            string += l[i]+'\n'

print(string)


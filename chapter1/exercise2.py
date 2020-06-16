
produce = ['apple','banana', 'cucumber']
volumes = ['one piece', 'cup', 'handful']
d = {}

for i in range(len(produce)):
    if produce[i] not in d:
        d[produce[i]] = volumes[i]

print(d.items())
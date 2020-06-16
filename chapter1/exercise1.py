
saytheirnames = ['breonna', 'george', 'manuel']
ages = ['25', '31', '42']
gender = ['f', 'm', 'm']

combo = saytheirnames + ages + gender

for i, item in enumerate(combo):
    print(f"{i}: {item}")

# alternate
for i in range(len(combo)):
    print(f"{i}: {combo[i]}")
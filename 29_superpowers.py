distincts = set()

for a in range(2,101):
    for b in range(2,101):
        distincts.add(a**b)
print(len(distincts), distincts)
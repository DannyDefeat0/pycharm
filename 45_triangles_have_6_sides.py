tris = []
pents = []
hexs = []

matches = 0


for i in range(2,100000000):
    tris.append(int((i/2)*(i+1)))
    pents.append(int((i/2)*(3*i - 1)))
    hexs.append(int(i*(2*i - 1)))
    if tris[-1] in pents and tris[-1] in hexs:
        matches += 1
        if matches == 2:
            print(tris[-1])
            break

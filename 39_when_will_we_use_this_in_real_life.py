#p = a + b + c -> c = p - a - b
#solve for b
#a^2 + b^2 = c^2 = (p - a - b)^2
#b = p(2a - p)/(2a-2p)
#for each p, we consider each a, then ask if b is an integer, if it is, it's a solution, so we increase the solution count by 1

solutions = {}
p = 1000

for i in range(p):
    for a in range(i//2):
        b = (i*(2*a - i))/(2*a-2*i)
        if int(b) == b:
            if i not in solutions:
                solutions[i] = 1
            else:
                solutions[i] += 1

Keymax = max(zip(solutions.values(), solutions.keys()))[1]
print(Keymax)

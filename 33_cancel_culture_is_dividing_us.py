# step 1 find the four fractions
# these must be of the form ac / bc = a / b, where b > a
# step 2 multiply them and simplify

solutions = []

a = 1
b = 2
c = 1

while len(solutions) < 4 and a < 10:
    numerator = int(str(a) + str(c))
    denominator = int(str(c) + str(b))
    if numerator / denominator == a / b:
        solutions.append([numerator, denominator])
    if b != 9 or c != 9:
        if c != 9:
            c += 1
        else:
            c = 1
            b += 1
    else:
        a += 1
        b = a + 1
        c = 1

print(solutions)

numerator = solutions[0][0] * solutions[1][0] * solutions[2][0] * solutions[3][0]
denominator = solutions[0][1] * solutions[1][1] * solutions[2][1] * solutions[3][1]


def simplify_fraction(num1, num2):
    for i in range(2, min(num1, num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            print(num1, num2, i)
            num1 //= i
            num2 //= i
            return simplify_fraction(num1, num2)
    return num1, num2



print(simplify_fraction(numerator, denominator))

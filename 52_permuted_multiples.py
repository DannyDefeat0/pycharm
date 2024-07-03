def permutation(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


for i in range(1, 1000000):
    k = 2
    while k <= 6:
        if not permutation(i, i * k):
            break
        k += 1
    if k >= 6:
        print(i)
        break
"""
while True:
        if all(has_same_digits(x, k * x) for k in range(2, 7)):
            return x
        x += 1
"""
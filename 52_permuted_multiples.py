def permutation(num1, num2):
    #if two numbers are a permutation of each other they will sort to the same number
    return ''.join(sorted(str(num1))) == ''.join(sorted(str(num2)))


for i in range(1, 1000000):
    k = 2
    while k <= 6:
        if not permutation(i, i * k):
            break
        k += 1
    if k >= 6:
        print(i)
        break

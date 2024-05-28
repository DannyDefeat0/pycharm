def concatenator(n):
    product = 1
    string = ""
    for i in range(1,n+1):
        string += str(i)
        if len(string) > n:
            break
    d = 1
    print(str)
    while d <= n:
        print(d, product)
        product *= int(string[d-1])
        d *= 10
    print(string)
    return product

print(concatenator(1000000))
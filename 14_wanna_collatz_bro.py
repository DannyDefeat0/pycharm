def collatz_chain(number):
    chain_length = 1
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (3*number) + 1
        chain_length += 1
    return chain_length

max_chain = 1
for i in range(1,1000001):
    print(i)
    if collatz_chain(max_chain) < collatz_chain(i):
        max_chain = i
print(max_chain)




print(collatz_chain(13))
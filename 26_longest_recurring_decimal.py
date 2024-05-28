def longest_recurring(number):
    remainders = [10]
    #use long division, find the remainder of the current number, multiply by ten, repeat until we have a repeated remainder
    while ((remainders[-1]) % number)*10 not in remainders:
        remainders.append((remainders[-1] % number)*10)
    return len(remainders)-remainders.index((remainders[-1] % number)*10)

cycle_length = 0
index = 0
for i in range(1, 1000):
    if longest_recurring(i) >= cycle_length:
        cycle_length, index = longest_recurring(i), i
print(index)
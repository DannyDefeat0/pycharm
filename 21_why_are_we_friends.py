divisor_sums = {2:1}
friendly_sums = 0

for i in range(3, 10000):
    proper_divisor_sum = 0
    for k in range(1,i):
        if i % k == 0:
            proper_divisor_sum += k
    if proper_divisor_sum != 1:
        divisor_sums[i] = proper_divisor_sum
        if proper_divisor_sum in divisor_sums and proper_divisor_sum != i:
            if divisor_sums[proper_divisor_sum] == i:
                print(i, proper_divisor_sum)
                friendly_sums += i + proper_divisor_sum
print(divisor_sums)
print(friendly_sums)

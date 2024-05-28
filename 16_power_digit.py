#print(len(str(2**1000)))
#did this to gut check length, looks small so we can brute force this
def power_digit_sum(n,k):
    sum = 0
    for i in range(0, len(str(n**k))):
        sum += int(str(n**k)[i])
    return sum

print(power_digit_sum(2, 1000))


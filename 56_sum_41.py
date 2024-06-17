def digit_sum(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum


max_sum = 0

for a in range(1, 100):
    for b in range(1,100):
        if digit_sum(a**b) > max_sum:
            max_sum = digit_sum(a**b)

print(max_sum)
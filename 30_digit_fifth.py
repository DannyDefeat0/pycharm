total_sum = 0

for i in range(10,1000000):
    digit_sum = sum(int(digit)** 5 for digit in str(i))
    if digit_sum == i:
        total_sum += digit_sum
print(total_sum)

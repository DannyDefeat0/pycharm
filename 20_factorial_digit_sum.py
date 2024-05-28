def factorial_digit_sum(n):
    num = 1
    if n < 2:
        return "1"
    for i in range(2,n+1):
        num *= i
    num = str(num)
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    return digit_sum



print(factorial_digit_sum(100))
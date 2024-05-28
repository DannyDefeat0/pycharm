#observation, it takes 8 steps for loop 1, we check every 2nd number (3, 5, 7, 9), it takes 16 steps for the next loop
#so we check 13, 17, 21, 25, the next loop is 24, so we check intervals of 6,
#so the pattern is increasing the sum by 2 for each set of 4
#proof by guess and check


def math_is_for_squares(n):
    current = 1
    total = current
    step = 2
    while current < n ** 2:
        for _ in range(4):
            current += step
            total += current
        step += 2
    return total

print(math_is_for_squares(1001))
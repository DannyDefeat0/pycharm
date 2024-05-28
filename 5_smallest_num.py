def smallest_number_divisible_through_n(n):
    checks = [i for i in range(1,n+1)]
    solution = -1
    check = checks[-1]
    sum = n
    while solution == -1:
        if sum % check != 0:
            sum += n
            check = checks[-1]
        else:
            check -= 1
            if check == 1:
                return sum
    return solution

print(smallest_number_divisible_through_n(10))

print(smallest_number_divisible_through_n(20))
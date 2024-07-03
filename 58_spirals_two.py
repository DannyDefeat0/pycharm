import euler_functions

primes = euler_functions.sieve(int(1e9))

print(primes)


def prime_percent(set, prime_set):
    return len(set & prime_set)/len(set)


def prime_margin(percent):
    length = 1
    k = 0
    bottom_right = 1
    bottom_left = 1
    upper_left = 4*(k**2) + 1
    upper_right = 1

    bottom_right_diagonal = {1}
    upper_right_diagonal = {1}

    while length == 1 or prime_percent(bottom_right_diagonal | upper_right_diagonal, primes) >= percent:
        print(length," - " , prime_percent(bottom_right_diagonal | upper_right_diagonal, primes))
        length += 2
        k += 1
        bottom_right = bottom_right + (8 * k)
        bottom_left = bottom_left + (8*k) - 2
        upper_left = 4*(k**2) + 1
        if length == 3:
            new_upper_right = 3
        else:
            new_upper_right = upper_right + diff + 8
        diff = new_upper_right - upper_right
        upper_right = new_upper_right

        bottom_right_diagonal.update([upper_left,bottom_right])
        upper_right_diagonal.update([upper_right, bottom_left])
    return length

print(prime_margin(.1))
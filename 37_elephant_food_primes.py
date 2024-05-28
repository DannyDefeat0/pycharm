#meeting notes
#we start by defining a set for our solutions
#using sieve we generate a list of primes up to a million, which I guessed would be large enough
#we define two functions that truncate strings from either left or right and check if the result is still a prime using recursion
#We then DONT USE A WHILE LOOP to find our first 11 solutions greater 7 and stop there.

truncatable_primes = set()

n = 1000000
is_prime = [False, False] + [True] * (n - 1)
list_of_primes = [2]

for i in range(3, n + 1, 2):
    if is_prime[i]:
        list_of_primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
print(list_of_primes)


def left_truncate(string, prime_list):
    if len(string) > 1:
        if int(string) not in prime_list:
            return False
        else:
            string = string[1:]
            return left_truncate(string, prime_list)
    return int(string[len(string)-1]) in prime_list


def right_truncate(string, prime_list):
    if len(string) > 1:
        if int(string) not in prime_list:
            return False
        else:
            string = string[:len(string)-1]
            return right_truncate(string, prime_list)
    return int(string[0]) in prime_list

print(right_truncate("257",list_of_primes))
print(left_truncate("257",list_of_primes))


for prime in list_of_primes:
    if prime <= 7:
        pass
    else:
        if left_truncate(str(prime), list_of_primes) and right_truncate(str(prime), list_of_primes):
            truncatable_primes.add(prime)
            if len(truncatable_primes) == 11:
                break
print(truncatable_primes)
print(sum(truncatable_primes))

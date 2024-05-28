n = 98765322
is_prime = [False, False] + [True] * (n - 1)
list_of_primes = [2]

for i in range(3, n + 1, 2):
    if is_prime[i]:
        list_of_primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
print("primes done")

pandigital_dictionary = {i: ''.join(str(x) for x in range(1, i + 1)) for i in range(1, 10)}


def pandigital_check(number, length):
	number = ''.join(sorted(number))
	return number == pandigital_dictionary[length]

for prime in list_of_primes[::-1]:
    if pandigital_check(str(prime),len(str(prime))):
        print(prime)
        break




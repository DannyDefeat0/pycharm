import euler_functions

primes = [str(prime) for prime in list(euler_functions.sieve(10000)) if len(str(prime)) == 4]

prime_dict = {}

for prime in primes:
    if ''.join(sorted(prime)) in prime_dict:
        prime_dict[''.join(sorted(prime))].add(int(prime))
    else:
        prime_dict[''.join(sorted(prime))] = {int(prime)}


chains = []
last_diff = 0

for key in prime_dict:
    if len(prime_dict[key]) >= 3:
        sorted_list = sorted(prime_dict[key])  # Sort the list of primes
        for i in range(len(sorted_list) - 2):
            p1 = sorted_list[i]
            p2 = sorted_list[i + 1]
            p3 = sorted_list[i + 2]
            diff1 = p2 - p1
            diff2 = p3 - p2
            if diff1 == diff2:
                chain = str(p1) + str(p2) + str(p3)
                chains.append(chain)

print(chains)



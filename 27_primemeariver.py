def main(n,a,b):
    return n**2 + n*a + b

#Observations
#Since n = 0 must result in a prime, b must also be prime, so by default we are only checking prime values of b,
#and b is also likely to be odd since 2 is the only even prime
#All primes are positive, which means b is always positive
#At n=1 f(n) = 1 + a + b, which means a is usually odd, because if b isn't 2, 1+b will be even,
# and therefore a must be odd to make the sum odd
#This follows from the fact that all primes that aren't 2 are odd, otherwise they'd be divisible by 2.
#let's see if we can find a reason a must be prime
#if 1 + a + b is prime, then a is only the solutions


def prime_check(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

bs = []
for k in range(2,1001):
    if prime_check(k):
        bs.append(k)
print((bs))

ba_s = {}
for a in range(-999,1001,2):
    for b in bs:
        if prime_check(1+a+b):
            if b in ba_s:
                ba_s[b].append(a)
            else:
                ba_s[b] = [a]

global_max = [0,0,0]
for b in ba_s:
    for a in ba_s[b]:
        n = 0
        while prime_check(main(n,a,b)):
            n += 1
        if n >= global_max[0]:
            global_max = [n,a,b]
            n = 0
print(global_max[1]*global_max[2])

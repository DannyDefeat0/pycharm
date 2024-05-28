# only able to move right and down
# this is an n choose k problem, where n is the number of steps (40) with 20 decisions of left or down.
# Note - we don't actually care about the paths, just the number of different paths

def factorial(number):
    product = 1
    if number <= 1:
        return product
    for i in range(2, number + 1):
        product *= i
    return product


def n_choose_k(n, k):
    if k > n:
        return -1

    return factorial(n) // (factorial(k) * (factorial(n - k)))

print(n_choose_k(40, 20))
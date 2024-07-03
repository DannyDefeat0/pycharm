import math

def combinatorics_greater_than_k(n, k):
    greater_than_k_count = 0
    for i in range(n+1):
        for r in range(n+1):
            if math.comb(i, r) > k:
                greater_than_k_count += 1
    return greater_than_k_count

print(combinatorics_greater_than_k(100, 1e6))
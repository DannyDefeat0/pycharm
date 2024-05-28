cheat = 233168

def div_total(nums, limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(div_total(1000))

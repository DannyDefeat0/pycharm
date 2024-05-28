#I modified some dynamic programming code example to do this

def fib(max):
    nums = [0,1]
    total = 0
    while nums[-1] < max:
        nums.append(nums[-1] + nums[-2])
        if nums[-1] % 2 == 0:
            total += nums[-1]
    return total

def fib_sum(limit):
    a,b = 1,2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a+b
    return total


print(fib(4000000))
print(fib_sum(4000000))
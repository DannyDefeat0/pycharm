#I modified some of Andrew's code to do this


def fib_sum(limit):
    a,b = 1,2
    i = 3
    while len(str(b)) < limit:
        i += 1
        a, b = b, a+b
    return i

print(fib_sum(1000))
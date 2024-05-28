# all solutions must start with a number that is part of the solution, since base * 1 will always be present
# so we define a function to check for repeats and a function to check for pandigitals
# I figured 10000 seemed big enough

pandigital = "123456789"
pandigitals_found = set()


def pandigital_check(number):
    number = ''.join(sorted(number))
    return number == pandigital


def repeat_check(string):
    return len(string) == len(set(string))


for i in range(1, 10000):
    base = str(i)
    # more numbers are redundant than not
    if not repeat_check(base) or "0" in base:
        pass
    possible_answer = base
    n = 1
    while len(possible_answer) < 9 and n < 9:
        n += 1
        possible_answer += str(i * n)
        if not repeat_check(base):
            break
    if pandigital_check(possible_answer):
        pandigitals_found.add(possible_answer)

print(pandigitals_found)
print(max(pandigitals_found))

# I AM SPEED

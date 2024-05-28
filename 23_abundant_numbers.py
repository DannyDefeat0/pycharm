abundant_numbers = [12]
#This is my slowest solution so far, I couldn't think of any clever ways to speed this up.
for i in range(13, 28124):
    total = 0
    for k in range(1,(i//2)+1):
        if i % k == 0:
            total += k
            if total > i or k in abundant_numbers:
                abundant_numbers.append(i)
                break

print(abundant_numbers)
print(len(abundant_numbers))

non_abundant_numbers_sum = 0
#if 12 made it to the end, then the next value will make it there or lower
#if 18 fails at k - 1, then no value past 18 will exceed past that, so we can stop checking there.

abundantSums = set([])
for numOne in abundant_numbers:
    for numTwo in abundant_numbers:
        abSum = numOne + numTwo
        if abSum > 28123:
            break
        else:
            abundantSums.add(abSum)

# compile list of non-absolute sums
NonAbSums = [number for number in range(28124) if number not in abundantSums]






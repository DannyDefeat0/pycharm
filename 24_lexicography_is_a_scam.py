#We shouldn't need to calculate all permutations
#from the example we can observe 0 is at the from twice, as are 2 and 1.
#For each number we calculate the number of ways to arrange the nine numbers following it, and then try to predict where 1e6 falls.


def factorial(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    return product


numbers = list(range(10))
n = len(numbers)
answer = [0] * 10
remain = 1E6 - 1


for i in range(n):
    k = int(remain // factorial(n - 1 - i))
    #print(k, i)
    k = min(k, len(numbers) - 1)
    answer[i] = numbers[k]
    remain %= factorial(n - 1 - i)
    del numbers[k]

answer = ''.join(map(str, answer))
#print(answer)



#We can now apply this to numberr in the second spot

#We know the permutation starts with 2

#most optimal way of organizing
from itertools import permutations
perms = permutations(range(10))
sorted_perms = sorted(perms)
millionth_perm = sorted_perms[999999]
result = int(''.join(map(str, millionth_perm)))
print("result: ", result)


def factorial(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    return product

#consider making a helper library to just import these instead of copying and pasting

global_sum = 0

for i in range(3,1000000):
    sum = 0
    number = str(i)
    for digit in number:
        sum += factorial(int(digit))
        if sum > i:
            break
    if sum == i:
        global_sum += sum
        print(i)
print(global_sum)
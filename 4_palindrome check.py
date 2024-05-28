def palindrome(number):
    return str(number) == str(number)[::-1]

answer = 0

left = 999
right = 999

#tortoise
while right != 100:
    while left != 100:
        if palindrome(left*right):
            answer = max(left*right, answer)
        left -= 1
    right -= 1
    left = right
#hare
for i in range(100, 1000):
    for k in range(i,1000):
        product = i * k
        if palindrome(product) and product > answer:
            answer = product

print(answer)
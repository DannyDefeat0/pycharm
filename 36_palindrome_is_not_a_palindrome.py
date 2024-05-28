def palindrome_check(string):
    return string == string[::-1] and string[0] != "0"


def binary_conversion(num):
    return bin(num).replace("0b", "")

palidromic_sum = 0

for i in range(1,int(1e6)):
    if palindrome_check(str(i)):
        if palindrome_check(binary_conversion(i)):
            print(i, binary_conversion(i))
            palidromic_sum += i
print(palidromic_sum)
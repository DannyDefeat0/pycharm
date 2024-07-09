import euler_functions

lines = euler_functions.open_txt('https://projecteuler.net/resources/documents/0059_cipher.txt')
lines = lines[0].split(",")

codes = [int(line) for line in lines]

lowers = "abcdefghijklmnopqrstuvwxyz"


def valid_char(char):
    return (char in "0123456789 -()[]/,.+;:'?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" or char == '"')


def xor(char1, char2):
    return chr(char1 ^ char2)


messages = []

for a in lowers:
    for b in lowers:
        for c in lowers:
            #make our key
            ords = [ord(a), ord(b), ord(c)]
            message = ""
            for i in range(len(codes)):
                #each key has length 3 is repeated through the letters, so we use a, then b, then c, then a again, and so on
                k = i % 3
                char = xor(codes[i], ords[k])
                if not valid_char(char):
                    break
                else:
                    message += char
                    if i == len(codes) - 1:
                        print(a, b, c)
                        messages.append(message)


print(messages)

total = 0
for letter in messages[0]:
    total += ord(letter)
print(total)


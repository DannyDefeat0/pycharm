import codecs
decode_hex = codecs.getdecoder("hex_codec")
string = decode_hex("1c0111001f010100061a024b53535009181c")[0]

string_1 = string
string_2 = "686974207468652062756c6c277320657965"
a = bin(int(string_1))
b = bin(int(string_2))

longest = len(a) if len(a) > len(b) else len(b)

a = a.zfill(longest)
b = b.zfill(longest)

def xor(a,b):
    output = ""
    for i in range(len(a)):
        if int(a[i]) + int(b[i]) == 1:
            output += "1"
        else:
            output += "0"
    print(output)
    return hex(int(output))
print(xor(a,b))



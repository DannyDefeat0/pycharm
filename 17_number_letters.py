#There's one one in every ten numbers
#All but one number in a range of 100 has "and"

sub_twentys = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

post_twentys = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

total_length = 0
for i in range(1, 1001):
    num = str(i)
    current_string = ""
    if len(num) == 4:
        current_string += "onethousand"
    elif len(num) == 3:
        current_string += sub_twentys[int(num[0])] + "hundred"
        if num[1] != "0" or num[2] != "0":
            current_string += "and"
            if num[1] != "0":
                if num[1] == "1":
                    check = num[1] + num[2]
                    current_string += sub_twentys[int(check)]
                else:
                    current_string += post_twentys[int(num[1])]
            if num[2] != "0" and num[1] != "1":
                current_string += sub_twentys[int(num[2])]
    elif len(num) == 2 and i >= 20:
        current_string += post_twentys[int(num[0])] + sub_twentys[int(num[1])]
    else:
        current_string += sub_twentys[i]
    print(i, current_string)
    total_length += len(current_string)

print(total_length)




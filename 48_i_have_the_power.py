def power_string(n):
    total = 0
    for i in range(1, n+1):
        total += i**i
    return str(total)

#this is the ugliest thing I have ever made and I couldn't be happier
print(power_string(1000)[::-1][:10][::-1])
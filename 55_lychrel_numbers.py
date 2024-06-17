def lychrel_test(n,k):
    total = str(n + int(str(n)[::-1]))

    if total == total[::-1]:
        return False
    elif k == 50:
        return True
    else:
        return lychrel_test(int(total), k+1)





lychrel_count = 0

for i in range(1,int(1e4)+1):
    if lychrel_test(i, 0):
        lychrel_count += 1
        print(i)
print(lychrel_count)
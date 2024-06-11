from bisect import bisect_left

def pentagonal_number_generator(n):
    pentagonals = []
    for i in range(1,n+1):
        pentagonals.append(int(i*(3*i - 1)/2))
    return pentagonals

pents = pentagonal_number_generator(10000)

def bisect_search(list, item):
    #binary searching is faster because this list was presorted, unsure how long this ends up taking with just 'in"
   return (item <= list[-1]) and (list[bisect_left(list, item)] == item)

D = 10e99
#this is the largest possible gap in our current solution pool, we will gradually decrease this within our next loop

for i in pents:
    for k in pents:
        if bisect_search(pents, i+k) and bisect_search(pents, abs(i-k)):
            D = min(abs(i-k),D)
print(D)
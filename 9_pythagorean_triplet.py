#a**2 b**2 c**2 = 1000
#we need a^2 + b^2 = c^2 and a < b
#just loop through bs less than root(1000)
# since we know b we can actually solve for a and c by using liner algebra
# shoutout to irena
# n - b - c = a
# a^2 = c^2 - b^2
# => c = -(2 b^2 - 2 b n + n^2)/(2 b - 2 n)
# check this for 25, then we have a = n - b - (that shit above)
# now all we need to confirm is that a, b, c are all integer solutions

def pythagorean_triplets(n):
    solution = -1
    for b in range(1,n):
        #step 1 do math
        c = (-2*(b**2) + 2*b*n - n**2) / (2*b - 2*n)
        a = n - b - c
        #step 2 check math
        if int(a) == a and int(c) == c and c > 0 and a > 0:
            #step 3 finally, return math
            return int(a*b*c)
        else:
            print(a,b,c)
    return solution

print(pythagorean_triplets(1000))
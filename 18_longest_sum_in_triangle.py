triangle ="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = triangle.split("\n")
triangle = [[int(x) for x in line.split()] for line in triangle]

n = len(triangle)
sums = [triangle][-1][-1]
#start with the bottom row, it has no branches anyway
#Notably this does not efficiently solve problem 67, some ideas for improvement would keeping track of the max of each subpath
#A trivial example is as follows
#1
#2 3
#We only need to add 1 to 3 because 3 > 2. Similarly, any node connecting to one need only check node + (3 + 1), not node + (2 + 1)

for k in range(1,n):
    row = n-k-1
    #This variable looks like math
    new_sums = []
    for i in range(len(triangle[row])):
        shift = i * (2**(k-1))
        branches = 2**k
        for j in range(branches):
            new_sums.append(triangle[row][i] + sums[j+shift])
    sums = new_sums


print(max(sums))
print(len(sums))





def sum_square_diff(n):
    #both terms contained n^2 so the difference is the leftover terms in the sum squared
    #use the formulas to avoid needing a loop
    squares = 0
    sum = 0
    for i in range(1,n+1):
        sum += i
        squares += i**2
    return (sum**2) - squares

print(sum_square_diff(100))
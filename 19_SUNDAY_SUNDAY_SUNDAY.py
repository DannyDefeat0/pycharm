#The gap between Sundays is unaffacted by leap years, so if
#the first sunday is Jan 7th, 1900

months = [31, 28, 31, 30, 31, 30,31,31,30,31, 30, 31]

#This list is very intuitive and readable
sundays = []
year = 1900
day = 7
month = 0
#0th index month in dictionary
while year < 2001:

    #The first only happens once a month, so we just need to find the first Sunday next month
    #The first will only fall on a Sunday if day + 7n = current_days_in_month+1
    if month == 1:
        if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
            months[1] = 29
        else:
            months[1] = 28
        #write a check for leap year, this will only
    n = ((months[month] - day)//7 + 1)
    if day + 7*n - months[month] == 1 and year != 1900:
        sundays.append([month, year])
    day = day + 7*n - months[month]
    if month < 11:
        month += 1
    else:
        month = 0
        year += 1

print(sundays)
print(len(sundays))

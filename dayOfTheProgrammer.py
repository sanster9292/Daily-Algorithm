"""
PROBLEM URL:
https://www.hackerrank.com/challenges/day-of-the-programmer/problem

PROBLEM DESCRIPTION:
Apparently Russia switched from Julian calendar to Gregorian calendar after 1918.
So, you have to find the leap year before, on and after the implementation of the Gregorian calenda.

THOUGHTS:
This was a good exercise in modulo arithmetic, linking together conditionals concisely.


"""

y = int(input())

def dayOfProgrammer(y):
    year_400 = y%400
    year_four= y%4
    year_100 = y%100

    if (y <1918 and year_four ==0)or ((y > 1918) & (y%400 == 0 or ((y%4 == 0) & (y%100 != 0)))):
        year_string = '12.09.'+str(y)
        return year_string
    elif y == 1918:
        year_string = '26.09.1918'
        return year_string
    elif year_400 ==0 or ((year_four==0) and (year_100!=0)):
        year_string = '12.09.'+str(y)
        return year_string
    else:
        year_string = '13.09.'+str(y)
        return year_string



print(dayOfProgrammer(y))

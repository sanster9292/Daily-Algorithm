"""
PROBLEM URL:
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

PROBLEM DESCRIPTION:
We are given three number i,j and k. We have to calculate how many betuiful day
pairs there are in the range from i to j. We calculate this by reversing an integer,
calculate the differnce between the integer and its reverse and then divide it by k.
If k divides the integer evenly, then the integer and its reverse constitute a
beautiful day pair.

EXAMPLE:
i = 20 j = 23 k = 6
pairs = 2

i = 20 --> reverse = 02 --> differnce = 18 --> differnce/k = 18/6 =3

THOUGHTS:
The main thing that i had to think for this was how to reverse the integers in
consideration. I did this by coverting the integer to a string and then reversing
the string using the following line:
rev = int(str(num)[::-1])

Everything, after this was fairly rudimentary.
"""

start, end, div  = [int(x) for x in input().split()]

beaut = 0

for i in range(start, end+1):

    num = i
    rev = int(str(num)[::-1])
    print(i, rev)

    diff_div  = abs(num-rev)%div

    if diff_div == 0:
        beaut+=1

print('\n\n', beaut)

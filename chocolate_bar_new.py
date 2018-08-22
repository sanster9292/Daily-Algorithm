
"""
PROBLEM URL:
https://www.hackerrank.com/challenges/the-birthday-bar/problem

THE PROBLEM REVOLVES AROUND TRYING TO SLICE UP VALUES GIVEN AND ITERATE THROUGH
THEM TO SEE IF THE SUM OF CERTAIN CONTIGUOUS VALUES IS EQUAL TO A GIVEN VALUES.

PROBLEM STATEMENT:
Lily has a chocolate bar that she wants to share it with Ron for his birthday.
Each of the squares has an integer on it. She decides to share a contiguous segment
of the bar selected such that the length of the segment matches Ron's birth month
and the sum of the integers on the squares is equal to his birth day. You must determine
how many ways she can divide the chocolate.

MY THOUGHTS:
Intitally I thought about approaching this problem by comparing the sum of the  first and the
second value with the expected sum value. That only worked for some cases. What I then realized was
that I had to slice the numbers given into smaller windows and then iterate through those smaller windows.

WHAT I LEARNED:
Sliding Window and ways to implement it. 

"""
n = int(input())

s = input().split(' ')
s = [int(x) for x in s]

d, m = input().split(' ')
d, m = int(d), int(m)

def bday_choice(n,s,d,m):
    count = 0

    for i in range(0,n):
        total = sum(s[i:m+i])
        if total ==d:
            count+=1
    return count

print(bday_choice(n,s,d,m))


"""
PROBLEM URL:
https://www.hackerrank.com/challenges/migratory-birds/problem

PROBLEM DESCRIPTION:
In this problem, you will be given two inputs.

A number n the id numbers of birds migrating.
(For example, n= 6 means there are 6 different kinds of birds migrating.)

An array which is a record of how often a bird of each category was seen.
array = [1 4 4 4 5 3]
means that bird type 1 was seen once, bird type 4 was seen 3 times and so on.

THOUGHTS:
While solving this, I knew I had to keep track of the count of appearence. To do
this, I used a method of counting which is new to me: storing counts as a list instead
of individual counts.

"""
n = input()
arr = input()
arr = [int(x) for x in arr.split(' ')]
count = [0]*int(n)

for i in arr:
    count[i]+=1

print(count.index(max(count)))

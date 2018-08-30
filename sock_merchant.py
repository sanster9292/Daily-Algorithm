"""
PROBLM URL:
https://www.hackerrank.com/challenges/sock-merchant/problem

PROBLEM DESCRIPTION:
A sock merchant has many different colors of socks. Numbers represent
the color of those socks. For example, 1 represents color1 and 2 represents
color2...so on and so forth.
So, you take the input of colors and find out how many pairs there are and return
the number of pairs in that pile.

n= number of socks.
ar = the colors of each sock

Example:
n =9
ar = 10 20 20 10 10 30 50 10 20

This shold return 3 as the number of socks that are in this pile.

THOUGHTS:
In this challenge I tried to work with dictionaries instead of list which was
what I was using earlier. It was fun to flex those muscles.
"""


n = int(input())
ar= [int(x) for x in input().split(' ' )]

count_dict = {i:ar.count(i) for i in ar}
sock_count = 0

for k, v in count_dict.items():

    if count_dict[k] >1:
        pairs = count_dict[k]//2
        sock_count += pairs

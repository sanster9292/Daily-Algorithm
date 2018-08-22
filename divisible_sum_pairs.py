"""
PROBLEM URL
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

PROBLEM DESCRIPTION:
Given a number k and a list of intergers find the pair of values (i,j) in the
input array where
 1. i<j
 2. array[i]+array[j] is divisible by k

 Return how many such pairs exits in a given array.
 the first line of input takes 2 space seperated integers where n describes the
 number of values in input array and k is the value in question for comparison.

 THOUGHT PROCESS:

 I realized that it would be easier for me to just sort the input array . I had
 already implemented the bubble sort algorithm and knew the intuition behind it.
 So, I didn't reimplement it, I used the list.sort() method to sort the listself.
 Then, I iterated through the list with two indices, i and j and used the modulo
 operator to compare the sum of these values with the input value of k.

"""

n = input().split(' ')
n,k = [int(x) for x in n]

ints = input().split(' ')
ints = [int(x) for x in ints]
ints.sort()
#ints_sort = ints.sort()

def divisible_sums(n,k,ints):
    values = 0
    for i in range(len(ints)-1):
        for j in range(1+i,len(ints)):
            if ints[i]<ints[j]:
                sum_nums = ints[i] +ints[j]
                if (sum_nums % k==0):
                    values +=1
            else:
                continue

    return values

values = divisible_sums(n,k,ints)

print(values)

"""
PROBLEM URL:
https://www.hackerrank.com/challenges/bon-appetit/problem

PROBLEM EXPLANATION:
Tale as old as time. Two 'friends' go to a dinner and decide to split the bill.
One friend(Anna) is allergic to something and didn't quite eat all that was ordered. The other
friends(Brian) tries to over charge. Our job as warriors of truth and justice is to find out
if Anna is being overcharged.

INPUT FORMAT

The first line contains two space-separated integers  and , the number of items ordered and the
0 -based index of the item that Anna did not eat.
The second line contains n space-separated integers.
The third line contains an integer, b , the amount of money that Brian charged Anna for her share of the bill.

OUTPUT FORMAT:
If the amount charged is correct, print out Bon Appetit else print out the difference
that the overcharging friend(Brian) should pay Anna.

THOUGHTS:
This was the first time I was able to complete an algorithm on my own without looking at any code
in the discussion section.
Also, I was trying to think of the variables and the information provided in a visual way. I was recounting 
the information out loud to help with the thought process.

"""
vals = input().split(' ')
n,k = [int(x) for x in vals]

order = input().split(' ')
order = [int(x) for x in order]

b = int(input())

def bon_appetit(n,k,order,b):

    new_order = order.copy()
    del new_order[k]

    new_sum = int(sum(new_order)/2)

    if new_sum == b:
        print('Bon Appetit')
    else:
        return (b-new_sum)

print(bon_appetit(n,k,order,b))

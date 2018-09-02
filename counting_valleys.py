"""
PROBLEM URL:
https://www.hackerrank.com/challenges/counting-valleys/problem

PROBLEM DESCRIPTION:
If someone is walking up and down high points, we have to find out how manu valleys
they have been through. A valley means more than one consecutive Downwards steps,
followed by being level off by upwards steps
We have to use this to find how many valleys this person has been through.

INPUTS:
n = number of steps taken
s = string containing all the the steps taken.

EXAMPLE:
n = 8
UDDDUDUU

THOUGHTS:
For this I realized early on that I had to convert up/down into numerical data.
I did this by changing a counter everytime the person took a downwards step.
When they leveled off, I registered that as a valley. 
"""




# number of steps taken by a person

n = int(input())

# downs/ in those steps
s = list(input())

def count_valleys(n,s):

    valley, level = 0,0

    for step in s:

        if step =='D':
            level -=1
        else:
            if level ==-1:
                valley +=1
            level +=1

    return valley

print(count_valleys(n,s))

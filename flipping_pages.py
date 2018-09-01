 """
DATE: 09/01/2018.

 PROBLEM URL:
 https://www.hackerrank.com/challenges/drawing-book/problem

 PROBLEM DESCRIPTION:
 Flipping pages, you don't really think of how you are doing it, mathematically.
 Now, how would you teach a computer to navigate to a page in a book. Do you start
 from the intro, or do you start from the end?

INPUT:

n = total number of pages in a book
p = the page number that you want to flip to.

OUTPUT:
How many times you will have to flip to get to the page you want. You have to
find the minimum number of flips?

THOUGHTS:

Even though this wasn't a hard problem, I had to take a moment to really break
the logic for this problem. The main thing to consider if it will be faster to
navigate to the required page from the begining or the end. Then you break down
how to break down the method of getting there.


 """
# Total number of pages in the book
n = int(input())

# The page number that you want to be turned to
p = int(input())

def pageCount(n,p):

    if p/n<0.5:

        nums = len(range(int(n/2)))
        pairs = nums//2
    else:

        #nums = len(range(int(n/2+1),n+1))
        nums = len(range(p,2))
        pairs = nums//2

    return pairs

pages = pageCount(n,p)
print(pages)

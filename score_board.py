"""
PROBLEM URL:
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

DESCRIPTION:
Alice is playing a game where she is trying to get on a leaderboardself.
We have current leaderboard. We take the scores that Alice gets after however many
games she plays and we have to print out the rank she has after each tryself.

THOUGHTS:
This challenge was meant to push me and frustrate me, and boy it did. This challenge
had only 58.95% success rate on Hacker Rank and I wasn't sure if I could do it.
I had to think and try about 7 different ways before I cracked it. It took me a full day to crack it.
What I am proud of more than anything else is that when I was done, I had to loop over the
input list just once which makes the algorithm simple and elegant(not to toot my own horn).


"""

#n is the number of games that are recorded with high scores.
#board contains the high scores for each of those games in a descending order.

n = int(input())
board =[int(x) for  x in input().split(' ')]

# Alice's scores. m  is the number of games she has played and
# list named alice contains her scores in an ascending order.

m = int(input())
alice = [int(x) for x in input().split(' ')]


for ii in alice:
    scores = list(set(board))
    if ii not in scores:
        scores.append(ii)
        scores.sort(reverse=True)
        print(scores.index(ii)+1)
    else:
        scores.sort(reverse=True)
        print(scores.index(ii)+1)

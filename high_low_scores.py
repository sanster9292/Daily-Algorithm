
"""
PROBLEM URL:
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

PROBLEM DESCRIPTION
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array . scores = [12,24,10,24]
Scores are in the same order as the games played. She would tabulate her results as follows:

Function Description

Complete the breakingRecords function in the editor below. It must return an integer array containing the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.

breakingRecords has the following parameter(s):

scores: an array of integers

Sample Input
9
10 5 20 20 4 5 2 25 1

Sample Output
2 4
"""
games = int(input())
scores = input().split(' ')

high = int(scores[0])
low = int(scores[0])

high_count = 0
low_count =0

for i in range(len(scores)):
    if int(scores[i])>high:
        high = int(scores[i])
        high_count+=1
    elif int(scores[i])<low:
        low = int(scores[i])
        low_count+=1
    else:
        continue
print('high count', high_count)
print('low count ', low_count)

''' PROBLEM STATEMENT as taken from the following Hacker Rank link

https://www.hackerrank.com/challenges/birthday-cake-candles/problem

You are in-charge of the cake for your niece's birthday and have decided the cake will have one
candle for each year of her total age. When she blows out the candles, she’ll only be able to blow
out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning  years old, and the cake will have  candles of height 3,2,1,3,
she will be able to blow out candles successfully, since the tallest candle is of height  and there
are  such candles.

Input Format

The first line contains a single integer, , denoting the number of candles on the cake.
The second line contains  space-separated integers, where each integer  describes the height of candle .

Output Format

Print the number of candles that can be blown out on a new line.
'''

#MY ALGORITHM

n = input('Age of your neice: ')
candles = input('height of candles: ').strip().split()
# print(candles)

def birthdayCakeCandles(candles):
    for i in range(0,len(candles)-1):
        for j in range(0,len(candles)-1-i):
            if candles[j]>candles[j+1]:
                candles[j], candles[j+1]= candles[j+1], candles[j]

    return candles

sort_candles= birthdayCakeCandles(candles)
print(sort_candles.count(max(sort_candles)))

''' A BETTER APPROACH
 I saw some people on the discussion board using the function map to do this task. So after, I had
 written my own algorith to make sure that I understood it, I tried my had at map function. It is a lot of funself.
'''
n = input()
candles = list(map(int, input().strip().split()))

print(candles.count(max(candles)))

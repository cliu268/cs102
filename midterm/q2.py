# Digital games
# https://xjoi.net/contest/4582/problem/2

# 【describe】
# Tom sent a 01 string with a length of 8 to Marry to play the number game. Marry wanted to know how many 1s there were in the string.

# Note: the 01 string is a string with 0 or 1 characters. For example, "101" (without double quotation marks) is a 01 string with 
# a length of 3.

# 【format】
# The input file has only one line and a 01 string s with a length of 8.
# The output file has only one line and contains an integer, that is, the number of character 1 in the 01 string.

# sample input：
# 00010100

# sample output：
# 2
s=input()
answer=0
for i in s:
  if int(i)==1:
    answer+=1
print(answer)
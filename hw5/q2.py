# Chinese and Math
# https://xjoi.net/contest/4503/problem/2

# Description of the topic:
# There are n children who have taken two courses in Chinese and Mathematics.
# Now I hope to sort the grades to determine the ranking. The total score is ranked first, and if the total score is the same, 
# then it is ranked according to the Chinese score. Now please output the sorted scores.

# Input format:
# The first line, an integer n, indicating the number of children taking the test.
# The next n lines, two numbers per line, representing Chinese and math scores.

# Output format:
# A total of n lines, two numbers per line, indicating the Chinese and math scores after sorting.

# Sample input:
# 3
# 2 2
# 3 1
# 1 1

# Sample output:
# 3 1
# 2 2
# 1 1

# Constraints: All numbers do not exceed 1000.
n= int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
  for j in range(n-1-i):
    if sum(l[j])<sum(l[j+1]) or sum(l[j])==sum(l[j+1]) and l[j][0]<l[j+1][0]:
      l[j],l[j+1]=l[j+1],l[j]
for p in l:
  print(*p)
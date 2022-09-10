# Merge ordered arrays
# https://xjoi.net/contest/4936/problem/8

# Given two ordered arrays. Merge these two arrays into a new ordered array and output it.

# Input:
# Enter the two integers n,m in the first line.
# Enter n numbers in the second line to indicate the first ordered array.
# Enter the m numbers in the third line to indicate the second ordered array.

# Output:
# Output n + m numbers, indicating the result of the merge of the two arrays.

# Sample input:
# 3 4
# 4 5 8
# 1 3 6 7

# Sample output:
# 1 3 4 5 6 7 8

# Constraints:
# 1 <= n <= 5000000, 1 <= m <= 5000000, all numbers are in the range of signed 32-bit integers.
n,m = map( int, input().split())
a= list(map(int, input().split()))
b= list(map(int, input().split()))
c= a+b
c.sort()
print(*c)
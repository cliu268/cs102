# median
# https://xjoi.net/contest/4464/problem/5

# Description:
# Input N numbers, output the median of N numbers. N is an odd number.

# Input format:
# The first line is an integer n, indicating the number of numbers.
# The second line has n integers.

# Output format:
# One number per line, the median.

# Sample input:
# 3
# 2 3 1

# Sample output:
# 2

# Constraints: 
# N≤1000
n = int(input())
l = list(map(int, input().split()))
l.sort()
print(l[n//2])
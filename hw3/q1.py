# Sub string
# https://xjoi.net/contest/4442/problem/1

# Description of the topic:
# Givena string a, you want to output the substring between position l and r in a. Note that the characters in a are numbered 
# starting from 0.

# Input format:
# Enter a string a.
# Then enter two integers l and r.

# Output format:
# The output format is described in the title.

# Sample input 1:
# abc
# 2 2

# Sample output 1:
# c

# Note:
# a does not exceed 100 in length and contains only lowercase letters. l, r is less than the length of a, and l <= r.
a = list(input())
b,c = map( int, input().split())
print(*a[b:c+1],sep = '')
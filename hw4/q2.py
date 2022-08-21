# Carriage rearrangement
# https://xjoi.net/contest/4464/problem/2

# Description:
# There is a bridge next to an old train station whose bridge deck can be rotated horizontally around the pier in the center of 
# the river. Staff of the station found that the length of the bridge can accommodate up to two carriages. If the bridge is 
# rotated 180 degrees, the positions of two adjacent carriages can be exchanged. In this way, the order of the carriages can 
# be rearranged. So he was responsible for using the bridge to re-arrange the unsorted carriges from small to large numbers. 
# After he retired, the train station decided to automate this work. One of the important tasks was to make a program, to take 
# the numbers of the initial order of carriage, and calculate the minimum number of steps needed to sort the carriages.

# Input
# The input file has two rows of data, the first row is the total number of carriages N (not greater than 10,000), and the second 
# row is N different numbers indicating the initial carriage order.

# Output
# One data is the minimum times of rotations.

# Sample input:
# 4
# 4 3 2 1

# Sample output:
# 6

# data range:
# N is not greater than 10000
n = int(input())
y = list(map(int, input().split()))
count=0
for i in range(n):
  for x in range(n-i-1):
    if y[x] > y[x+1]:
      y[x], y[x+1] = y[x+1], y[x]
      count+=1
print(count)
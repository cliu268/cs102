# apple picking
# https://xjoi.net/contest/4582/problem/1

# There is an apple tree in Taotao's yard, and there are 10 mature apples every autumn, and at that time ,Tao Tao will run to 
# pick apples. Tao Tao has a 30-cm-high bench. When she can't pick the apple directly with her hand, she will step on the bench 
# and try again.

# it's known the height of 10 apples to the ground, and the maximum height that can be reached when Taotao stretch his arms. 
# Please help Tao Tao count the number of apples she can pick. Suppose once she hits an apple, the apple will fall.

# Input:
# Two lines of data. The first line contains 10 integers (in centimeters) between 100 and 200 (including 100 and 200) representing 
# the height of 10 apples to the ground, separated by a space between two adjacent integers. 
# The second line consists of only an integer (in centimeters) between 100 and 120 (inclusive of 100 and 120), which represents the 
# maximum height that Taotao can reach when stretching his arm.

# Output :
# Including one line, this line contains only one integer, indicating the number of apples that Tao Tao can pick.

# Sample input:
# 100 200 150 140 129 134 167 198 200 111
# 110

# Sample output:
# 5
l=list(map(int, input().split()))
a=int(input())
answer=0
for i in l:
  if int(i)<=(a+30):
    answer+=1
print(answer)
# p-coding
# https://xjoi.net/contest/4442/problem/7

# 【Description】
# Given an string str which is consist of entirely numeric characters(' 0 ', '1', '2'...  , '9'),
# please figure out its p-type string.
# For example, the string 122344111 has 1 numeric character "1", 2 numeric characters "2", 1 numeric characters "3", 
# 2 numeric characters "4", 3 numeric characters "1". 
# So we say that the p-type  string of 122344111 is 1122132431;  
# Similarly, the p-type  string of 1111111111  is 101.the p-type  string of 00000000000  is 110.
# 100200300 can be described as "one 1, two 0's, one 2's, two 0's, one 3's, two 0's", so its p-type  string is 112012201320.  

# [Data format]  
# Enter a single line containing the string str.  Each string can contain a maximum of 1000 numeric characters.  
# Prints the p-encoded string corresponding to the string.  

# 【Sample input】
# 122344111

# 【Sample output】
# 1122132431
a = list(input())
b = []
count = 1
for i in range(len(a)-1):
  if a[i] != a[i+1]:
    b.extend([count, a[i]])
    count = 1
  elif a[i] == a[i+1]:
    count += 1
b.extend([count, a[-1]])
print(*b, sep = '')
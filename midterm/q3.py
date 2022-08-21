# Caesar encryption
# https://xjoi.net/contest/4582/problem/3

# Description:
# In ancient Rome, "Gaul War" described Caesar's use of encryption to convey information, the so-called "Caesar Encryption", 
# which is an alternative encryption. Each letter in the message was replaced by the t-th letter after it. For example, when t=4, 
# the rule of encryption is to replace the original letter with the 4th letter after the original letter. i.e, the 4th letter after 
# the letter "A" is "E", and the "A" is substituted by "E", and the 4th letter after the letter "z" is "d", and "z" is substituted 
# by "d". Therefore, "China" will be translated to "Glmre". Please write a program to encrypt characters of any input string by 
# replacing each letter with the t-th letter after it.

# Input:
# One string and a integer t.

# Output:
# One string..

# Sample input 1:
# china 4

# Sample output 1:
# glmre

# Sample input 2:
# antDZYO 30

# Sample output 2:
# erxHDCS

# Constraints:
# the string contains letters only and its length does not exceed 100 and the t<=260
n,t = input().split()
x= len(n)
l= list(n)
ans = ''
for i in range (x):
  if l[i].isupper():
    l[i]= chr((ord(l[i])-ord('A')+int( t)) %26 + ord('A'))
  else:
    l[i]= chr((ord(l[i])-ord('a')+int( t)) %26 + ord('a'))
  ans += l[i]
print(ans)
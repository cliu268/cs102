# Code Your Function 3
# https://xjoi.net/contest/4773/problem/4?locale=en

# Title Description
# Please write a function to pass a real number of A and an integer of 1 or 2 to represent a temperature and a parameter, 
# respectively. You need to transmit a real number of a double type of B, which represents another temperature. 
# When the parameter type value is 1 , the unit of A is Celsius, and it needs to be converted to the Fahrenheit temperature 
# of B and returned; When the parameter type value is 2 , the unit of A is Fahrenheit, and it needs to be converted to a 
# temperature of B Celsius and returned.
# Assuming a temperature of A Celsius, the formula for converting it to a temperature of B Fahrenheit is:
# B = \ Frac{9}{5} A +32

# Input Format
# The first line is an integer of q, which means that there is a q group query.
# Next to the q line, each line contains a real number of A and an integer of type , indicating a query.

# Output Format
# A total of q row, including a real number, represents the answer to a group of queries.

# Note: The answer is rounded to 3 decimal places

# Sample Input
# 2
# 0.0 1
# 20 2

# Sample Output
# 32.000
# -6.667
def temp(n,t):
  if t==1:
    return('%.3f' % ((9/5)*n + 32))
  else:
    return('%.3f' % (((5*n)-160)/9))

q=int(input())
l=[]
for i in range(q):
  x,y= input().split()
  y= int(y)
  x = float(x)
  print(temp(x,y))
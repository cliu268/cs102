# reference
# https://xjoi.net/contest/4845/problem/1?locale=en

# Description :
# A reference is an alias for a variable.
# Such as int &a = b;
# Then a is a reference to b, a is an alias for b, and changing the value of a is equivalent to changing the value of b.

# Note that the reference must be assigned an initial value, a separate int &a; is not acceptable. 
# That is to say, the reference can't be empty like a pointer, and the reference is always dependent on the referenced object.

# A common scenario for referencing is passing parameters to functions.

# By directly changing the value of $a, b$ inside the function, you can change the value of $a, b$ in the main function.

# There are also commonly used operations to update larger or smaller values.

# You can update x with y by calling checkmin(x, y) directly inside the main function.

# Implement two functions, checkmin(), checkmax(), which use the reference implementation to find the maximum and minimum values 
# in an array.

# Input:
# Enter an integer $n$ in the first line of
# Enter $n$ integer in the second line

# Output :
# Output two integers for max and min of the inputs

# Sample input:
# 5
# 1 2 3 4 5

# Sample output:
# 5 1
def checkmin(x, y):
  return(min(y))
 
def checkmax(x, y):
  return(max(y))
 
n= int(input())
l= list(map(int, input().split()))
print(checkmax(n, l), checkmin(n, l))
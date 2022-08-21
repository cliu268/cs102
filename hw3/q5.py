# ISBN code
# https://xjoi.net/contest/4442/problem/6

# Each officially published book has an ISBN number corresponding to it. The ISBN code includes a 9-digit number, a 1-digit 
# identifier, and a 3-digit separator. The specified format is “x-xxx-xxxxx-x”, where the symbol “-" is the separator 
# (minus sign on the keyboard), the last digit is the identification code, for example 0-670-82162-4 is a standard ISBN code. 
# The first digit of the ISBN code indicates the publishing language of the book, for example, 0 stands for English; the three 
# digits after the first separator "-" represent the publisher, for example, 670 stands for Viking Press; the fifth digit after 
# the second separator Represents the number of the book in the publisher; the last digit is the identification code.

# The identification code is calculated as follows:
# The first digit is multiplied by 1 plus the minor digit multiplied by 2... and so on. Using the result mod 11, the resulting 
# remainder is the identification code. If the remainder is 10, the identification code is the uppercase letter X. For example, 
# the identification code 4 in the ISBN number 0-670-82162-4 is obtained as follows: 9 digits of 067082162, from left to right, 
# multiplied by 1, 2, ..., 9, respectively, and then summed, that is, 0×1 + 6×2 +...+ 2×9 = 158, and then the result 
# 4 of 158 mod 11 is taken as the identification code.
# Your task is to write a program to determine whether the identifier in the input ISBN number is correct. 
# If it is correct, only "Right" is output; if it is wrong, output the ISBN number that you think is correct.

# Input :
# The input has only one line and is a sequence of characters representing the ISBN number of a book (guaranteed that the input 
# conforms to the format requirements of the ISBN number).

# Output :
# The output has one line. If the ID of the input ISBN number is correct, then "Right" is output. Otherwise, the correct ISBN number 
# (including the separator "-") is output according to the specified format.

# Sample input 1:
# 0-670-82162-4

# Sample output 1:
# Right

# Sample input 2:
# 0-670-82162-0

# Sample output 2:
# 0-670-82162-4
isbn= input().replace('-','')
sum=0
 
for i in range(9):
  sum+=int(isbn[i])*(i+1)
 
r= sum%11
if int( r)==10:
  if isbn[9]=='X':
    print("Right")
  else:
    print(isbn[0] + '-' + isbn[1:4] + '-' + isbn[4:9] + '-' + 'X')
else:
  if isbn[9]==str( r):
    print("Right")
  else:
    print(isbn[0] + '-' + isbn[1:4] + '-' + isbn[4:9] + '-' + str( r))

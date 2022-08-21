# Encrypted medical records
# https://xjoi.net/contest/4442/problem/5

# 【 Description 】  
# Xiao Ying, a junior student majored  in pharmacy, got an opportunity to practice in a hospital during her summer vacation.  
# During the period, Xiaoying's solid professional foundation won unanimous praise from the doctors. So the director gave her an 
# additional task to decrypt the encrypted list of the wounded soldiers who attended the Anti-Japanese War.  
# After research, Xiao Ying discovered the following encryption rules (an example of "original text -> ciphertext" is in parentheses)  
# 1. All characters in the original text are looping three places to the left in the alphabet （dec  -> abz）
# 2. Reverse storage （abcd -> dcba ）
# 3. Case reversal （abXY -> ABxy）

# 【Data format】  
# Enter an encrypted string.  (Contains less than 50 uppercase and lowercase letters only)  
# Output the decrypted string.  

# 【Sample input】
# GSOOWFASOq

# 【Sample output】
# Trvdizrrvj
def Move(a):
  if 119<ord(a)<123 or 87<ord(a)<91:
    a=chr(ord(a)-23)
  else:
    a=chr((ord(a)+3))
  return a
 
def Reverse(a):
  if a.isupper():
    a= a.lower()
  elif a.islower():
    a= a.upper()
  return a
 
n=list(input())
for i in range(len(n)):
  n[i] = Move(n[i])
  n[i] = Reverse(n[i])
print(*list(reversed(n)), sep='')
# Who got the scholarship
# https://xjoi.net/contest/4503/problem/3

# After the mid-term exams are finished, the students must be ranked. The school has a special provision: First m (m<=60) students 
# are awarded scholarships. In the face of those mountains of papers, Director Wang was at a loss, so he came to ask for your 
# help since you understand NOIP. I hope you can help him.

# Note: 
# 1. The rank rule is as follows: 
# students are ranked by average test score, if the average score is the same, then the variance is calculated and the students 
# with smaller variance are ranked first. If the variance is also the same, they are arranged according to the order of the test 
# number (smaller test number first). 
# 2. The average and variance of the fractional part are ignored (that is, round down to the nearest whole number) 
# 3. The variance formula is: variance s=(x[1]*x[1]+x[2]*x[2]+...+x[n]*x[n]-n*b*b)/n ( Where s is the variance, 
# x[1..n] is a set of numbers, and b is the average number of this set)

# Input：
# The first three numbers n (n <= 1000), m (m <= 60), k (k <= 10), where n represents the number of students, m represents 
# the number of students who can obtain a scholarship, k represents the number of subjects tested in the mid-term exam.

# The next n rows, each row k numbers, the i-th row, the j-th column shows the score x on jth subject of student with test number 
# i (x<=100)

# Output：
# There are only m numbers: test numbers for students who can receive scholarships (arranged in descending order of rank), 
# with a space between each two numbers.

# Sample Input：
# 5 3 3 
# 99 92 71
# 98 98 98
# 80 93 72
# 98 98 98
# 97 98 99 

# Sample Output：
# 2 4 5
n,m,k=map( int, input().split())
 
scores=[]
avgs=[0]*n
vars=[0]*n
ids=[0]*n
 
for i in range(n):
  scores.append(list(map(int, input().split())))
 
for i in range(n):
  ids[i]=i
 
for i in range(n):
  student_score= scores[i]
  avgs[i]= sum(student_score) // k
 
for i in range(n):
  student_score= scores[i]
  var=0
  for j in range(k):
    var+=student_score[j]**2
  var-=avgs[i] ** 2 * k
  vars[i] = var // k
 
for i in range(m):
      max_pos = i
      max_id = ids[i] 
      for j in range(i + 1, n):
          j_id = ids[j]
          if (avgs[j_id] > avgs[max_id]) or (avgs[j_id] == avgs[max_id] and vars[j_id] < vars[max_id]) or (avgs[j_id] == avgs[max_id] and vars[j_id] == vars[max_id] and j_id < max_id):
              max_pos = j
              max_id = j_id
             
      ids[i], ids[max_pos] = ids[max_pos], ids[i]
 
for i in range(m):
      print(ids[i] + 1, end="")
      print(" ", end="")
'''
N-QUEEN
'''

import sys
input = sys.stdin.readline

n = int(input())

answer = 0
row = [0] * n

def possible(x):
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == (x - i): #열체크 or 대각선 체크
      return False
  return True

def n_queens(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if possible(x):
                n_queens(x+1)
n_queens(0)
print(answer)
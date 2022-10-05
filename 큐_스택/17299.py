'''
오등큰수
'''

#Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, 
# Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수
# 그러한 수가 없는 경우에 오등큰수는 -1

import sys
from collections import Counter

n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))

'''
unique = set(a_list)
F = []
for _ in range(1,len(unique)+1):
    F.append(a_list.count(_))
unique = list(unique)
'''

count = Counter(a_list)

output = [-1] * n
stack = [0] #스택활용문제
# stack.pop()
# stack

for i in range(1, n):
    while stack and count[a_list[stack[-1]]] < count[a_list[i]]: #처음돌 때 a_list[0] vs a_list[1]
            output[stack.pop()] = a_list[i]
    stack.append(i)
    
print(*output)

## 유사 문제 : 17298 오큰수 , 2493 탑


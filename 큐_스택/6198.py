'''
옥상 정원 꾸미기
'''

import sys
n = int(sys.stdin.readline())

building_h = []
for _ in range(1, n+1):
    height = int(sys.stdin.readline())
    building_h.append(height)

cnt = 0
stack = [] #스택활용문제

for b in building_h:
  while stack and stack[-1]<=b:
    stack.pop()
  stack.append(b)
  cnt += len(stack)-1

print(cnt)


'''
[10] 옥상을 볼 수 있는 건물 X : len(stack)-1 = 0
[10, 3] 높이 10에서 높이 3 옥상 보기 가능 : len(stack)-1 = 1
[10, 7] 높이 10에서 높이 7의 옥상 보기 가능 : len(stack)-1 = 1
[10, 7, 4] 높이 10에서 높이 4의 옥상 보기 가능 (7의 옥상은 봤음), 높이 7에서 높이 4의 옥상보기 가능 : len(stack)-1 = 2
[12] 옥상을 볼 수 있는 건물 X : len(stack)-1 = 0
[12, 2] 높이 12에서 높이 2의 옥상 보기 가능 : len(stack)-1 = 1
=> 1+1+2+1 = 5
'''

### 유사문제 : 2493 탑


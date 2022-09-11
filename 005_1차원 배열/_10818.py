import sys 
a = [int(s) for s in sys.stdin.read().split()[1:]] 
print(min(a), max(a))
a = sorted(int(s) for s in sys.stdin.read().split()[1:]) #정렬 먼저
print(a[0], a[-1]) #맨 앞, 맨 뒤 == 최소, 최대


import sys, heapq as hq 
#우선순위 큐 알고리즘이라고도 하는 힙(heap) 큐 알고리즘은 이진 트리로 정렬하여 최소값을 빠르게 가져옴
### 큐 알고리즘 추가 학습
a = [int(s) for s in sys.stdin.read().split()[1:]] 
hq.heapify(a) 
print(*hq.nsmallest(1, a), *hq.nlargest(1, a))
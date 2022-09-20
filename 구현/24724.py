'''
현대모비스와 함께하는 부품 관리
'''

import sys

T = int(sys.stdin.readline())

for x in range(1, T+1) :
    N = int(sys.stdin.readline()) #부품의 개수
    for _ in range(N+1) :
        A, B = list(map(int, sys.stdin.readline().split()))    
    print("Material Management", x)
    print("Classification ---- End!")

'''
테트리스
'''
import sys
c,p = map(int, sys.stdin.readline().split()) #C와 떨어뜨리는 블록의 번호 P
height = list(map(int, sys.stdin.readline().split())) #각 칸의 높이(길이:c)

cnt=0
if p==1:
    cnt=cnt+c  #세우거나
    for i in range(c-3): #눕히거나 (4개 연속으로 height가 같아야하니까)
        if height[i] == height[i + 1] and height[i + 1] == height[i + 2] and height[i + 2] == height[i + 3]:
            cnt+=1

if p==2:
    #정사각형 -> 하나의 경우만 있음
    for i in range(c-1):
        if height[i] == height[i + 1]:
            cnt+=1


if p==3:
    for i in range(c-2): #눕힐때
        if height[i] == height[i + 1] and height[i + 1] == height[i + 2] - 1:
            cnt+=1
    for i in range(c-1): #세울때
        if height[i] == height[i + 1] + 1:
            cnt+=1

if p==4:
    for i in range(c-2):
        if height[i] == height[i + 1] + 1 and height[i + 1] == height[i + 2]:
            cnt+=1
    for i in range(c-1):
        if height[i] == height[i + 1] - 1:
            cnt+=1


if p==5:
    for i in range(c-2):
        #ㅗ
        if height[i] == height[i + 1] and height[i + 1] == height[i + 2]:
            cnt+=1
        #ㅜ
        if height[i] == height[i + 1] + 1 and height[i + 1] == height[i + 2] - 1:
            cnt+=1
    for i in range(c-1):
        #ㅏ
        if height[i] == height[i + 1] - 1:
            cnt+=1
        #ㅓ
        if height[i] == height[i + 1] + 1:
            cnt+=1


if p==6:
    for i in range(c-2):
        #_ _ㅣ
        if height[i]==height[i+1] and height[i+1]==height[i+2]:
            cnt+=1
        #ㅣ_ _
        if height[i]==height[i+1]-1 and height[i+1]==height[i+2]:
            cnt+=1
    for i in range(c-1):
        #ㄴ
        if height[i]==height[i+1]:
            cnt+=1
        #ㄱ
        if height[i]==height[i+1]+2:
            cnt+=1

if p==7:
    for i in range(c-2):
        if height[i]==height[i+1] and height[i+1]==height[i+2]:
            cnt+=1
        if height[i]==height[i+1] and height[i+1]==height[i+2] + 1:
            cnt+=1
    for i in range(c-1):
        if height[i]==height[i+1]-2:
            cnt+=1
        if height[i]==height[i+1]:
            cnt+=1

print(cnt)
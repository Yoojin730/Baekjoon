'''
미친로봇
'''

import sys
input = sys.stdin.readline

n, E, W, S, N = map(int, input().split())
graph = []
for i in range(2*n+1):
    graph.append([0] * (2*n+1)) #n이 2이면 5 , n이 3이면 7
    
probability = [E, W, S, N]
answer = 0
direction = [[1, 0], [-1, 0], [0, -1], [0, 1]] # 동 서 남 북 

def dfs(dx, dy, prob,cnt):
    global answer
    if cnt == n:
        answer += prob
        return

    now_prob = prob
    graph[dx][dy] = 1 #방문처리

    for i in range(4): #동서남북
        nx = dx + direction[i][0]
        ny = dy + direction[i][1]

        if graph[nx][ny] == 1:
            continue
        else :
            dfs(nx, ny, now_prob*(probability[i]/100),cnt+1)
            graph[nx][ny] = 0

dfs(n,n,1,0)
print(answer)                
                
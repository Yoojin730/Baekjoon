'''
트럭
'''

#n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중
n, w, l = map(int, input().split())

# 입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10)가 주어지는데,
# ai는 i번째 트럭의 무게를 나타낸다.
truck = list(map(int, input().split()))

bridge = [0] * w #다리의 길이
time_sum = 0

while bridge:
    time_sum += 1
    bridge.pop(0) #다리의 길이 하나씩 줄이기

    ## 트럭 확인
    if truck:
        #다리가 트럭 무게 버틸 수 있을 때 
        if sum(bridge) + truck[0] <= l:
            bridge.append(truck.pop(0))
        #무게 버틸 수 없을 때
        else:
            bridge.append(0) 

#최종 출력
print(time_sum)
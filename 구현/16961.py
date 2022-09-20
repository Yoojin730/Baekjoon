'''
탭 VS 공백
'''

N = int(input())
#tab, space를 따로 1~366일을 생성하고자 했으나 year 변수로 한 번에 처리하는게 나을듯 ... 
year = [[0,0] for i in range(366)] #0~365 : 366일
answer_5 = 0 #가장 오랜 기간 투숙한 사람이 투숙한 날의 수

for i in range(N):
    c, s, e = map(str, input().split())
    s = int(s)
    e = int(e)

    if c == 'T':
        for _ in range(s-1, e):
            year[_][0] += 1 #[0,0] 기준으로 앞은 T, 뒤는 S

    else:
        for _ in range(s-1, e):
            year[_][1] += 1

    if (e-s+1) > answer_5:
        answer_5 = (e-s+1)


answer_1 = 0 #투숙객이 1명 이상인 날의 수
answer_2 = year[0][0] + year[0][1] #가장 많은 투숙객이 있었던 날에 투숙한 사람의 수
answer_3 = 0 #싸움이 없는 날의 수
answer_4 = 0 #싸움이 없는 날 중 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수. 싸움이 없는 날이 없으면 0을 출력

for i in range(366):
    if year[i][0]+year[i][1] > 0:
        answer_1 += 1 #투숙객이 1명 이상인 날의 수

    if year[i][0] + year[i][1] > answer_2:
        answer_2 = year[i][0] + year[i][1]

    if year[i][0] == year[i][1] and year[i][0] > 0:
        answer_3 += 1
        if year[i][0] + year[i][1] > answer_4:
            answer_4 = year[i][0] + year[i][1]


print(answer_1) 
print(answer_2)
print(answer_3)
print(answer_4)
print(answer_5)
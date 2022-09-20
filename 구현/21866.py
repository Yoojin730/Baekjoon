'''
추첨을 통해 커피를 받자
'''

score = list(map(int, input().split()))
max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

hacker = False
for i in range(9):
    if score[i] > max_score[i]:
        hacker = True
if hacker == True:
    print("hacker")
else:
    print("draw" if sum(score) >= 100 else "none")
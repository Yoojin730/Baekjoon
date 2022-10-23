'''
AC
'''

#함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수
#두 번 뒤집으면 그대로니까 -> 홀수번 뒤집을 때만 뒤집기 : 시간 단축 방법

from collections import deque

T = int(input()) #테스트 케이스의 개수4

for _ in range(T):
    p = input() #RDD
    n = int(input())
    array = deque(input()[1:-1].split(','))

    holzzak = 0
    if n == 0:
        array = []

    for i in p:
        if i == 'R':
            holzzak += 1
        elif i == 'D':
            if len(array) == 0:
                print("error")
                break
            else:
                if holzzak % 2 == 0:
                    array.popleft() #그대로라면 앞에서 하나 빼기
                else:
                    array.pop() #뒤집을거니까 뒤에서 하나 빼기
 
    else:
        if holzzak % 2 == 0: #홀짝이 짝수라면 그대로 출력하면 끝
            print("[" + ",".join(array) + "]")
        else: #홀수일 때
            array.reverse()
            print("[" + ",".join(array) + "]")

        
'''
시간 초과

    for i in p:
        if i == 'R':
         array.reverse()
        elif i == "D":
            if len(array) == 0:
                break
        else:
            array.popleft()
    
    if len(array) == 0:
        print('error')
    else:
        print(list(array))
'''


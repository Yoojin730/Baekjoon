'''
문자열 폭발
'''

str_input = input()
bomb = list(input())

stack=[]

for i in str_input:
    stack.append(i) #한 글자씩 스택에 넣어주기
    if stack[-(len(bomb)):] == bomb :
        for _ in range(len(bomb)) :
            stack.pop()

if stack : #문자열이 남아있다면
    print(''.join(stack))
else:
    print("FRULA")


'''
cnt = 0  
while True :
    cnt = cnt + 1
    if str_input.find(bomb) != -1 :
        str_input = ''.join(str_input.split(bomb))
    else : 
        break

if str_input == '' :
            print('FRULA')
else : 
    print(str_input)
'''


'Hello'[:-2]


'''
부등호
'''

import sys
input = sys.stdin.readline

k = int(input())
s = input().split()
chk = [False] * 10
max = ''
min = ''
    
def check(a, b, c) :
    if b == '<' :
        return a < c
    else :
        return a > c

def make_output(numbers, num) :
    global max, min

    if num > k:
        if len(min) == 0:
            min = numbers
        else:
            max = numbers
        return

    for i in range(10) :
        if chk[i] == False :
            if num == 0 or check(numbers[-1], s[num-1] , str(i)) :
                chk[i] = True
                make_output(numbers+str(i), num+1)
                chk[i] = False

make_output('', 0)
print(max)
print(min)

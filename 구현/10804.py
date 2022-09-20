'''
카드역배치
'''

import sys

card = [i for i in range(0, 21)]
for _ in range(10):
    a , b = map(int, sys.stdin.readline().split())
    card_neworder = card[:a] + card[a:b+1][::-1] + card[b+1:]
    card = card_neworder

print(' '.join(map(str, card[1:])))
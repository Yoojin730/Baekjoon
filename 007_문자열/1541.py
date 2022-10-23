'''
잃어버린 괄호
'''

#괄호를 적절히 쳐서 이 식의 값을 최소로

abc = input()
minus_list = abc.split('-') 
sum_ = 0

for i in minus_list[0].split('+'):
    sum_ += int(i)

for i in minus_list[1:]:
    for j in i.split('+'):
        sum_ -= int(j)
        
print(sum_)




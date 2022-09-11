abc = input()
minus_list = abc.split('-') # 55-50+40-30+20
sum_ = 0
for i in minus_list[0].split('+'):
    sum_ += int(i)
for i in minus_list[1:]:
    for j in i.split('+'):
        sum_ -= int(j)
        
print(sum_)
word = input().upper()
word_list = list(set(word))

list_ = []

for x in word_list :
    cnt = word.count(x)
    list_.append(cnt)
    
if list_.count(max(list_)) >= 2 :
    print("?")
    
else : 
    print(word_list[(list_.index(max(list_)))])
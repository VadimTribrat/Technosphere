str1 = input().lower().split()
str2 = input().lower().split()
dict_1 = dict()
dict_2 = dict()
flag = True
for word in str1:
    dict_1[word] = dict_1.get(word, 0)+1
for word in str2:
    dict_2[word] = dict_2.get(word, 0)+1
for word in set(dict_2.keys()):
    if word not in dict_1 or dict_1[word] < dict_2[word]:
        flag = False
        print('NO')
        break
if flag:
    print('YES')

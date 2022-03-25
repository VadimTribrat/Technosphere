n = int(input())
lst = list(map(int, input().split()))
set_ = set(lst)
length = len(set_)
counter = 0
for val in lst:
    if val in set_:
        print(val, end=' ')
        set_.remove(val)
        counter += 1
print()
print(len(lst) - length)

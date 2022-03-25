n = int(input())
lst = []
mapper = dict()
for ind in range(n):
    temp = input()
    lst.append(temp)
    val = tuple(sorted(list(temp)))
    if val not in mapper:
        mapper[val] = [temp]
    else:
        mapper[val].append(temp)
for val in mapper.values():
    print(*val)

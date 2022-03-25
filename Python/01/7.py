import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


low = 1
high = 100_000
lst = [i for i in range(low, high, int(high/10))] + [high+1]
flag = True
while high - low > 2:
    flag = False
    middles = [int((lst[i] + lst[i+1])/2) for i in range(len(lst)-1)]
    results = []
    for val in middles:
        print("? {}".format(val))
    print("+")
    for ind, val in enumerate(middles):
        results.append(int(input()))
    if results[0] == 1 and results[-1] == 1:
        low = middles[0] - (middles[1] - middles[0]) if middles[0] - (middles[1] - middles[0]) >= 1 else 1
        high = middles[0]
    if results[0] == 0 and results[-1] == 0:
        low = middles[-1]
        delta = middles[-1] - middles[-2]
        high = middles[-1] + delta if middles[-1] + delta <= 100_000 else 100_000
        flag = True
    for i in range(len(results) - 1):
        if results[i] != results[i+1]:
            low = middles[i]
            high = middles[i+1]
            break
    lst = [i for i in range(low, high, int((high - low)/10 if int((high - low)/10) != 0 else 1))] + [high]
if flag:
    print("! {}".format(high))
else:
    print('! {}'.format(low))

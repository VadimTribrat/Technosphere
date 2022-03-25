def sum_of_digits(d):
    sum_ = 0
    for val in str(d):
        sum_ += int(val)
    return sum_


n = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst.sort(key=sum_of_digits)
print(*lst)

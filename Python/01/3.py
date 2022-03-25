n = input()
if '.' in n:
    n = n.split('.')
dig1, dig2 = 0, 0
if isinstance(n, list):
    dig1 = int(n[0])
    dig2 = int(n[1])
else:
    dig1 = int(n)
rubs = [10, 5, 2, 1]
fra = [50, 10, 5, 1]
dict1, dict2 = dict(), dict()
for val in rubs:
    dict1[val] = dig1//val
    dig1 -= dig1//val*val
for val in fra:
    dict2[val] = dig2//val
    dig2 -= dig2//val*val
for val in rubs:
    if dict1[val] != 0:
        print("{:5.2f}\t{}".format(val, dict1[val]))
for val in fra:
    if dict2[val] != 0:
        print("{:5.2f}\t{}".format(val/100, dict2[val]))

arr = [2222, 1221, 10, 353, 898, 23]
h_p = 00
for i in arr:
    temp = i
    rev = ''
    while temp > 0:
        rem = temp % 10
        rev += str(rem)
        temp = temp // 10

    if i == int(rev) and int(rev) > h_p:
        h_p = int(rev)
    else:
        h_p = h_p
print(h_p)

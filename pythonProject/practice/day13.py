# num = [5, 2, 5, 2, 2]
# for i in num:
#     print("x" * i)

n = [1100000, 355554, 55, 1, 12, 9, 70]
maxi = n[1]
for i in n:
    for j in n:
        if i < j:
            maxi = j
        else:
            maxi = i

print(maxi)
# b = n.sort()
# print(b)
# print(max(n))


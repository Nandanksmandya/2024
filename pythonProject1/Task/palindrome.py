print("Hellooo ")

list1 = [1, 0, 2, 0, 3, 0, 4, 5]
a = sorted(list1)
print(a)
list2 = []
for i in a:
    if i != 0:
        list2.append(i)
print(list2)
for j in a:
    if j == 0:
        list2.append(j)

print(list2)

b = (reversed(list1))
for k in b:
    print(k)

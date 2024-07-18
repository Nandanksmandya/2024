# givenNum = int(input("Enter the Number : "))
# lastDigit = givenNum % 10
# if 0 < lastDigit < 5:
#     output = givenNum - lastDigit
#     print(output)
# elif lastDigit > 5:
#     output = givenNum + (10 - lastDigit)
#     print(output)
# elif lastDigit == 5:
#     output = givenNum + 5
#     print(output)

# name = ['aa', 'bb', 'aa', 'cc']
# dic = {}
#
# for element in name:
#     if element in dic:
#         dic[element] += 1
#     else:
#         dic[element] = 1
#
# print(dic)

names = 'python developer'
a = names.replace(" ","")
print(a)
dic = {}

for element in a:
    if element in dic:
        dic[element] += 1
    else:
        dic[element] = 1

print(dic)
print(a[::-1])
p = (reversed(a))


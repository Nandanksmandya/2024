# list1 = ['Ebullient.com', 'Ethereal.in', 'Ineffable.pdf', 'Ephemeral.co']
# exten = []
# for i in list1:
#     e = '.'
#     a = i.split(".", maxsplit=1)
#     exten.append(a[-1])
# print(exten)

# s = "javadeveloper"
# replaced = ""


# o = ['a', "e", "i", 'o', 'u']
# ow = [][::-1]
# for i in s:
#     for j in o:
#         if j == i:
#             # print(i)
#             ow.append(i)
#             # break
# print(ow[::-1])
#
# for n in s:
#     for k in ow[::-1]:
#         if n not in o:
#             replaced += n
#             break
#         elif n in o:
#             replaced += k
#             ow.remove(k)
#             break
# print(replaced)

s = "javadeveloper"
vowels = ['a', 'e', 'i', 'o', 'u']

# Step 1: Extract vowels in reverse order
ow = [char for char in s if char in vowels][::-1]

# Step 2: Replace vowels
replaced = ""
for char in s:
    if char in vowels:
        replaced += ow.pop(0)  # Replace with the first element from reversed vowels
    else:
        replaced += char  # Keep non-vowel characters as they are

print(replaced)


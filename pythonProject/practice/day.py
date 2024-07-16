# weight = int(input("Enter the weight: "))
# a_weight = weight * 0.45
# # print("the Actual weight is :" + {a_weight})
# # print(f"nandan weight is{a_weight}")
# print("nandan" + str(a_weight))
"""remove all duplicate from the given string"""
name = input("enter the name: ")
rep_word = ""
not_reword = ""
count = 0
for char in name:
    if char not in not_reword:
        not_reword += char
    else:
        # rep_word += char
        pass

print(f"The given Name : {name}")
print(f"The repeated words in the given name : {rep_word}")
print(f"The Non-repeated words in the given name : {not_reword}")
# first = "nandan"
# last = "K S"
# print(f"{first} [{last}] is a coder")
# suv = first + "[" + last + "]" + "is a coder"
# print(suv)

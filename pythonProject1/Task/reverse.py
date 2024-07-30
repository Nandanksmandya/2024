# """Reverse a string"""
# given = "ABCDE"
# reve = ""
# for i in given:
#     reve = i + reve
# print(reve)
#
# """ Swap 2 numbers without using third variable """
# num1 = 5
# num2 = 3
#
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
#
# print(f"Num1: {num1}")
# print(f"Num2: {num2}")
#
# """vowel in the string"""
# name: "malayalam"
# if "a" or "i" or "e" or "o" or "u" in name:
#     print("Vowels present")
# else:
#     print("Not Present")
#
# """Prime num"""
#
# p = 7
# for i in range(2, p):
#     if p % i == 0:
#         print("Not a prime Number")
#         break
# else:
#     print("It is a prime number")
#
# """palindrome string"""
# p_name = "nandnan"
# rever = ""
# for i in p_name:
#     rever = i + rever
# if p_name == rever:
#     print("Given string is palindrome")
# else:
#     print("Given string is not a Palindrome")
#
# """Factorial of a num"""
# given_num = 10
# fact = 1
# for i in range(1, given_num + 1):
#     fact = fact * i
# print(fact)
#
# """Remove all the duplicates in the string"""
# given_str = "Reverse variable"
#
#
# def remove_duplicates(input_string):
#     seen = set()
#     result = []
#     for char in input_string:
#         if char not in seen:
#             seen.add(char)
#             result.append(char)
#     # print("".join(result))
#     return ''.join(result)
#
#
# print(remove_duplicates(given_str.lower()))
#
# """Reverse A number and count of digits"""
# g_n = 1234567
# rev = ""
# count = 0
# while 0 < g_n:
#     rem = g_n % 10
#     rev = rev + str(rem)
#     count += 1
#     g_n = g_n // 10
# print("The Reverse Number of given number : ", int(rev))
# print("The Count of digits of given number : ", count)

"""Armstrong Number"""

given_n = 153
o_given_num = given_n
temp = given_n
sum_of_digits = 0
while 0 < temp:
    rem = temp % 10
    sum_of_digits += 1
    temp = temp // 10
print(sum_of_digits)
sum_of_cube_of_eachDigits = 0

while 0 < o_given_num:
    remi = o_given_num % 10
    sum_of_cube_of_eachDigits = sum_of_cube_of_eachDigits + (remi ** sum_of_digits)
    o_given_num = o_given_num // 10
if given_n == sum_of_cube_of_eachDigits:
    print(sum_of_cube_of_eachDigits, "is Armstrong Number")

givenNum = int(input("Enter the Number : "))
lastDigit = givenNum % 10
if 0 < lastDigit < 5:
    output = givenNum - lastDigit
    print(output)
elif lastDigit > 5:
    output = givenNum + (10-lastDigit)
    print(output)
elif lastDigit == 5:
    output = givenNum + 5
    print(output)

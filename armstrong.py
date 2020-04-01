number = int(input('enter a value: '))
result = 0
temp = number
while temp > 0:
    dig = temp % 10
    # print(dig)
    result += dig ** 3
    # print(result)
    temp //= 10
    print(temp)
if number == result:
    # print(temp)
    print(number, 'is armstrong no.')
else:

    print(number, "is not armstrong number")

num = int(input('enter the no. for factorial :'))
factorial = 1
if num < 1:
    print("factorial in never negative")

elif num == 0:
    print("factorial for this is 0!")

else:

    for i in range(1, num+1):
        print(i)
        factorial = factorial*i
    print("the factorial for",num, "is", factorial)

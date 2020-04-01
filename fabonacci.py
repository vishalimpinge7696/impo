n = int(input('enter the input:-'))
def fbs(n):
    if n <= 0:
        return 'do not exist'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fbs(n-1)+fbs(n-2)
print(fbs(n))

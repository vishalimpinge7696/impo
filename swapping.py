print('enter value for x')
x = input()
print('enter value for y')
y = input()
print('The value of x is {}'.format(x))
print('The value of y is {}'.format(y))
temp_var = x
x = y
y = temp_var
print('The value of x after swapping is {}'.format(x))
print('The value of y after swapping is {}'.format(y))


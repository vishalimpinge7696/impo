lower = int(input("Enter lower range: "))
n_input = int(input("Enter upper range: "))

for num in range(1, n_input+1):
    if num <= 0:
        print('prime no. for positive integers greater than 1')
    elif num >= 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

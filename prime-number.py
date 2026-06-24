number =int(input("Enter number :"))
num =number + 1
while True:
    for i in range(2, num):
        if (num%i == 0):
            break
    else:
        print(num)
        break
    num = num + 1


def stats(*numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    length = len(numbers)
    average = sum(numbers)/len(numbers)
    return (minimum, maximum,length, average)


print(stats(10,20,30,40))

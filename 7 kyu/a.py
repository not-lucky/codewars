def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 2
for i in infinite_sequence():
    print(i)
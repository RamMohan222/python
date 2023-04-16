def fibonacci(f1, f2, max=20, count=0):
    print(str(f1)+", ", end="")

    if count >= max:
        return
    count = count+1

    '''
    temp = f2
    f2 = f1+f2
    f1 = temp
    '''

    f2 = f1+f2
    f1 = f2-f1
    fibonacci(f1, f2, max, count)


fibonacci(f1=0, f2=1)
# output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 

t = int(input())

while(t > 0):
    t -= 1
    n = int(input())
    if(n%2 == 1):
        sumLe = 0
        i = 1
        while(i <= n):
            sumLe += float(1/float(i))
            i += 2
        print('%.6f'%sumLe)
    else:
        sumChan = 0
        i = 2
        while(i <= n):
            sumChan += float(1/float(i))
            i += 2
        print('%.6f'%sumChan)
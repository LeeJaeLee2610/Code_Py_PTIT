n = int(input())
while n:
    dem = 1
    while(n != 1):
        if n & 1:
            n = 3 * n + 1
            dem += 1
        else:
            n = n // 2
            dem += 1

    print(dem)
    n = int(input())

t = int(input())

while(t > 0):
    s = input()

    a = s.split()

    N = float(a[0])
    X = float(a[1])/100
    M = float(a[2])

    dem = 0
    while(N <= M):
        N += N*X
        dem += 1

    print(dem)

    t -= 1
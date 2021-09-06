def fibo(n):
    f1 = 0
    f2 = 1
    fn = 0
    i = 0
    while(i <= n):
        if(i <= 1):
            fn = i
        else:
            fn = f1 + f2
            f1 = f2
            f2 = fn
        i += 1
    return fn

t = int(input())
while(t > 0):
    s = input()
    a = s.split()
    
    for i in range(int(a[0]), int(a[1]) + 1):
        print(fibo(i), end=" ")

    print("")
    t -= 1
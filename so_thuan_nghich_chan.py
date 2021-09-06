def stn(n):
    m = n
    tmp = 0
    while(m > 0):
        tmp = tmp*10 + m%10
        m //= 10
    if(tmp == n):
        return True
    else: return False

def check(n):
    dem = 0
    while(n > 0):
        dem += 1
        n //= 10
    
    if(dem%2 == 0):
        return True
    else: return False

def check2(n):
    tmp = str(n)
    ok = 1
    for i in tmp:
        if(int(i)%2 == 1):
            ok = 0
    if(ok == 1):
        return True
    else: return False

t = int(input())

while(t > 0):
    s = int(input())

    for i in range(1, s):
        if(stn(i) and check(i) and check2(i)):
            print(str(i) + ' ', end="")

    print()       
    t -= 1
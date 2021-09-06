def stn(n):
    m = n
    tmp = 0
    while(m > 0):
        tmp = tmp*10 + m%10
        m //= 10
    if(tmp == n):
        return True
    else: return False

t = int(input())
while(t > 0):
    t -= 1
    s = input()
    sum = 0;
    for i in s:
        sum += int(i)

    if(stn(sum) and sum > 10):
        print("YES")
    else: print("NO")
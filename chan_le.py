t = int(input())

while(t > 0):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    ok = 1
    n = len(s)
    for i in range(0, n - 1):
        j = i + 1
        if(abs(int(s[i]) - int(s[j])) != 2):
            ok = 0
            break

    if(ok == 1 and sum%10 == 0): print("YES")
    else: print("NO")
    t -= 1
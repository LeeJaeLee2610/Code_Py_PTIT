t = int(input())

while(t > 0):
    s = input()

    ok = 1

    for i in range(0, len(s) - 1):
        if(int(s[i]) > int(s[i + 1])):
            print("NO")
            ok = 0
            break
    
    if ok: print("YES")
    t -= 1

t = int(input())

while(t > 0):
    t -= 1
    
    s = input()
    ok = 1
    i = 0
    while(i < len(s) - 3):
        j = i + 2
        if(s[i] != s[j]):
            ok = 0
            break
        i += 2
    
    if(len(s)%2 != 0 and s[0] != s[1] and ok == 1):
        print("YES")
    else: print("NO")
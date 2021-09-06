t = int(input())

while(t > 0):
    s = input()

    ok = 1
    for i in s:
        if(i != '4' and i != '7'):
            print("NO")
            ok = 0
            break;
    
    if(ok == 1): print("YES")
    t -= 1
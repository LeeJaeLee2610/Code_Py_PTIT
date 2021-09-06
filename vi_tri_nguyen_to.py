def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n//2) + 1):
        if(n%i == 0):
            return False
    return True

t = int(input())
while(t > 0):
    t -= 1;
    s = input()
    a = []
    for i in s:
        a.append(int(i));
    
    ok = 1
    for i in range(0, len(a)):
        if(snt(i) == True):
            if(snt(a[i]) == False):
                ok = 0
                break
        else:
            if(snt(a[i]) == True):
                ok = 0
                break
    
    if(ok == 1):
        print("YES")
    else: print("NO")

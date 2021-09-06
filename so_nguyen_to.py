def snt(n):
    if(n < 2):
        return False
    for i in (2, n):
        if(n%i == 0):
            return False
    return True

t = int(input())

while(t > 0):
    n = int(input())
    if(snt(n)):
        print("YES")
    else: print("NO")

    t -= 1
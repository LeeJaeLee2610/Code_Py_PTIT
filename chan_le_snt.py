def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n//2) + 1):
        if(n%i == 0):
            return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    s = input()
    sum = 0;
    for i in s:
        sum += int(i)
    
    ok1 = 1
    i = 0
    while i < len(s) - 2:
        if(int(s[i])%2 != 0):
            ok1 = 0
            break
        i += 2

    j = 1
    ok2 = 1
    while j < len(s) - 1:
        if(int(s[i])%2 != 0):
            ok2 = 0
            break
        j += 2
    
    if(ok1 == 1 and ok2 == 1 and isPrime(sum)):
        print("YES")
    else: print("NO")
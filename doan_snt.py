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
    n = 4
    a = []
    for i in range(len(s) - 4, len(s)):
        a.append(int(s[i]))

    tmp = []

    for i in a:
        tmp.append(i*pow(10, n - 1))
        n -= 1
    sum = 0
    for i in tmp:
        sum += i
    if(isPrime(sum)):
        print("YES")
    else: print("NO")
import math

def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

t = int(input())
while(t > 0):
    s = input()
    a = s.split()
    tmp1 = int(a[0])
    tmp2 = int(a[1])
    tmp = math.gcd(tmp1, tmp2)
    x = str(tmp)
    sum = 0
    for i in x:
        sum += int(i)
    if(isPrime(sum)): print("YES")
    else: print("NO")
    t -= 1
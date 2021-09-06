import math

def dao_chuoi(s):
    str = ""
    for i in s:
        str = i + str
    return str

t = int(input())

while(t > 0):
    t -= 1
    s = input()
    str = dao_chuoi(s)
    a = int(s)
    b = int(str)
    if(math.gcd(a, b) == 1):
        print("YES")
    else: print("NO")
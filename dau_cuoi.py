t = int(input())

while(t > 0):
    s = input()
    n = len(s)

    tmp = s[0:2]
    tmp1 = s[len(s) - 2 : len(s)]
    
    if(int(tmp) == int(tmp1)):
        print("YES")
    else: print("NO")
    t -= 1
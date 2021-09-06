t = int(input())
while(t > 0):
    t -= 1
    s = input()
    sum = 0
    tich = 1
    ok = 1
    for i in range(0,len(s)):
        if i % 2 == 0:
            sum += int( s[i] )
        else:
            if( s[i] != '0'):
                ok = 0
                tich *= int(s[i])
    print(sum," ", end="")
    if(ok == 1):
        print(0)
    else: print(tich)
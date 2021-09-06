p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

n = input()
a = n.split()
k = int(a[0])
s = a[1]

res = []

while k:
    res.clear()

    for i in s:
        res.append(p[(p.find(i) + k)%28])
    res.reverse()
    for i in res:
        print(i, end="")

    print("")
    
    n = input()
    if(n == '0'):
        break;
    else:
        a = n.split()
        k = int(a[0])
        s = a[1]
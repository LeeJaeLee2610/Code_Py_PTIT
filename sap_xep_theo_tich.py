def tong_chu_so(n):
    sum = 1
    while(n > 0):
        sum *= n%10
        n //= 10
    return sum

t = int(input())

while(t > 0):
    t -= 1

    n = int(input())
    s = input()
    s = s.split()
    a = []
    for i in s:
        a.append(int(i))

    a.sort()
    
    hash = dict()
    for i in a:
        hash[int(i)] = tong_chu_so(i)
    
    hash_sorted = sorted(hash.items(), key = lambda x:x[1],reverse=False)

    for i in hash_sorted:
        print(i[0]," ",end="")
    print("")
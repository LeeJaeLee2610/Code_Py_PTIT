import math
def snt(n):
    if(n < 2):
        return False
    for i in range(2, int(n//2)+1):
        if(n%i == 0):
            return False
            break
    
    return True

n = int(input())

s = input()
a = s.split()

tmp = []

for i in a:
    if(snt(int(i))):
        tmp.append(int(i))

ok = [False for i in range(len(tmp))]

for i in range(len(tmp)):

    if(ok[i] == True):
        continue
    dem = 1
    for j in range(i + 1, len(tmp), 1):
        if(tmp[i] == tmp[j]):
            ok[j] = True
            dem += 1

    print(tmp[i], dem)
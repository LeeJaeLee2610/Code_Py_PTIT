def snt(n):
    if(n < 2):
        return 0
    for i in range(2, int(n//2) + 1):
        if(n%i == 0):
            return 0
    return 1

n = input()
n1 = n.split()

rows, cols = (int(n1[0]), int(n1[1]))
a = []
for i in range(rows):
    s = input()
    tmp = s.split()
    a.append(tmp)

for i in range(rows):
    for j in range(cols):
        if(snt(int(a[i][j]))):
            a[i][j] = str(1)
        else: a[i][j] = str(0)

for i in range(rows):
    for j in range(cols):
        print(int(a[i][j]), end="")
        print(" ", end="")
    print()
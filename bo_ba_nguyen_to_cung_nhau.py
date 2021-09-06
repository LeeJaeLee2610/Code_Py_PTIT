import math

s = input()
a = s.split()

l = int(a[0])
r = int(a[1])
a = []
for i in range(l, r + 1):
    a.append(i)

for i in range(0, len(a) - 2):
    for j in range(i + 1, len(a) - 1):
        for k in range(j + 1, len(a)):
            if(math.gcd(a[i], a[j]) == 1 and math.gcd(a[j], a[k]) == 1 and math.gcd(a[i], a[k]) == 1):
                print("(", end="")
                print(a[i], end=", ")
                print(a[j], end=", ")
                print(a[k], end="")
                print(")", end="")
                print()
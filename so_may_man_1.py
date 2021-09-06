s = input()

c1 = 0
c2 = 0

for i in s:
    if i == '4':
        c1 += 1
    elif i == '7':
        c2 += 1

c = c1 + c2

if c == 4 or c == 7:
    print("YES")
else: print("NO")
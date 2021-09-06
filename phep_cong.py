s = input()

a = []
dem1 = 0
sum1 = 0
for i in s:
    if(i.isnumeric()):
        dem1 += 1
    elif(i == '+'):
        break

for i in s:
    if(i.isnumeric()):
        a.append(int(i)*pow(10, dem1 - 1))
        dem1 -= 1
    elif(i == '+'):
        break

for i in a:
    sum1 += i

b = []
dem2 = 0
sum2 = 0

for i in range(len(a) + 1, len(s)):
    if(s[i].isnumeric()):
        dem2 += 1
    elif(s[i] == '='):
        break

for i in range(len(a) + 1, len(s)):
    if(s[i].isnumeric()):
        b.append(int(s[i])*pow(10, dem2 - 1))
        dem2 -= 1
    elif(s[i] == '='):
        break

for i in b:
    sum2 += i

c = []
dem3 = 0
sum3 = 0

for i in range(len(a) + len(b) + 4, len(s)):
    if(s[i].isnumeric()):
        dem3 += 1

for i in range(len(a) + len(b) + 4, len(s)):
    if(s[i].isnumeric()):
        c.append(int(s[i])*pow(10, dem3 - 1))
        dem3 -= 1

for i in c:
    sum3 += i

if(sum1 + sum2 == sum3): print("YES")
else: print("NO")
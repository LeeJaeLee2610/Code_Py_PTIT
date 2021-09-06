n = int(input())
s = input()
s = s.split()
a = []

for i in s:
    a.append(int(i))

dem = 0

i = 0
while i < len(a) - 1:
    if(a[i] != a[i + 1]):
        dem += 1
    i += 1

print(dem)
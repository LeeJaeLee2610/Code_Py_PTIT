n = int(input())

s = input()
dem = 0

a = s.split(" ")
for i in range(0, n):
    a[i] = int(a[i])

for i in range(0, n - 1):
    j = i + 1
    for j in range(i + 1, n):
        if(a[i] > a[j]):
            dem += 1

print(dem)
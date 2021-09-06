n = int(input())
a = []
for i in range(0, n):
    tmp = input()
    a.insert(i, tmp)
    a[i] = a[i].split()

k = int(input())
sum_up = 0
sum_beneath = 0

for i in range(0, n - 1):
    for j in range(0, n - i- 1):
        sum_up += int(a[i][j])
        sum_beneath += int(a[n - i - 1][n - j - 1])

res = abs(sum_up - sum_beneath)

if(res > k):
    print("NO")
    print(res)
else:
    print("YES")
    print(res)
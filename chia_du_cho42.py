dem = 0
a = []

while dem < 10:
    s = input()
    s = s.split()
    for i in s:
        dem += 1
        a.append(int(i)%42)

count = 0

tmp = dict()

for i in a:
    if i in tmp:
        tmp[i] += 1
    else: tmp[i] = 1;

for i in tmp:
    count += 1

print(count)
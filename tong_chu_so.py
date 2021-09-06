s = input()

sum = 0
while(len(s) == 1):
    for i in s:
        sum += int(i)
    s = str(sum)

print(sum)
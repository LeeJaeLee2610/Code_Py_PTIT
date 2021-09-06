t = int(input())

while(t > 0):
    s = input()
    
    n = len(s)
    i = 0
    while(i < n):
        dem = 1
        while(i < n - 1 and s[i] == s[i + 1]):
            dem += 1
            i += 1
        i += 1
        print(str(dem) + s[i - 1], end="")
    print()
    t -= 1
t = int(input())

while(t > 0):
    s = input()

    tmp = s[len(s) - 2 : len(s)]

    if (tmp == "86"):
        print("YES")
    else: print("NO")
    t -= 1
t = int(input())

while(t > 0):
    s = input()

    for i in range(0, len(s)):
        if(s[i].isnumeric()):
            for j in range(0, int(s[i])):
                print(s[i - 1], end="")

    print("")
    t -= 1
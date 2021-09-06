t = int(input())

while(t > 0):
    t -= 1
    s = input()
    
    tmp = ""
    sum = 0
    for i in s:
        if(i.isalpha()):
            tmp += i
        else: sum += int(i)

    tmp = ''.join(sorted(tmp))
    print(tmp+str(sum))

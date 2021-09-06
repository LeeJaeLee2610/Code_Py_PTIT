
n=int(input())
while n > 0:
    n-=1
    m=int(input())
    array=input().split()
    array=list(map(int, array))
    array1=input().split()
    array1=list(map(int, array1))
    array.sort()
    array1.sort()
    check = int(0)
    for x in range(0, m-1):
        if array[x]>array1[x]:
            print("NO")
            check = int(1)
            break
    if check == int(0):
        print("YES")
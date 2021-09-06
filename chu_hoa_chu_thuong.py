s = input()

dem = 0
dem1 = 0

for i in s:
    if(i >= 'a' and i <= 'z'):
        dem += 1
    elif(i >= 'A' and i <= 'Z'):
        dem1 += 1

if(dem > dem1):
    print(s.lower())
else: print(s.upper())

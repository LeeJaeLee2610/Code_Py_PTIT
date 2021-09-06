from os import sep


s1 = input()
s2 = input()
p = int(input())

print(s1[:p - 1], s2, s1[p - 1: len(s1)], sep="")
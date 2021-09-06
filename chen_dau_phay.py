def xu_li(s):
    str = ""
    for i in s:
        str = i + str
    return str

test_str = input("")
tmp = xu_li(test_str)
res = ','.join(tmp[i:i + 3] for i in range(0, len(tmp), 3))
tmp1 = xu_li(res)
print(tmp1)
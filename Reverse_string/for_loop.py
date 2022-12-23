def rev_string_loop(s):
    res = ''
    for x in s:
        print(x)
        res = x + res
        print(res)
    return res

print(rev_string_loop("palani"))
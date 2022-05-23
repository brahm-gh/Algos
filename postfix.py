def post_fix(s):
    l = []
    l2 = []
    operator = None
    for i in range(len(s)):
        l.append(s[i])

    for i in range(len(l)):
        if l[i] in ['+', '-', '*', '/'] and l[i+1] in ['+', '-', '*', '/']:
            l.insert(i-2, l[i+1])
            l2.append(l[i+2])
            l.pop(i+2)

        elif l[i] in ['+', '-', '*', '/']:
            operator = l[i]
            l[i] = l[i-1]
            l[i-1] = operator
            exp = ''.join([l[i-2], l[i-1], l[i]])
            res = eval(exp)
            l.pop(i)
            l.pop(i-1)
            l.pop(i-2)
            l.insert(i-2, str(res))
            i-=2


post_fix('5+2')






class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


def post_fix(s):
    stack = ArrayStack()
    l = []

    for i in range(len(s)):
        l.append(s[i])




    for i in range(len(l)):
        if l[i] in ['+', '-', '*', '/']:
            l2 = []
            a = stack.pop()
            b = stack.pop()
            l2.append(b)
            l2.append(l[i])
            l2.append(a)
            exp = ''.join(l2)
            res = eval(exp)
            stack.push(str(res))


        else:
            stack.push((l[i]))

    return float(stack.top())


print(post_fix('52+83-*4/'))





class EvalPostfix:
    def __init__(self):
        self.stack = []
        self.top = -1

    def pop(self):
        if self.top == -1:
            return
        else:
            self.top -= 1
            return self.stack.pop()

    def push(self, i):
        self.top += 1
        self.stack.append(i)

    def calculate(self, expression):
        for i in expression:
            try:
                self.push(int(i))
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()
                if i == '/':
                    self.push(val2 / val1)
                if i == '*':
                    self.push(val2 * val1)
                if i == '+':
                    self.push(val2 + val1)
                if i == '-':
                    self.push(val2 - val1)
        return int(self.pop())


'''str_postfix_expression = '100 200 + 2 / 5 * 7 + '
strconv = str_postfix_expression.split(' ')
obj = EvalPostfix()
print(f"{obj.calculate(strconv)}")'''

str_postfix_expression = input("Input the postfix expression : ")
strconv = str_postfix_expression.split(' ')
obj = EvalPostfix()
print(f"The result is {obj.calculate(strconv)}")

class Calc:
    a = 0
    b = 0
    def __init__(self):
        self.a = int(raw_input())
        self.b = int(raw_input())
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

c = Calc()
op=['+','-','*','/']
flag=True
while flag:
    print('1. + \t2. - \t3. * \t4. / ')
    x=int(raw_input())
    for index,value in enumerate(op):
         if index == x-1:
             if value == '+':
                 res=c.add()
                 flag=False

             elif value == '-':
                 res=c.sub()
                 flag=False

             elif value == '*':
                 res=c.mul()
                 flag=False
             elif value == '/':
                 res=c.div()
                 flag=False
print res

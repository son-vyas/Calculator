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
    def mul():
        return self.a * self.b
    def div():
        return self.a / self.b

c = Calc()
op=['+','-','*','/']
while True:
    print('1. + \t2. - \t3. * \t4. / ')

sum = c.add()
print sum

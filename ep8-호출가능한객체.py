class Calculator(object):
    def __init__(self, base):
        self.base = base

    # def mysum(self, x,y):
    #     return self.base + x + y

    def __call__(self, x, y): # 이과 같이 작성하면 인스턴스 이름으로 함수를 실행 할 수 있다
        return self.base + x+  y


calculator = Calculator(10)
# print(calculator())

calc2 = Calculator(10)
print(calc2.__call__(10,20))  #
print(calc2(10,200))

"""
Iterables Iterator Generators

클래스를 통한 Iterable 객체 만들기
"""
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):  #iterator를 요구받고, 현 instance에서 next 처리
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration # 남은 요소가 없을 때, StopIteration 강제 발생

        value = self.start
        self.start += 1
        return value

#
iterable = MyRange(0,3) # 클래스를 사용하여 클래스 자체로 반복을 실행 시키고 싶을 경우 위와 같은 방법으로 동작 시킨다

for i in iterable:
    print(i)

myrange = MyRange(0,3)
iterator = iter(myrange)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

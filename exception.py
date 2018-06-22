"""
traceback
-> 어떤 예외가 발생하면 이 예외가 발생했는지 확인을 할 수 있다.

ValueEorr
print('line1')
val = int('a')+1  -> 실행이 중단.
print('line2')

예외잡기
try ~ ecept 잡을 예외의 종류 as e:
    print(e)

예외 종류

IndexError : 범퀴 밖의 인덱스 참조시
KeyError   : 존재하지 않는 key에 접근시 -> 사전에서 발생
NameError  : local/global name 을 찾지모한 경우
TypeError  : 부적절한 연산/함수를 적용했을 때, 예) '1'+1
ValueEorr  : 부적절한 값을 발견했을 때 예 int('a`')
IndentationError    : 소스코드 내에 부적절한 들여쓰기가 있을
NotImplementedError : 아직 구현하지 않은 부분임을 명시








print('line1')
try:
    value = int('a') + 1
except ValueEorr as e:
    print(e)
print('line2')

위의 코드를 실행 시키면! 예외처리를 하고 다음 코드가 실행된다.

int('10', base=16)
-> a [ 16 진수로 표현할 수 있다. ]



"""


def fn1(x,y):
    return x + y

def fn2(a,b):
    return 10 * fn1(a,b)

print('line1')
try:
    print(fn2('a',10))
    print('line2')
except TypeError as e:
    print(e)
    print('line3')
print('line4')


try:
    import AskDjango
except ImportError as e:
    print(e)
    print('line error')


"""
NotImplementedError  예시
아직 구현하지 않은 부분임을 명시
"""
class Person:
    def run(self):
        raise NotImplementedError

class Doctor:
    pass


class Developer(Person):

    def run(self):
        print('개발자는 오늘도 뜁니다.')

#Doctor().run() #ß NotImplementedError 발생 자식 클래스에게 run함수 구현 Override 강제 효과
Developer().run()


print(" ")
# def mysum(x,y):
#     pass
#
# mysum(10,20)





try:
    pass #실행! 예외 발생으로 예상되는 구간,
except:
    pass #예외 발생하면 실행
else:
    pass #예외 없으면 실행
finally:
    pass #무조건 실행

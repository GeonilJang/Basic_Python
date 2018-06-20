print("hello world with python")

# def mysum1():
#      fn = lambda x , y : x+ y
#      return fn
#
# myfn = mysum1()
# print(myfn(10,30))


# def base_10(fn):
#     def wrap(x,y):
#         return fn(x,y) + 10
#     return wrap
#
# def mysum(x,y):
#     return x+y
#
#
# myf = base_10(mysum)
# print(myf(10,10))


"""
@장식자
1) 정의 되어있는 함수 안에 인자로 함수를 받는다.
2) 인자로 받은 함수를 정의 하고자한 함수 안에서 사용가능하다.
3) 인자로 넣어 주고 싶은 함수를 만든다
* 즉 내가 사용가는 함수가 있고 이 기능을 추가 하고 싶을때
내가 사용하는 함수를 내가 추가하고 싶은 함수를 구현 하기위하여 인자로 넣어준다.

f1 : 이미 사용중인 함수
my : f1의 기능 만으로는 완벽한 기능을 구현 할 수 없어 기능 추가를 원한다.

my(f1)  ->  이런식으로 내가 원하는 함수를 커스텀 한다.

ex)

def sum(x,y):
    return x+y

위 함수가 있는데 더하기 뿐만 아니 더한 값에 10을 곱해서 리턴해주는 함수를 만들고 싶다.

def myfuntion(fn): -> 여기서 fn 으로 위의 sum함수를 담을 것이다.
    def newFuntion(x,y): -> newFuntion을 리턴 받는 함수로 사용하겠다.
        return fn(x,y) * 10
    return newFuntion

customFnc = myFuntion(sum) -> 이렇게 하면 newFuntion(x,y) 함수가 리턴이 된다.
customFun(10,20) -> return sum(x,y) * 10 이 된다 즉! sum 함수를 실행하고 그다음
                    그 값에 *10 을 해서 리턴을 해준다 어려운것이아니다.
30 * 10 = 300 이된다.



"""

def base_30(fn):
    def wrap(x,y,z):
        return "x:{}, y: {} z:{} [ {} ]".format(x,y,z,fn(x,y,z))
    return wrap
#
# def cal(x,y,z):
#     if(z =='+'):
#         return "{}+{}={}".format(x,y,x+y)
#     elif(z == "-"):
#         return "{}-{}={}".format(x,y,x-y)
#     else:
#         print("wrong")
#         return False
#
#
# myf = base_30(cal)
# print(myf(10,20,'ㅌs'))

"""
@장식자 사용번 -> 동일한 결과 다른 방식
위 주석 부분을 아래 처럼 사용할 수있다.

오! 아래와 같은방법으로 사용하면 동일한 함수 이름으로도 사용이 가능하네..
아 그냥 변수로밭을때 똑같이 받으면되는거구나....



###

리터 받은 함수의 인자값은 제일 겉에서 입력하는 값이고 안에서 사용할 함수의 인수 갯수만 잘
맞춰서 사용해주면 된다
"""
@base_30 #->이 문법 아래에 나오는 함수를 인자로 받아서 사용하겠다. 라는 의미가 된다.
def cal(x,y,z='+'):
    if(z=='+'):
        return "{}+{}={}".format(x,y,x+y)
    elif(z=='-'):
        return "{}-{}={}".format(x,y,x-y)
    else:
        print('wrong')
        return False


print(cal(70,20,'-'))










"""
메모리즈 패턴


함수 호출시 동일한 인자가 들어와서 여러번 실행할때 동작 시간을
감소시킬수 있는 중요한 방법이다.
"""
import time

def myf(fn):
    cached = {}
    def wrap(x,y):
        key = (x,y)
        if key not in cached:
            cached[key] = fn(x,y)
        return cached[key]
    return wrap

@myf
def mylongtime1(x,y):
    time.sleep(1)
    return x+y+10


def mylongtime2(x,y):
    time.sleep(1)
    return (x*y)+10





print(mylongtime1(10,20))
print(mylongtime1(10,20))
print(mylongtime1(10,20))
print(mylongtime2(120,20))
print(mylongtime2(120,20))
print(mylongtime2(130,20))

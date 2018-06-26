"""
+함수는 <작업 지시서>와 같은 개념
 -> 코드 중족을 제거하기 위한 목적
+함수의 구성
 -> 1개의 함수명 (필수): 작업의 이름
 -> 0개 이상의 인자값 (옵션): 작업에 필요한 정보
 -> 1개의 반환값 (옵션): 작업의 결과를 하나 돌려 받습니다.

+ 코드의 중복을 제거하기 위해서 가장 필요한 문법
+ 빌트인 함수: print. range 등..
+ 반환 값이 없는 경우 None is not None


1급 객체이다 => 함수를 리턴 받을 수 있다


++ 인자 ++
함수에 들어가는 값!

디폴트 인자 문법이 함께 적용 : 함수 호출 실에 해당 인자를 지정하지 않으면, 디폴트 인자값으로 값이 자동지정
ex)

def fn_with_keyword_arguments(name ="", age=0):
    print("당신의 이름은 {}이며, 나이는 {}입니다.".format(name, age))

라고 정의했을때! name = /
fn_with_keyword_arguments(name="geonil")
fn_with_keyword_arguments(age=10)
fn_with_keyword_arguments(name="geonil", age=10)
fn_with_keyword_arguments()


********
Packing*
********

+인자의 갯수를 제한하지 않고, 다수의 인자를 받을 수 있음
+다수의 Positional Arguments를 하나의 tuple로서 받을 수 있음

def fn2(*colors):
    for color in colors:
        print(color)

**colors
-> name ="dw" age=23 (이런식으로 키워드 있는 인자값을 많이 받고 싶을때)




*********
lambda x,y : x+y





*********
1급객체!!
인자로 넘기기, 변수에 대입하기등
종류 : 일급 함수 / 클래수를 지원


*******
고차함수
+ 다른 함수를 생산/소비하는 함수
+ 다른 함수를 인자로 받거나, 그 결과로 함수를 반환하는 함수

def base_calculator(base):
    wrap = lambda x,  y : base + x +y
    return wrap







"""


# def fn2(*colors):
#     for color in colors:
#         print(color)
#
#
# fn2("geonil","ge","ge","geeewew","gwqeg")




def sum(x,y):
    return x+y
def base_calculator(fn):

    def wrap(x,y):
        return fn(x,y)+10
    return wrap


# def base_calculator(base):
#     wrap = lambda x, y : base + x + y
#     return wrap


myfunction1 = base_calculator(sum)
print(myfunction1(10,20))

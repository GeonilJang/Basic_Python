"""
지정 클래스 타입의 변수 = 인스턴스
인스턴스 생성 문법
 + 함수를 호출 하듯이, 클래스를 호출하여 인스턴스 생성
클래스가 호출이 될 때, 클래스내 __init__ 함수가 자동 호출
 + 생성자 Constructor 라 하며, 해당 인스턴스를 초기화 하는 역할
 + 클랙스 호출 시에 넘겨진 인자는 모두 생성자의 인자로 넘겨짐.
인스턴스를 위한 함수/ 변수들을 인스턴스 함수, 인스턴스 변수  -> 필드/ 메소드


"""

class Circle(object):
    def __init__(self, x, y, radius): #생성자
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return self.radius **2

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2 - (self.radius + other.radius))


"""
자바코드 예

import java.util.ArrayList;

public class Dog{
    ArrayList <String> tricks;

    public Dog(){
        this.tricks = new ArrayList<String>();
    }

    public void add_trick(String trick){
        this.tricks.add(trick)
    }


    public static void main(String[] args){
        Dog dog1 = new Dog();
        dog1.add_strick("roll over");

        System.out.println(dog1.tricks)

    }


}
"""



class Dog:
    th = [] # 클래스 변수 -> 클래스를 사용하고 있는 인스턴스들이 공유하고 있는 변수 이다
    def __init__(self):
        self.tricks = [] #이것이 인스턴스 변수입니다. - 각 인스턴스만 사용하는 변수를 말합니다.

    def add_trick(self, trick):
        self.tricks.append(trick)
        self.th.append(trick)



dog1 = Dog()
dog1.add_trick("roll over")
print(dog1.tricks)

dog2 = Dog()
dog2.add_trick("play dead")
print(dog2.tricks)

print(dog1.th)




"""
데이터 은닉과 이름장식

+ mangle: [동사] 짓이기다. 심하게 훼손하다.
+ 파이썬에서는 접근 제한다 (public, private, protected)미지원
+ 언더스코어 2개(__)로 시작하는 이름에 한하여 이름을 변경 (Name Mangling)기법을 제공
 -> 인스턴스 함수 내에서는 이름 그대로 접근
 -> 클래스 밖에서는 "_클래스명변수명"으로 접근
ex_)
"""
class Person:
    def __init__(self,name):
        self.__name = name
        self.geonil = name

    def say_hello(self):
        print("안녕 {}.".format(self.__name)) #함수 안에서는 접근이 가능

geonil = Person("geonil")
geonil.say_hello()
#그러나 아래처럼은 접근이 불가능 하다
print(geonil.geonil)
print(geonil.__name)

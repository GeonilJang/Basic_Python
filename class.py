"""
상송(Inheritance)
+ 코드 중복을 최소화 하기 위한 목적으로 등장
+ 파이썬 클래스는 최상위 object 를 상속
  -> 파이썬2 에서는 object상속 유무에 따라 old/new style class로 분리
  -> 파이썬2 에서는 old-style class가 제거
 + 클래스 간에 상속관계에 놓이게 되면, 부모/자식 관계가 성립
 + 자식 클래스는 부모 클래스의 모든 내역을 물려받음
 + 다중상속 지원 : 직계 부보가 다수
   ->class Myclass(부모1, 부모2):


MRO(Method Resolution Order)
+파이썬의 클래스 탐색순서는 MRO를 따릅니다.
 -> Class.mro를 통해 확인 가능
 +MRO 가 꼬이도록 클래스를 설계할 수는 없습니다.
  -> TypeError: Cannot create a consistent method Resolution order(MRO)

"""

#뛰고 먹고 자고 공부하고
# Doctor Programmer Designer
#ex)
"""
class Doctor:
    def __init__(self, name):
        self.name = name
        print("{}님 입니다.".format(self.name))

    def run(self):
        print("{} 달리기.".format(self.name))

    def eat(self):
        print("{} 먹습니다.".format(self.name))

    def sleep(self):
        print("{} 먹습니다.".format(self.name))

    def study(self):
        print("{} 공부합니다.".format(self.name))

    def research(self):
        print("연구하기")

class Programmer:
    def __init__(self, name):
        self.name = name
        print("{}님 입니다.".format(self.name))

    def run(self):
        print("{} 달리기.".format(self.name))

    def eat(self):
        print("{} 먹습니다.".format(self.name))

    def sleep(self):
        print("{} 먹습니다.".format(self.name))

    def study(self):
        print("{} 공부합니다.".format(self.name))

    def research(self):
        print("개발하")


class Designer:
    def __init__(self, name):
        self.name = name
        print("{}님 입니다.".format(self.name))

    def run(self):
        print("{} 달리기.".format(self.name))

    def eat(self):
        print("{} 먹습니다.".format(self.name))

    def sleep(self):
        print("{} 먹습니다.".format(self.name))

    def study(self):
        print("{} 공부합니다.".format(self.name))

    def design(self):
        print("디자인하기")
"""



# doc = Doctor('goenil')

# doc.run()
# doc.eat()
# doc.sleep()
# doc.study()
# doc.research()



"""
위 코드를 상속으로 중복 해결
"""
class Person(object):
    def __init__(self, name):
        self.name = name
        print("{}님 입니다.".format(self.name))

    def run(self):
        print("{} 달리기.".format(self.name))

    def eat(self, food):
        print("{} 먹습니다.".format(food))

    def sleep(self):
        print("{} 잡니다.".format(self.name))

    def study(self):
        print("{} 공부합니다.".format(self.name))



class Doctor(Person):
    def research(self, sub):
        print("열심히 {}를 연구합니다.".format(sub))

class Programmer(Person):
    def coding(self):
        print("개발중")

class Designer(Person):
    def draw(self):
        print("그리기")


doc = Doctor('geonil')
doc.run()
doc.eat('김밥')
doc.sleep()
doc.study()
doc.research('You')

"""

module.py
pkg1
 /----> __init__.py
 /----> pkg2
          /----> __init__.py

import pkg1 -> pkg1/__init__.py 를 콜
import pkg1.pkg2 -> pkg1/pkg2/__init__.py를 콜


ex)
[1]
import mymodule1
mymodule1.mysum(1,2)

[2]
import pkg1.pkg2
pkg1.pkg2.mysum(1,2)

from pkg1.pkg2 import mymodule1
mymodule1.mysum(1,2)


modules  : 파일
packages : 폴더

"""


# import mymodule
# print(mymodule.mysum(10,20))

from mymodule import mysum
print(mysum(10,20))

import sys
for pa in sys.path:
    print(pa)


"""
최초 시작 __main__  >>> python a.py  -> __name__ = __main__ 이된다
임포트틑 __name__ 이다 __name__ = __name__이 된다

"""

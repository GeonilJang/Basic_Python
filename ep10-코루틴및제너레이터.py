"""
"""


from __future__ import unicode_literals
import time

begin_t = time.time()

gen = ( i for i in range(10000000))

for i in range(10000000):
    print(i)

print("{}초 소요".format((time.time() - begin_t)/60))


"""
def co_routine():
    yield 10
    yield 20
    yield 30


generator1 = co_routine()

next(generator1)   #next를 사용해야 사용이 된다
10
next(generator1)
20
next(generator1)
30
"""

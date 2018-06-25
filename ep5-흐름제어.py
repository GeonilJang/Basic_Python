"""
if 문

if 조건:
    pass
elif 조건:
    pass
elif 조건:
    pass
else:
    pass

if/ else는 1회만 쓸 수 있으나. elif는 제한 없이 사용할 수 있다.


+++ +++
* 입력 = input("입력하세요.") -> String 타입
"""

for i in range(2,9,2):
    for j in range(1,10):
        print("{} x {} = {}.\n".format(i,j,i*j))

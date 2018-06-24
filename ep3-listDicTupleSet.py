"""
여러 원소들을 가지고 있는 자료구조
+ list / deque
+ set  / fronzensets
+ dic / defaultdict, OderedDoict, Counter
+ tuple / namedtuplse

in 문법
"geonil" in "hello geonil" -> True


list = [1,3,4,5,6]
1) list[-2] -> 5
2) for i in list:
     print(i)

3)
list.append(값) : 끝에추가
list.pop(index) : 특정인덱스 값 제거밑 return
list.remove(값) : 특정 값을제거
list.insert(index, 값) : 특정 위치 값추가


슬라이스 [시작인덱스 : 끝인덱스 : 인덱스 증가량]
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2  -> [1,2,3,4,5,6]


list3[1:] 최초 부터 끝
list3[:8] 8미만 까지
list3[1:8:2] 1 부터 8미만 인텍스 사이를 2칸씩 뛰어서
list3[::-1] 거꾸로

"""

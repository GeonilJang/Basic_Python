"""
sorted

sorted_list = sorted(iterable, key = None, reverse =False)
+ key : 정렬기준값을 생성할 함수를 시정. iterable 객체의 각 원소마다 key함수가 호출 되고 그리턴값으로 정렬을 수행

"""

def sort_fn(value):
    return value%10 #일의 자리수로 정렬

sorted_list = sorted([19,25,32,45] , key=sort_fn, reverse=True)
print(sorted_list)
#[19, 25, 45, 32]
sorted_list = sorted([19,25,32,45] , key=sort_fn, reverse=False)
print(sorted_list)
#[32, 25, 45, 19]


"""
filter
+ 지정함수로 필터링된 결과를 생산할 Iterator를 반환

각 원소마다 지정함수가 호출되어, 리턴값이 True 판정될 경우 통과

iterator = filter(필터링여부를 결정할 함수 , iterable)
"""
def judge_fn(value):
    return value % 2 == 0 #짝수만 통과

iterator = sorted(filter(judge_fn, [6,10,3,2,1,100]))
print(list(iterator))





"""
map
+ 지정함수의 리턴값을 반환할 Iterator 반환

iterator = map(값을변환할함수, iterable)
"""
def power_fn(value):
    return value **2

iterable = map(power_fn,[1,2,3,4,5])
print(list(iterable))



"""필터와 map 엮기"""

maped = map(lambda j : j**2 , filter(lambda i : i%2 == 0, [10,9,8,7,6,5,4,3,2,1]))
print(list(maped))




"""
max min
+빈 리스트일 경우 디폴트 값이 출력됩니다
"""
print(max([1,2,3,4,-19], default = 0 ,key=lambda x : abs(x)))
print(min([1,2,3,4,-19], default = 0 ,key=lambda x : abs(x)))



"""
list에는
list.sort() 함수를 지원한다 리턴 값이 없으며 자체를 소트한다
"""

def fn(value):
    # fn_list = []
    # fn_list.append(value)
    # sorted_fn_list1 = sorted(fn_list, key=lambda x:len(str(x)))
    # print("첫 번째",sorted_fn_list1)
    # sorted_fn_list2 = sorted(sorted_fn_list1, key=lambda x : x%10)
    # return sorted_fn_list2
    return(len(str(value)), value%10)

mylist = [10,11,9,20,12,313,211,121]
mylist.sort(key = fn)
# mylist.sort(key = lambda x : (len(str(x)), x%10, x/100))
print(mylist)

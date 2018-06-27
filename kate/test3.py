"""
    3	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]	50
    3	[“Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”]	21
    2	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]	60
    5	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]	52
    2	[“Jeju”, “Pangyo”, “NewYork”, “newyork”]	16
    0	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]	25
"""

from testCase import cases

caches = [3,3,2,5,2,0]
i = 0
time = 0
for list in cases:
    cache = caches[i]
    i += 1
    if cache > 0:
        incache = [0 for j in range(cache)] #캐시크기 초기화
        print(" ")
        print("최초 캐쉬 : ",incache)
        for item in list:
            if item.upper() in incache: #캐시안에 값 조회 후 있으면 +1
                time += 1
            else: #캐시안에 값 조회 후 없으면 대문자로 캐쉬에 담기 +5
                time += 5
                if(len(incache) == 3):
                    incache.pop(0)
                incache.append(item.upper())
    else:
        print(" ")
        print("최초 캐쉬 : ",incache)
        time = len(list)*5

    print("{i}번째, 캐쉬 사이즈 : {incache}, 런타임 : {time}".format(i=i, time=time, incache=len(incache)))
    time = 0
    incache = []

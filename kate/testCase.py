t1 = "1S2D*3T"
t2 = "1D2S#10S"
t3 = "1D2S0T"
t4 = "1S*2T*3S"
t5 = "1D#2S*3S"
t6 = "1T2D3D#"
t7 = "1D2S3T*"

testList = [t1, t2, t3, t4, t5, t6, t7]


"""
    3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
    3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
    2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
    5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
    2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
    0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25
"""

cases = [
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
    ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
    ["Jeju", "Pangyo", "NewYork", "newyork"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"],

]

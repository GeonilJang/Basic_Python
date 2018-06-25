"""
1	1S2D*3T	    37	    1^1 * 2 + 2^2 * 2 + 3^3
2	1D2S#10S	9	    1^2 + 2^1 * (-1) + 10^1
3	1D2S0T	    3	    1^2 + 2^1 + 0^3
4	1S*2T*3S	23	    1^1 * 2 * 2 + 2^3 * 2 + 3^1
5	1D#2S*3S	5	    1^2 * (-1) * 2 + 2^1 * 2 + 3^1
6	1T2D3D#	    -4	    1^3 + 2^2 + 3^2 * (-1)
7	1D2S3T*	    59	    1^2 + 2^1 * 2 + 3^3 * 2

"""
import re
from testCase import testList

def checkOption(option):
    if(option == '*'):
        return "2"
    elif(option == '#'):
        return "-1"
    else:
        return "1"

def checkScore(testCase):
    score = 0
    option = ""
    datas = dict()
    games = re.split(r'(\d\d?[S|T|D][*|#]{0,1})(\d\d?[S|T|D][*|#]{0,1})(\d\d?[S|T|D][*|#]{0,1})', testCase)

    print(" ")
    print("게임 : ",games)
    print(" ")

    for i in range(1, 4):
        ele = re.split(r'(\d\d?)([S|T|D])([*|#]{0,1})', games[i])
        if('S' in ele[2]):
            score = int(ele[1])
            option = ele[3]
        elif('D' in ele[2]):
            score = int(ele[1])**2
            option = ele[3]
        elif('T' in ele[2]):
            score = int(ele[1])**3
            option = ele[3]
        else:
            print("You got wrong a game option")

        datas[i-1]=[score, int(checkOption(option))]
    return datas


j=0
k=0
result = [1, 1, 1]
for testCase in testList:
    out1 = checkScore(testCase)
    print("{out1} 딕셔너리".format(out1=out1))
    for i in range(3):
        if(i == 0):
            if(out1[1][1] == 2 and out1[0][1] == -1):
                result[i] = out1[0][0] * -2
            elif(out1[1][1] == 2):
                result[i] = out1[0][0] * 2
            elif(out1[0][1] == -1):
                result[i] = out1[0][0] * -1
            elif(out1[0][1] == 2 and out1[1][1] == 2):
                result[i] = out1[0][0] * 4
        elif(i == 1):
            if(out1[0][1] == -1 and out1[1][1] == 2):
                result[i] = out1[1][0] * -2
            elif(out1[1][1] == 2 and out1[2][1] == 2):
                result[i] = out1[1][0] * 4
            elif(out1[])


























        print(result)

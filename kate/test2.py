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

result = [1, 1, 1]

for testCase in testList:
    dicValue = checkScore(testCase)
<<<<<<< HEAD
    # print("{dicValue} 딕셔너리".format(dicValue=dicValue))
    for i in range(3):
        if(i > 0):
            if(dicValue[i][1] == -1):
                result[i] = dicValue[i][0]*(-1)
            elif(dicValue[i][1] == 2):
                result[i] = dicValue[i][0]*2
                result[i-1] = result[i-1]*2
            else:
                result[i] = dicValue[i][0]*dicValue[i][1]
        else:
            result[i] = dicValue[i][0]*dicValue[i][1]

=======
    print("{dicValue} 딕셔너리".format(dicValue=dicValue))
    for i in range(3):
        if(i > 0):
            if(dicValue[i][1] == 2):
                result[i-1] = result[i-1]*2
                result[i] = dicValue[i][0]*2
            elif(dicValue[i][1] == -1):
                result[i] = dicValue[i][0]*-1
            else:
                result[i] = dicValue[i][0]
        else:
            result[i] = dicValue[i][0] * dicValue[i][1]
>>>>>>> 92a47b40bd8356848cc55718fcd9c51f20d4b429
    print(sum(result))

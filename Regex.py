data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit(): #park 주문번호
            word = word[:6] + "-" + "*******"
        word_result.append(word) #차례대로 넣고
    result.append(" ".join(word_result))



print("\n".join(result))

import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

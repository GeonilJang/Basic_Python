"""
데이터를 영속성있게 저장할려면???

+ 메모리 내 데이터는 프로세스가 종료되면, 사라짐.
+ 영속석있게 저장할려면 파일에 저장해야합니다.
  -> 파이썬에서는 open 함수를 통해 파일 일기/쓰기 지원


#파일 모드(Read, Write, Append)
+ 모드R : 기존파일 읽기
+ 모드W or A : 새 파일 생성해서 쓰기
+ 모드W : 기존 파일 내용제거하고, 처음부터 쓰기
+ 모드A : 기존 파일에 추가하기


파일의 종류
Text : 문자열 데이터
    + 자동 인코딩/디코딩이 있으면, 더편리하겠죠?
BINARY : 바이너리 데이터
    + 자동 인코딩/디코딩을 구지 수행하지 않겠습니다.
    + 대개 문자열이 아닌, 이미지/PDF/XLS 포맷 등
    + text 데이터여도 BINARY로 열수도 있겠죠
"""



"""
open(파일 쓰기 / 일기 함수)
file_obj = open(파일경로, mode='rt or rb ...', encoding=None, 그 외 옵션 생략).read()
readed_data = file_obj.read()
file_obj.close()
    +
     file object 주용 멤버함수
     .write : 쓰기
     .read  : 일기
     .close : 파일 닫기
"""

# file_obj = open("README.md", "rt", encoding="utf8").read()
# print(file_obj)
# file_obj = open("README.md", "at", encoding="utf8").write("Geonil's been stuying for 4 hours a day")
# file_obj = open("README.md", "rt", encoding="utf8").read()










"""
더좋은 코드는 아래같이 써주세요

with open("README.md", "rt", encoding="utf8") as f:
    for line in f:
        print(line.rstrip())

"""
with open("README.md", "rt", encoding="utf8") as f:
    for line in f:
        print(line.rstrip())

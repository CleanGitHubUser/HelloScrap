# -*- coding: UTF-8  -*-

import requests
from bs4 import BeautifulSoup
import codecs

# 다음 영화 순위 스크리핑 예제

movie_rank = []         # 순위
movie_title = []        # 제목
movie_grade = []        # 평점
movie_opdate = []       # 개봉일

URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'
source_code = requests.get(URL)
plain_text = source_code.text

soup = BeautifulSoup(plain_text, 'html.parser')   # html 파서
# soup = BeautifulSoup(plain_text, 'lxml')            # xml 파서
# print(soup)

# 순위 추출
for i in range(1, 21):
    findkey = 'span["class=ico_ranking ico_top' + str(i) + '"]'
    for rank in soup.select(findkey):
        # print(" ".join(rank.text.strip().split()))
        movie_rank.append(" ".join(rank.text.strip().split()))

# 제목 추출
findkey = "a['class=link_g']"
for title in soup.select(findkey):
    # print(title.text.strip())
    movie_title.append(title.text.strip())

# 평점 추출
findkey = "em['class=emph_grade']"
for grade in soup.select(findkey):
    # print(grade.text.strip() + "/10")
    movie_grade.append(grade.text.strip() + "/10")

# 개봉일 추출
findkey = "dl['class=list_state']"
for opdate in soup.select(findkey):
    # print(opdate.select('dd')[0].text.strip())
    movie_opdate.append(opdate.select('dd')[0].text.strip())

# 모든 내용 출력
for i in range(0, len(movie_rank)):
    print(movie_rank[i])
    print(movie_title[i])
    print(movie_grade[i])
    print("%s\n" % (movie_opdate[i]))

# ----파일 저장하기
fmt = '%s, %s, %s, %s \n'   # 출력형식 정의
f = open('movie_rank2.txt', 'w')            # 파일을 쓰기모드로 open
# f.write('hello,python!!\n')         # 파일에 내용쓰기
# f.write('안녕하세요, 파이썬!!\n')
for i in range(0, 20):
    rank = fmt % (movie_rank[i], movie_title[i], \
                  movie_grade[i], movie_opdate[i])
    # f.write(rank)
    # 유니코드 문자 저장시 오류 발생!! - codecs 추천!
    # 파이썬2는 기본적으로 모든 문자를 ascii로 처리
    # 파일에 기록시 먼저 ascii로 디코딩하기 때문에 오류발생

f.close()                           # 파일 작업 종료 (필수!)

f = codecs.open('movie_rank2a.txt', 'w', 'utf-8')
for i in range(0, 20):
    rank = fmt % (movie_rank[i], movie_title[i], \
                  movie_grade[i], movie_opdate[i])
    f.write(rank)
f.close()

# ---- 파일 저장하기 (파이썬3)
try:
    f = codecs.open('movie_rank3.txt', 'w', 'utf-8')
    for i in range(0, 20):
        rank = fmt % (movie_rank[i], movie_title[i], \
                      movie_grade[i], movie_opdate[i])
        f.write(rank)
    f.close()
except Exception as ex:
    print(ex)

# ---- 파일 읽어 출력하기 (파이썬2)
# readline  : 한줄씩 읽어옴 (추가적으로 while 필요)
# readlinse : 모든 줄을 리스트로 읽어옴 (추가적으로 for 필요)
# read      : 파일 내용 전체 읽어옴 - 바이너리 파일 처리시 사용

f = codecs.open('movie_rank2a.txt', 'r', 'utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt', 'r', 'utf-8')
lines = f.readlines()
# print(lines)
for line in lines:
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt', 'r', 'utf-8')
data = f.read()
print(data)
f.close()

# ---- 파일 읽어 출력하기 (파이썬3)
f = open('movie_rank2a.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close

f = open('movie_rank2a.txt', 'r', encoding='utf-8')
line = f.readlines()
for line in lines:
    print(line)
f.close

f = open('movie_rank2a.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close

# with ~ as 구문으로 파일 다루기
# 파일 작업시 파일을 열고 닫는 것은 번거로운 일임
# 파이썬이 알아서 닫아주면 어떨까? - 편리함
with codecs.open('movie_rank2a.txt', 'r', 'utf-8') as f:
    data = f.read()
    print(data)

# 파일 읽기/쓰기 모드
# r : read (읽기), w : write(쓰기)
# t : text (텍스트파일), b : binary (바이너리파일 : 이미지)
# a : append (추가), + : update (수정)
# 파일모드의 기본값은 : rt


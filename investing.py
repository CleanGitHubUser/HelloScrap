# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# selenium 설치
# firefox용 webdriver 다운로드

URL = 'https://kr.investing.com/currencies/'

# firefox를 띄워 브라우저에 나타난 소스를 스크래핑 함
driver = webdriver.Firefox(
    executable_path=
    r'C:\Program Files\Mozilla Firefox/geckodriver.exe')
# 웹브라우저를 자동화할 수 있도록 특수하게 컴파일된
# 브라우저인  geckodriver.exe을 다운로드 후 지정한 위치에 저장
# github.com/mozilla/geckodriver
driver.get(URL)

# source_code = requests.get(URL)
source_code = driver.page_source
    # firefox로 가져온 소스를 source_code 변수에 저장
# print(source_code)

soup = BeautifulSoup(source_code, 'html.parser')   # html 파서
# soup = BeautifulSoup(plain_text, 'lxml')            # xml 파서
# print(soup)

# 종목 추출
findkey = 'section["id=leftColumn"]'
tables = []
for table in soup.select(findkey):
    tables.append(table)
# tables = table.split(',')
# for tb in table: print(tb)
# print(table[0])
# table = []
# for tb in tables:
#     table.append(tb)

findkey = 'span["class=alertBellGrayPlus js-plus-icon genToolTip oneliner"]'
subjects = []
# for subject in tables
#     subjects.append(table[0].select(findkey))
# for sb in subject: print(sb)
print(subject[0])

pair = []
# for su in subject:
#     print(su)
    # pr = su.get('data-id')
    # pair.append(pr)
    # print(pr)

# for i in range(0, len(subject)):
    # print(subject[i].get("id").text.strip())

    # for rank in soup.select(findkey):
        # print(" ".join(rank.text.strip().split()))
        # movie_rank.append(" ".join(rank.text.strip().split()))

    # 제목 추출
    # findkey = "a['class=link_txt #top #ranking #title @'" \
    #           + str(i) + "]"
    # for title in soup.select(findkey):
        # print(title.text.strip())
        # movie_title.append(title.text.strip())

# currid = [1, 2, 3, 125, 5, 6, 7, 8, 650, 159]       # 종목 번호
#
# # 종목 추출
# findkey = 'td["class=left noWrap"]'
# for title in soup.select(findkey):
#     print(title.text.strip().split())
#
# # 현재가 추출
# for i in range(0, len(currid)):
#     findkey = 'td[class=pid-"' + str(currid[i])'"-last"]'
#     for title in soup.select(findkey):
#         print(title.text.strip().split())
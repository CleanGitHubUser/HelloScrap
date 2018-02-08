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

# id 추출
findkey = 'section["id=leftColumn"]'
table = soup.select(findkey)
ts = BeautifulSoup(str(table[0]), 'html.parser')
findkey = 'span["class=alertBellGrayPlus js-plus-icon genToolTip oneliner"]'
subject = ts.select(findkey)
currid = []
for sb in subject:
    currid.append(sb.get('data-id'))
    # print(id)

# currid = [1, 2, 3, 125, 5, 6, 7, 8, 650, 159]       # 종목 번호

# 종목 추출
currs = []
findkey = 'td["class=left noWrap"]'
for curr in soup.select(findkey):
    # print(curr.text.strip().encode('utf-8'))
    currs.append(curr.text.strip().encode('utf-8'))

# 현재가 추출
values = []
for i in range(0, len(currid)):
    findkey = 'td["class=pid-' + str(currid[i]) + '-last"]'
    for value in soup.select(findkey):
        # print(value.text.strip().encode('utf-8'))
        values.append(value.text.strip().encode('utf-8'))

for i in range(0, len(currs)):
    print('%s, %s' %( currs[i], values[i] ))
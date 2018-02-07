# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# selenium 설치
# firefox용 webdriver 다운로드

URL = 'http://movie.daum.net/main/new#slide-1-1'

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
print(source_code)

soup = BeautifulSoup(source_code, 'html.parser')   # html 파서
# soup = BeautifulSoup(plain_text, 'lxml')            # xml 파서
# print(soup)

# 순위 추출
for i in range(1, 21):
    findkey = 'em["class=num_rank rank_' + str(i).zfill(2) + '"]'
    for rank in soup.select(findkey):
        print(" ".join(rank.text.strip().split()))
        # movie_rank.append(" ".join(rank.text.strip().split()))

    # 제목 추출
    findkey = "a['class=link_txt #top #ranking #title @'" \
              + str(i) + "]"
    for title in soup.select(findkey):
        print(title.text.strip())
        # movie_title.append(title.text.strip())
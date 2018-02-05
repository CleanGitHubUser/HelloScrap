#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 다음 JTBC 뉴스 스크래핑 예제
# media.daum.net/cp/310
# ?page=2&regDate=20170501&cateId=1002

press = [310]       # 언론사
date = [20180205]   # 년월일
page = [1, 2, 3]            # 페이지

new_title = []      # 뉴스 제목
new_desc = []       # 뉴스 간략 소개

# 스크래핑할 URL 지정
URL = 'http://media.daum.net/cp/' + str(press[0]) + \
    '?page=' + str(page[0]) + '&regDate=' + str(date[0])

# 스크래핑해서 소스를 source_code 에 저장
source_code = requests.get( URL )

# 중간 결과 출력
# print( source_code.text )

# 텍스트 추출을 위해 lxml로 태그 분석 (메모리 적재)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')

# 기사 제목 추출
cnt = 1
new_title = []
for title in soup.select("a['class=link_txt']"):
    if cnt > 15: break
    # print(title.text)
    # print(title.text.strip())
    new_title.append(title)
    cnt += 1

# 기사 간단 소개 추출
cnt = 1
new_desc = []
for summary in soup.select("span['class=link_txt']"):
    if cnt > 15: break
    # print(title.text)
    # print(title.text.strip())
    new_desc.append(summary)
    cnt += 1

article_list = []
for i in range(0, len(new_title)):
    link = soup.select("a['class=link_txt']")
    sc = requests.get(link[i].get("href"))
    pt = sc.text
    sp = BeautifulSoup(pt, 'lxml')
    article = sp.select("div['id=harmonyContainer']")
    article_list.append(article[0])

for i in range(0, len(new_title)):
    print(new_title[i].text.strip() + '\n')
    # print(new_desc[i].text.strip())
    print(article_list[i].text.strip())
    print('\n')
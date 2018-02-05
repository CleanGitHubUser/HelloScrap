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

print( source_code.text )
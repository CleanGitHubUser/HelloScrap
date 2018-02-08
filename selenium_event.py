# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver

# 탐색할 URL 정의
URL = 'https://kr.investing.com/currencies/'

# 웹 브라우저 자동화를 위해 드라이버 초기화
driver = webdriver.Firefox(executable_path=
   'C:\Program Files\Mozilla Firefox/geckodriver.exe')

# 브라우저를 지정한 URL로 이동시킴
driver.get(URL)

# 웹 페이지 오른쪽 '암호화폐'탭의 xpath 정의
alink = driver.find_element_by_xpath('//*[@id="QBS_7"]/a')

# 마우스, 단축키 이벤트 처리를 위해 ActionChains 초기화
mouse = webdriver.ActionChains(driver)

# 해당 링크를 마우스 클릭으로 처리하기 위해 move_to_element 사용
# 즉, 마우스를 링크로 이동한 다음 클릭
mouse.move_to_element(alink).click().perform()

# 클릭 후 보이는 페이지 내용을 source_code에 저장
source_code = driver.page_source

# 웹 페이지 내용을 parsing 하기 위해 bs4 로 초기화
soup = BeautifulSoup(source_code, 'html.parser')

findkey = 'table["class=genTbl openTbl quotesSideBlockTbl collapsedTbl"]'
table = soup.select(findkey)

ts = BeautifulSoup(str(table[0]), 'html.parser')

findkey = 'tr'
ids = []
id = ts.select(findkey)
for i in id:
    # print(i.get('pair'))
    ids.append(i.get('pair'))

findkey = 'a'
coins = []
coin = ts.select(findkey)
for c in coin:
    # print(c.text)
    coins.append(c.text)

#
# btccode = ['-btc-usd', '-btc-krw', '-eth-usd']    # 종목
# btccurcode = ['94']     # 환율 코드
#
#
# # 암호화폐 종류 (data-gae="-btc-usd")
# findkey = 'a["data-gae' + str(btccode[i]) + '"]'
# for coin in soup.select(findkey):
#     print(coin.text.strip().encode('utf-8'))

prices = []
for id in ids:
    findkey = 'td["id=sb_last_' + id + '"]'
    price = ts.select(findkey)
    for p in price:
        prices.append(p.text)

#
# # 암호화폐 환율 (id="sb_last_945629")
# findkey = 'td["id=sb_last_' + str(btccurcode[i]) + '"]'
# for rate in soup.select(findkey):
#     print(rate.text.strip().encode('utf-8'))

for i in range(0, len(coins)):
    print('%s, %s' %( coins[i], prices[i] ))

# 테스트를 위해 띄운 브라우저 닫기
driver.close()
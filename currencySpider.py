#-*- coding:utf-8 -*-
import scrapy
import codecs

import sys
# 리눅스상에서 파이썬2를 이용해서 utf-8로
# 파일에 내용을 기록하려면
# 시스템 기본 인코딩을 utf-8로 설정해야 함
reload(sys)
sys.setdefaultencoding('utf-8')

# scrapy에서 spider는 크롤링/스크래핑을 담당하는 핵심부분
# 크롤링/스크래핑 절차에 대한 정의를 하는 부분
class CurrencySpider(scrapy.Spider):
    name = 'currencySpider'        # 스파이더 프로그램의 이름 정의
    start_urls = ['http://finance.naver.com/marketindex/']

    def parse(self, response):

        cm = response.css( 'span.blind::text').extract()

        value = response.css( 'span.value::text').extract()

        with codecs.open('currencyValue.csv', 'w', 'utf-8') as f:

            currency = []
            measure = []
            cm2 = []
            for i in range(0, len(cm)):
                cm2.append(cm[i])
                if cm[i].encode('utf-8') == '달러인덱스':
                    cm2.append('')

            for i in range(0, len(cm2)):
                if i % 3 == 0:
                    currency.append(cm2[i])
                elif i % 3 == 1:
                    measure.append(cm2[i])

            for i in range(0, len(currency)):
                c = currency[i].encode('utf-8')
                v = value[i].encode('utf-8')
                m = measure[i].encode('utf-8')
                print(c)
                print('%s %s' %( v, m ))
                print
                f.write('%s, %s, %s\n' % ( c, v, m ))

        f.close()
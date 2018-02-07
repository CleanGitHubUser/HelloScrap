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
class MovieSpider(scrapy.Spider):
    name = 'movieSpider'        # 스파이더 프로그램의 이름 정의
    start_urls = ['http://ticket2.movie.daum.net/Movie/MovieRankList.aspx']
        # 스파이더가 스크래핑할 위치를 URL로 정의

    def parse(self, response):
        # start_urls에 정의된 URL을 스파이더가 스크래핑하고
        # 내용이 다운로드된 후 호출되는 메서드
        # parse()는 실제 추출할 데이터를 작업한 후
        # 결과로 return 하는 역할 담당

        ranks = response.css( 'span.ico_ranking::text').extract()
        # css 선택자를 이용해서 클래스가 ico_ranking인
        # 모든 항목을 추출해서 rank 변수에 저장

        titles = response.css('a.link_g::text').extract()
        # css 선택자를 이용해서 클래스가 link_g인
        # 모든 항목을 추출해서 title 변수에 저장

        with codecs.open('movierank.csv', 'w', 'utf-8') as f:
            # 처리 결과를 파일에 저장하기 위해
            # movierank.csv 라는 이름으로 쓰기 모드로 open

            for i in range(0, len(ranks)):
                # rank = ranks[i].replace('\r\n', ' ')
                # rank = ranks[i].strip()
                # title = titles[i].replace('\r\n', ' ')
                # title = titles[i].strip()
                    # \r\n -> whitespace
                # rank = ' '.join(rank.split())
                rank = ' '.join(ranks[i].strip().split())
                title = titles[i].strip().encode('utf-8')
                print(rank)
                print(title)
                    # utf_8로 변환후 출력
                f.write('%s, %s\n' % (rank, title))
                    # 순위와 제목을 파일에 기록
        f.close()
# -*-coding:utf8-*-

import sys
import os
import re
import json
import requests
import bs4
from bs4 import BeautifulSoup as bs
import feedparser
import datetime

news_out = []


def link_craw(rss_link):

    news_link = []
    for category in rss_link:
        links = feedparser.parse(category)
        for link in links.entries:
            news_link.append(link.link)

    return news_link


def crawl_news_data(url, tag):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    try:
        html = requests.get(url, headers=headers)
    except requests.exceptions.SSLError as e:
        sys.stderr.write('%s -> %s\n' % (usr, e))
        return []
    
    
    html = html.text
    data = bs(html, 'html.parser')
    
    # title
    title = data.select(tag.get("title"))
    title = title[0].getText().strip()
    
    # category
    source = data.select(tag.get("category"))
    if source != "":
        source = source[0].getText().strip()
    else:
        source = "etc"
    
    # abstract
    summary = data.select(tag.get("summary"))

    if summary != []:
        summary = summary[0].getText().strip()
        summary = summary.strip()
        # summary = re.sub(r'\t\t*','\t', summary)
        # summary = re.sub(r'  *',' ', summary)
        # summary = re.sub(r'\n','\\n', summary)

    else:
        summary = ""
    
    # contents
    txt = data.select(tag.get("contents"))
    text = list()
    for t in txt:
        t = [d for d in t if type(d) == bs4.element.NavigableString]
        text += t
    txt = '\\n'.join(text).strip()

    result = {'title': title, 'category': source,
              'url': url, 'summary': summary, 'contents': txt}

    return result


def write_json(name, news_result):

    dt_now = datetime.datetime.now()
    date = str(dt_now.date()).replace("-", "_")
    with open('/home/sia0940/crawling_daily/result/'+name+"/"+name+"_"+date+".json", 'w') as f:
        json.dump(news_result, f, ensure_ascii=False, indent=4)
    print(name+' DONE!', flush=True)


def get_news(rss_link, tag):
    news_links = []
    news_result = []
    news_links = link_craw(rss_link)
    print(len(news_links))
    try:
        for news_url in news_links:
            try:
                news_result.append(crawl_news_data(news_url, tag))
            except:
                continue
    except:
        print("ERROR occured! : " + news_url)

    write_json(tag.get("news_name"), news_result)


# news
def newsis():
    rss_link = [
        "https://newsis.com/RSS/sokbo.xml",
        "https://newsis.com/RSS/international.xml",
        "https://newsis.com/RSS/bank.xml",
        "https://newsis.com/RSS/society.xml",
        "https://newsis.com/RSS/met.xml",
        "https://newsis.com/RSS/sports.xml",
        "https://newsis.com/RSS/culture.xml",
        "https://newsis.com/RSS/photo.xml",
        "https://newsis.com/RSS/politics.xml",
        "https://newsis.com/RSS/economy.xml",
        "https://newsis.com/RSS/industry.xml",
        "https://newsis.com/RSS/health.xml",
        "https://newsis.com/RSS/country.xml",
        "https://newsis.com/RSS/entertain.xml",
        "https://newsis.com/RSS/square.xml",
        "https://newsis.com/RSS/newsiseyes.xml"
    ]
    tag = {
        "news_name": "newsis",
        "title": "#content > div.articleView > div.view > div.top > p",
        "category": "#container > div.subMenu > div > p > a",
        "summary": "#content > div.articleView > div.view > div.viewer > article > div.summury_view > p:nth-child(2)",
        "contents": "#content > div.articleView > div.view > div.viewer > article"
    }

    get_news(rss_link, tag)


def nocut_news():
    rss_link = [
        "https://rss.nocutnews.co.kr/category/politics.xml",  # 정치
        "https://rss.nocutnews.co.kr/category/economy.xml",  # 경제
        "https://rss.nocutnews.co.kr/category/society.xml",  # 사회
        "https://rss.nocutnews.co.kr/category/culture.xml",  # 문화
        "https://rss.nocutnews.co.kr/category/world.xml",  # 세계
        "https://rss.nocutnews.co.kr/category/it.xml",  # IT/과학
        "https://rss.nocutnews.co.kr/category/entertainment.xml",  # 연예
        "https://rss.nocutnews.co.kr/category/sports.xml",  # 스포츠
        "https://rss.nocutnews.co.kr/category/area.xml",  # 전국
        "https://rss.nocutnews.co.kr/category/opinion.xml",  # 오피니언
    ]
    tag = {
        "news_name": "nocut_news",
        "title": "#pnlViewTop > div.h_info > h2",
        "category": "#divSubCategory > p > strong",
        "summary": "#pnlViewBox > div.summary_l > div > p",
        "contents": "#pnlContent"
    }
    get_news(rss_link, tag)


def boan_news():
    rss_link = [
        "http://www.boannews.com/media/news_rss.xml?kind=1",  # 사건ㆍ사고
        "http://www.boannews.com/media/news_rss.xml?kind=2",  # 공공ㆍ정책
        "http://www.boannews.com/media/news_rss.xml?kind=3",  # 비즈니스
        "http://www.boannews.com/media/news_rss.xml?kind=4",  # 국제
        "http://www.boannews.com/media/news_rss.xml?kind=5",  # 테크
        "http://www.boannews.com/media/news_rss.xml?kind=6"  # 오피니언
    ]
    tag = {
        "news_name": "boan_news",
        "title": "#news_title02 > h1",
        "category": "#news_tag_txt > a > span",
        "summary": "#news_content > mark",
        "contents": "#news_content"
    }
    get_news(rss_link, tag)


def khan():
    rss_link = [
        "https://www.khan.co.kr/rss/rssdata/total_news.xml",
        "https://www.khan.co.kr/rss/rssdata/politic_news.xml",
        "https://www.khan.co.kr/rss/rssdata/economy_news.xml",
        "https://www.khan.co.kr/rss/rssdata/society_news.xml",
        "https://www.khan.co.kr/rss/rssdata/kh_world.xml",
        "http://www.khan.co.kr/rss/rssdata/kh_sports.xml",
        "https://www.khan.co.kr/rss/rssdata/culture_news.xml",
        "https://www.khan.co.kr/rss/rssdata/kh_entertainment.xml",
        "http://www.khan.co.kr/rss/rssdata/it_news.xml",
        "https://www.khan.co.kr/rss/rssdata/local_news.xml",
        "https://www.khan.co.kr/rss/rssdata/people_news.xml",
        "https://www.khan.co.kr/rss/rssdata/opinion_news.xml"
    ]
    tag = {
        "news_name": "khan",
        "title": "#top_title > p",
        "category": "#topBarWrap > div.fx_topbar > ul > li > a",
        "summary": "#articleBody > div.art_subtit > p",
        "contents": "#articleBody > p"
        # "contents" : "#articleBody > div.art_subtit"
    }
    get_news(rss_link, tag)


def herald():
    rss_link = [
        "http://biz.heraldcorp.com/common/rss_xml.php?ct=0",
        "http://biz.heraldcorp.com/common/rss_xml.php?ct=1",
        "http://biz.heraldcorp.com/common/rss_xml.php?ct=2",
        "http://biz.heraldcorp.com/common/rss_xml.php?ct=3",
        "http://biz.heraldcorp.com/common/rss_xml.php?ct=4",
        "http://biz.heraldcorp.com/common/rss_xml.php?ct=5",
        "http://biz.heraldcorp.com/common/rss_xml.php?ct=6"
    ]
    tag = {
        "news_name": "herald",
        "title": "body > div.wrap > div.view_bg > div.view_area > div.article_wrap > div.article_top > ul > li.article_title.ellipsis2",
        "category": "body > div.wrap > div.view_bg > div.view_area > div.article_wrap > div.article_top > ul > li.article_category",
        "summary": "#articleText > div.summary_area",
        "contents": "#articleText > p",
        "re_contents": "#articleText"
    }
    get_news(rss_link, tag)


def main():
    try:
        newsis()
        boan_news()
        nocut_news()
        khan()
        herald()
        print("ALL PROCESS COMPLETE")
    except:
        print("MAIN ERROR")


if __name__ == '__main__':
    main()

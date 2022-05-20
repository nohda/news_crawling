#-*-coding:utf8-*-

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import re
import json
import requests
import bs4
from bs4 import BeautifulSoup as bs

## for crawling twitter with img

def crawl_nc(index):

    url = 'https://www.nocutnews.co.kr/news/{}'.format(index)
    try:
        html = requests.get(url)
    except requests.exceptions.SSLError as e:
        sys.stderr.write('%s -> %s\n'%(usr,e))
        return []
            
    html = html.text
   # with open('{}.html'.format(index), 'w') as f:
   #     f.write(html)

    data = bs(html, 'html.parser')

    
    ## title
    title = data.select('#pnlViewTop > div.h_info > h2')
    title = title[0].getText().strip()

    ## headword_info
    #source = data.findAll('div', class_='headword_info')[0]
    source = data.select('#divSubCategory > p > strong')
    source = source[0].getText().strip()

    ## abstract
    summary = data.select('#pnlViewBox > div.summary_l > div > p')
    #summary = data.findAll('dl', class_='summary_area')
    if summary != []:
        summary = summary[0].getText().strip()
        summary = re.sub(r'\t\t*','\t', summary)
        summary = re.sub(r'  *',' ', summary)
        summary = re.sub(r'\n','\\n', summary)
    #print(summary
    else: summary = ""

    ## contents
    txt = data.select('#pnlContent')
    text = list()
    for t in txt:
        t = [d for d in t if type(d) == bs4.element.NavigableString]
        text += t
    txt = '\\n'.join(text).strip()

    result = {'title':title, 'category':source, 'url':url, 'summary':summary, 'contents':txt}
    with open('./result/{}.json'.format(index),'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

def crawl_ba(index):

    url = 'https://www.boannews.com/media/view.asp?idx={}'.format(index)
    try:
        html = requests.get(url)
    except requests.exceptions.SSLError as e:
        sys.stderr.write('%s -> %s\n'%(usr,e))
        return []
            
    html = html.text
    data = bs(html, 'html.parser')

    ## title
    title = data.select('#news_title02 > h1')
    title = title[0].getText().strip()

    ## headword_info
    #source = data.findAll('div', class_='headword_info')[0]
    source = data.select('#news_tag_txt > a > span')
    source = source[0].getText().strip()

    ## abstract
    summary = data.select('#news_content > mark')
    #summary = data.findAll('dl', class_='summary_area')
    if summary != []:
        summary = summary[0].getText().strip()
        summary = re.sub(r'\t\t*','\t', summary)
        summary = re.sub(r'  *',' ', summary)
        summary = re.sub(r'\n','\\n', summary)
    #print(summary
    else: summary = ""

    ## contents
    txt = data.select('#news_content')
    text = list()
    for t in txt:
        t = [d for d in t if type(d) == bs4.element.NavigableString]
        text += t
    txt = '\\n'.join(text).strip()

    result = {'title':title, 'category':source, 'url':url, 'summary':summary, 'contents':txt}
    with open('./result_ba/{}.json'.format(index),'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

if __name__=='__main__':
	
    #index = 5610350
    index = 101228
    count = 0
   
    while(1):
        try:
           # crawl(index-count)
           crawl_ba(index-count)
           count += 1 
           print('Success : https://www.boannews.com/media/view.asp?idx='+str(index-count))
          #exit()
        except:
           #print('ERROR : https://www.nocutnews.co.kr/news/'+str(index-count))
           print('ERROR : https://www.boannews.com/media/view.asp?idx='+str(index-count))
           #count += 1
           #exit()
           count += 1

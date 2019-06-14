
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from datetime import datetime 
import pandas as pd 
import time 
import re
import math
driver = webdriver.Chrome('chromedriver')



df = pd.read_csv('0614greencar.csv', encoding='utf-8-sig')


link = df['link']


news={'link':[], 'content':[]} #한국경제 #아시아경제 #문화일보 #아주경제 불가
for site in link:
    text=''
    driver.get(site)
    time.sleep(3)
    if 'chosun' in site: #조선일보
        for num in range(3,9,2):
            text += driver.find_element_by_css_selector(f'#news_body_id > div:nth-child({num})').text
            text += '\n\n'
    elif 'www.mk' in site: #매일경제
        text += driver.find_element_by_css_selector('#article_body > div').text
    elif 'fnnews' in site: #파이낸셜뉴스
        text += driver.find_element_by_css_selector('#article_content').text
    #elif 'hankookilbo' in site: #한국일보
        #text += driver.find_element_by_css_selector('#article_story').text
    elif 'heraldcorp' in site: #헤럴드
        text += driver.find_element_by_css_selector('#articleText').text
    elif 'news.mt' in site: #머니투데이
        text += driver.find_element_by_css_selector('#textBody').text
    elif 'sedaily' in site: #서울경제
        text += driver.find_element_by_css_selector('#v-left-scroll-in > div.view_con').text
    elif 'naeil' in site: #내일신문
        text += driver.find_element_by_css_selector('#contents').text
    elif 'biz.khan' in site: #경향비즈
        text += driver.find_element_by_css_selector('#articleBody').text
    elif 'segye' in site: #세계일보
        text += driver.find_element_by_css_selector('#article_txt').text
    elif 'seoul.co.kr' in site: #서울신문
        text += driver.find_element_by_css_selector('#atic_txt1').text
    elif 'hani' in site: #한겨레
        text += driver.find_element_by_css_selector('#a-left-scroll-in > div.article-text > div > div.text').text
    elif 'joins' in site: #중앙일보
        text += driver.find_element_by_css_selector('#article_body').text
    elif 'kmib' in site: #국민일보
        text += driver.find_element_by_css_selector('#articleBody').text
    elif 'bizn.donga' in site: #동아일보
        text += driver.find_element_by_css_selector('#ct').text
    elif 'news.donga' in site:
        text += driver.find_element_by_css_selector('#contents > div.article_view > div.article_txt').text
    else:
        pass
    news['link'].append(site)
    news['content'].append(text)
df = pd.DataFrame.from_dict(news)
df.columns = ['link', 'content']
df.to_csv('article_그린카.csv', index=False, encoding='utf-8-sig')


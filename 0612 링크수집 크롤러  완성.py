
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from datetime import datetime 
import pandas as pd 
import time 
import re
import math
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver')


# In[15]:


lst=['그린카'] 
chk = True
for query in lst:
    driver.get('https://www.bigkinds.or.kr/')
    time.sleep(3)
    #10년 설정
    driver.find_element_by_css_selector('#news-search-form > div > div > div > div.main-search-filters.text-left.mt-2 > div:nth-child(2) > button').click()
    time.sleep(0.5)
    for i in range(10):
        driver.find_element_by_css_selector('#search-begin-date').send_keys(Keys.BACK_SPACE)
    time.sleep(0.2)
    driver.find_element_by_css_selector('#search-begin-date').send_keys('2009-01-01')
    driver.find_element_by_css_selector('#news-search-form > div > div > div > div.main-search-filters.text-left.mt-2 > div.dropdown.main-search-filters__item.open > div').click()
    driver.find_element_by_css_selector('#news-search-form > div > div > div > div.main-search-filters.text-left.mt-2 > div.dropdown.main-search-filters__item.open > div > div.action-wrap > button.btn.btn-sm.btn-primary.close-filter-btn').click()
    # 언론사 열기
    time.sleep(0.5)
    driver.find_element_by_css_selector('#provider-filter-btn').click()
    driver.find_element_by_css_selector('#providers-wrap > div:nth-child(3) > div:nth-child(1) > div > label').click()
    driver.find_element_by_css_selector('#providers-wrap > div:nth-child(4) > div:nth-child(1) > div > label').click()
    driver.find_element_by_css_selector('#news-search-form > div > div > div > div.main-search-filters.text-left.mt-2 > div.dropdown.main-search-filters__item.none-relative.open > div > div.action-wrap > button.btn.btn-sm.btn-primary.half.close-filter-btn').click()
    # 쿼리 검색
    time.sleep(0.3)
    driver.find_element_by_css_selector('#total-search-key').send_keys(query)
    driver.find_element_by_css_selector('#news-search-form > div > div > div > div.input-group.main-search__form > span > button').click()
    # 100개씩 보기로 변경
    driver.find_element_by_css_selector('#collapse-step-2 > div > div > div.col-sm-9.col-lg-10 > div:nth-child(3) > div > div.col-xs-12.col-lg-4.col-sm-7.text-right > div:nth-child(2) > select > option:nth-child(4)').click()
    # 화면 로드 타임 슬립
    time.sleep(12)
    # (전체 검색 결과 / 100) -1 #페이지 넘기는 수
    page = math.ceil(int(re.sub(',','',(driver.find_element_by_css_selector('#total-news-cnt').text)))/100)
    if page < 1 :
        page =1
    #빈 딕셔너리 생성
    Article={'title':[], 'date':[], 'category':[], 'link':[], 'company':[], 'query':[]}
    # 페이지 수 만큼 while 문 반복
    while page:
        page -= 1
        #페이지 로드 시간 지연
        if chk == True:
            chk = False
        else:
            time.sleep(20)
        # div tag 전체를 리스트로 저장
        div_tag=driver.find_elements_by_css_selector('#news-results > div')
        for article in div_tag:
            time.sleep(0.1)
            chk_title= article.find_element_by_css_selector('div.news-item__body > h4').text
            if query in chk_title:
                try:
                    Article['company'].append(article.find_element_by_css_selector('a').text)
                except:
                    Article['company'].append('')
                try:
                    Article['title'].append(article.find_element_by_css_selector('div.news-item__body > h4').text)
                except:
                    Article['title'].append('')
                try:
                    Article['category'].append(article.find_element_by_css_selector('div.news-item__body > div.news-item__meta > span.news-item__category').text)
                except:
                    Article['category'].append('')
                try:
                    Article['date'].append(article.find_element_by_css_selector('div.news-item__body > div.news-item__meta > span.news-item__date').text)
                except:
                    Article['date'].append('')
                try:
                    Article['link'].append(article.find_element_by_css_selector('div.news-item__body > div.news-item__meta > a').get_attribute("href"))
                except:
                    Article['link'].append('')
                try:
                    Article['query'].append(query)
                except:
                    Article['query'].append('')
        # next page
        try:
            next_button=driver.find_element_by_css_selector('#news-results-pagination > ul > li:nth-child(10) > a')
            next_button.click()
        except:
            pass
    Article=pd.DataFrame.from_dict(Article)
    Article.columns = ['title', 'date', 'category','link', 'company','query']
    Article.to_csv(f'{query}.csv', index=False, encoding='utf-8-sig')
    print(f'{query} 저장 완료')


# In[ ]:


df = pd.read_csv('이니스프리.csv', encoding='utf-8-sig', engine='python')


# In[7]:


driver.find_element_by_css_selector('div.news-item__body > div.news-item__meta > span.news-item__category').text


# In[10]:


len(Article['title'])


# In[11]:


len(Article['category'])


# In[13]:


driver.find_element_by_css_selector('div.news-item__body > h4').text


# In[19]:


len(Article['title'])


# In[22]:


len(Article['link'])


# In[25]:


len(Article['category'])


# In[26]:


len(Article['company'])


# In[30]:


for i in range(len(Article['category'])):
    if Article['category'][i] == '':
        print(i)


# In[55]:


titlelst1=Article['company'][0:321]


# In[56]:


titlelst2=Article['company'][322:]


# In[45]:


titlelst2


# In[58]:


len(titlelst1+titlelst2)


# In[57]:


newcom=titlelst1+titlelst2


# In[53]:


newtitle[320]


# In[59]:


Article['title'] = newtitle


# In[60]:


Article['company'] = newcom


# In[61]:


Article=pd.DataFrame.from_dict(Article)
Article.columns = ['title', 'date', 'category','link', 'company','query']
Article.to_csv(f'{query}.csv', index=False, encoding='utf-8-sig')


# In[72]:


Article.shape[0]


# In[82]:


df = df[df['link'] != 'http://www.hankookilbo.com/news/npath/?did=KP ']


# In[77]:


df2['company'].value_counts()


# In[83]:


df['company'].value_counts()


# In[85]:


df.to_csv('0614greencar.csv', index=False, encoding='utf-8-sig')


# In[87]:


df[df['link']=='http://www.fnnews.com/news/201604041126491210']


# In[88]:


df.shape


#!/usr/bin/env python
# coding: utf-8

# # 출산율, 실업률, 국민부담률 간 상관관계 데이터 분석

# In[ ]:


# 데이터 출처: https://kostat.go.kr
# 출산율 데이터(10년치) 불러오기


# In[278]:


import pandas as pd

People_OECD = pd.read_excel('C:\\Users\\shiny\\OneDrive\\바탕 화면\\프로젝트\\합계출산율_OECD__20230103141546.xlsx')
People_OECD


# In[279]:


# 출산율 데이터 살펴보기


# In[280]:


People_OECD.info()


# In[281]:


# 출산율 데이터 정리하기


# In[282]:


People_OECD.rename(columns={'2013':'2013년','2014':'2014년','2015':'2015년','2016':'2016년'
                           ,'2017':'2017년','2018':'2018년','2019':'2019년','2020':'2020년'
                            ,'2021':'2021년','2022':'2022년' }, inplace=True)
# 쓸데 없는 데이터 삭제 (리히텐슈타인은 실업률 정보가 누락되어 있어서 제외)
People_OECD.drop(index=[0,5,9,13,28,41], axis=0, inplace=True)
People_OECD


# In[287]:


# 출산율 평균 수치 추가 및 인덱스 설정
People_OECD['출산율 평균']=(People_OECD['2013년']+People_OECD['2014년']+People_OECD['2015년']+People_OECD['2016년']+People_OECD['2017년']+People_OECD['2018년']+People_OECD['2019년']+People_OECD['2020년']+People_OECD['2021년']+People_OECD['2022년'])/10
People_OECD.reset_index(drop=True, inplace=True)
People_OECD


# In[288]:


# 출산율 낮은 국가
People_OECD.sort_values(by='출산율 평균', ascending=True).head()


# In[289]:


# 출산율 높은 국가
People_OECD.sort_values(by='출산율 평균', ascending=False).head()


# In[290]:


# 실업률 데이터 가공하기
Unemploy_OECD=pd.read_excel('C:\\Users\\shiny\\OneDrive\\바탕 화면\\프로젝트\\실업률_OECD.xlsx')
Unemploy_OECD.drop(columns=['2013.1','2013.2','2014.1','2014.2','2015.1','2015.2','2016.1','2016.2','2017.1','2017.2'
                            ,'2018.1','2018.2','2019.1','2019.2','2020.1','2020.2','2021.1','2021.2']
                              , axis=1, inplace=True)
Unemploy_OECD.drop(index=[0,1,6,10,14,41], axis=0, inplace=True)
Unemploy_OECD=Unemploy_OECD.astype({'2013':'float64', '2014':'float64',
                                  '2015':'float64', '2016':'float64',
                                  '2017':'float64', '2018':'float64',
                                  '2019':'float64', '2020':'float64',
                                  '2021':'float64'})
Unemploy_OECD['실업률 평균']=(Unemploy_OECD['2013']+Unemploy_OECD['2014']+Unemploy_OECD['2015']+Unemploy_OECD['2016']+Unemploy_OECD['2017']+Unemploy_OECD['2018']+Unemploy_OECD['2019']+Unemploy_OECD['2020']+Unemploy_OECD['2021'])/9
Unemploy_OECD.reset_index(drop=True, inplace=True)
Unemploy_OECD


# In[292]:


# 국민부담률 데이터 가공하기
Burden_OECD=pd.read_excel('C:\\Users\\shiny\\OneDrive\\바탕 화면\\프로젝트\\국민부담률_OECD.xlsx')
Burden_OECD.drop(index=[0,5,9,13,40], axis=0, inplace=True)
Burden_OECD['국민부담률 평균']=(Burden_OECD['2013']+Burden_OECD['2014']+Burden_OECD['2015']+Burden_OECD['2016']+Burden_OECD['2017']+Burden_OECD['2018']+Burden_OECD['2019']+Burden_OECD['2020'])/8
Burden_OECD.reset_index(drop=True, inplace=True)
Burden_OECD


# In[295]:


# 출산율, 실업률, 국민부담률 데이터 합치기 및 데이터 정리

People_OECD['실업률 평균']=Unemploy_OECD['실업률 평균']
People_OECD['국민부담률 평균']=Burden_OECD['국민부담률 평균']
People_OECD.drop(columns=['2013년','2014년','2015년','2016년','2017년','2018년','2019년','2020년','2021년','2022년'], axis=1, inplace=True)
People_OECD


# In[ ]:


# 국가별로 인덱스 설정하기


# In[298]:


# 그래프로 보기

People_OECD.set_index('국가별', inplace=True)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import platform
path = "c:/windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else :
    print('Unknown system... sorry~~~')    


# In[299]:


# 출산율 그래프
People_OECD['출산율 평균'].sort_values().plot(kind='barh', grid=True, figsize=(10,15))
plt.xticks(np.arange(0, 3.5, 0.5), ('0.0명','0.5명','1.0명','1.5명','2.0명','2.5명','3.0명'))
plt.title('출산율 평균')
plt.show()


# In[301]:


# 실업률 그래프
People_OECD['실업률 평균'].sort_values().plot(kind='barh', grid=True, figsize=(10,15))
plt.xticks(np.arange(0, 22.5, 2.5), ('0.0%','2.5%','5.0%','7.5%','10.0%','12.5%','15.0%','17.5%','20.0%'))
plt.title('실업률 평균')
plt.show()


# In[303]:


# 국민부담률 그래프
People_OECD['국민부담률 평균'].sort_values().plot(kind='barh', grid=True, figsize=(10,15))
plt.xticks(np.arange(0, 50, 10), ('0%','10%','20%','30%','40%'))
plt.title('국민부담률 평균')
plt.show()


# In[324]:


# 출산율 낮은 국가
People_OECD.sort_values(by='출산율 평균', ascending=True).head(10)


# In[323]:


# 출산율 높은 국가
People_OECD.sort_values(by='출산율 평균', ascending=False).head(10)


# In[322]:


# 실업률 낮은 국가
People_OECD.sort_values(by='실업률 평균', ascending=True).head(10)


# In[321]:


# 실업률 높은 국가
People_OECD.sort_values(by='실업률 평균', ascending=False).head(10)


# In[318]:


# 국민부담률 낮은 국가
People_OECD.sort_values(by='국민부담률 평균', ascending=True).head(10)


# In[320]:


# 국민부담률 높은 국가
People_OECD.sort_values(by='국민부담률 평균', ascending=False).head(10)


# In[306]:


# 출산율, 실업률, 국민부담률 사이의 상관관계 그래프
sns.pairplot(People_OECD, vars=['출산율 평균','실업률 평균','국민부담률 평균'], kind='reg', height=3) 
plt.show()


# In[307]:


# 출산율, 실업률, 국민부담률 사이의 상관관계 수치화(절대값이 1에 가까울 수록 상관도가 높음)
df = People_OECD[['출산율 평균','실업률 평균','국민부담률 평균']]
df.head()
df.corr()


# In[308]:


# 수치화 한 것을 시각화하기(양의 상관관계는 녹색계열, 음의 상관관계는 보라색 계열)
plt.matshow(df.corr())


# # 결과 분석

# In[ ]:


이 프로젝트를 시작하기 전에 예상한 내용은 출산율이 낮은 이유 중에 실업률과 국민부담률이 높다는 것이었다. 
상관관계 수치를 분석한 결과, 출산율과 실업률은 음의 상관관계, 출산율과 국민부담률은 음의 상관관계를 갖는다는 것을 알게 되었다.
이는 예상한 바와 비슷하다고 말할 수 있지만 상관도 수치의 절댓값이 0.2 수준이므로 상관도가 높다고 볼 수 없다.
특히 대한민국의 경우, 출산율은 OECD 국가 중 최하위를 기록했지만 실업률과 국민부담률 또한 낮은 수치를 기록했으므로 프로젝트 시작 전
예상 내용과는 다르다는 것을 알 수 있다.


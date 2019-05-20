#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import numpy as np
import warnings; warnings.simplefilter('ignore')


# In[ ]:





# In[ ]:





# In[ ]:


## load data per year
Year_1978 = pd.read_csv('./gl1990-2018/GL1978.TXT',sep=',',header=None)
Year_1979 = pd.read_csv('./gl1990-2018/GL1979.TXT',sep=',',header=None)
Year_1980 = pd.read_csv('./gl1990-2018/GL1980.TXT',sep=',',header=None)
Year_1981 = pd.read_csv('./gl1990-2018/GL1981.TXT',sep=',',header=None)
Year_1982 = pd.read_csv('./gl1990-2018/GL1982.TXT',sep=',',header=None)
Year_1983 = pd.read_csv('./gl1990-2018/GL1983.TXT',sep=',',header=None)
Year_1984 = pd.read_csv('./gl1990-2018/GL1984.TXT',sep=',',header=None)
Year_1985 = pd.read_csv('./gl1990-2018/GL1985.TXT',sep=',',header=None)
Year_1986 = pd.read_csv('./gl1990-2018/GL1986.TXT',sep=',',header=None)
Year_1987 = pd.read_csv('./gl1990-2018/GL1987.TXT',sep=',',header=None)
Year_1988 = pd.read_csv('./gl1990-2018/GL1988.TXT',sep=',',header=None)
Year_1989 = pd.read_csv('./gl1990-2018/GL1989.TXT',sep=',',header=None)
Year_1990 = pd.read_csv('./gl1990-2018/GL1990.TXT',sep=',',header=None)
Year_1991 = pd.read_csv('./gl1990-2018/GL1991.TXT',sep=',',header=None)
Year_1992 = pd.read_csv('./gl1990-2018/GL1992.TXT',sep=',',header=None)
Year_1993 = pd.read_csv('./gl1990-2018/GL1993.TXT',sep=',',header=None)
Year_1994 = pd.read_csv('./gl1990-2018/GL1994.TXT',sep=',',header=None)
Year_1995 = pd.read_csv('./gl1990-2018/GL1995.TXT',sep=',',header=None)
Year_1996 = pd.read_csv('./gl1990-2018/GL1996.TXT',sep=',',header=None)
Year_1997 = pd.read_csv('./gl1990-2018/GL1997.TXT',sep=',',header=None)
Year_1998 = pd.read_csv('./gl1990-2018/GL1998.TXT',sep=',',header=None)
Year_1999 = pd.read_csv('./gl1990-2018/GL1999.TXT',sep=',',header=None)
Year_2000 = pd.read_csv('./gl1990-2018/GL2000.TXT',sep=',',header=None)
Year_2001 = pd.read_csv('./gl1990-2018/GL2001.TXT',sep=',',header=None)
Year_2002 = pd.read_csv('./gl1990-2018/GL2002.TXT',sep=',',header=None)
Year_2003 = pd.read_csv('./gl1990-2018/GL2003.TXT',sep=',',header=None)
Year_2004 = pd.read_csv('./gl1990-2018/GL2004.TXT',sep=',',header=None)
Year_2005 = pd.read_csv('./gl1990-2018/GL2005.TXT',sep=',',header=None)
Year_2006 = pd.read_csv('./gl1990-2018/GL2006.TXT',sep=',',header=None)
Year_2007 = pd.read_csv('./gl1990-2018/GL2007.TXT',sep=',',header=None)
Year_2008 = pd.read_csv('./gl1990-2018/GL2008.TXT',sep=',',header=None)
Year_2009 = pd.read_csv('./gl1990-2018/GL2009.TXT',sep=',',header=None)
Year_2010 = pd.read_csv('./gl1990-2018/GL2010.TXT',sep=',',header=None)
Year_2011 = pd.read_csv('./gl1990-2018/GL2011.TXT',sep=',',header=None)
Year_2012 = pd.read_csv('./gl1990-2018/GL2012.TXT',sep=',',header=None)
Year_2013 = pd.read_csv('./gl1990-2018/GL2013.TXT',sep=',',header=None)
Year_2014 = pd.read_csv('./gl1990-2018/GL2014.TXT',sep=',',header=None)
Year_2015 = pd.read_csv('./gl1990-2018/GL2015.TXT',sep=',',header=None)
Year_2016 = pd.read_csv('./gl1990-2018/GL2016.TXT',sep=',',header=None)
Year_2017 = pd.read_csv('./gl1990-2018/GL2017.TXT',sep=',',header=None)
Year_2018 = pd.read_csv('./gl1990-2018/GL2018.TXT',sep=',',header=None)


# In[ ]:


alldata = pd.concat([Year_1978, Year_1979, Year_1980, Year_1981, Year_1982, Year_1983, Year_1984, Year_1985, Year_1986, Year_1987, Year_1988, Year_1989, Year_1990, Year_1991, Year_1992, Year_1993, Year_1994, Year_1995, Year_1996, Year_1997, Year_1998, Year_1999, Year_2000, Year_2001, Year_2002, Year_2003, Year_2004, Year_2005, Year_2006, Year_2007, Year_2008, Year_2009, Year_2010, Year_2011, Year_2012, Year_2013, Year_2014, Year_2015, Year_2016, Year_2017, Year_2018])


# In[ ]:


alldata.shape


# In[ ]:


##Only keep Toronto home games
tordata = alldata[alldata[6] == 'TOR']
tordata.shape


# In[ ]:


tordata = tordata.reset_index(drop = True) ## Reset index. Old one is based on all the other teams
from dateutil.parser import parse
tordata[0]=pd.to_datetime(tordata[0],format='%Y%m%d')  ## convert to datetime
tordata.set_index(0, inplace = True) ## set datetime as index


# In[ ]:


###Extract relevant columns 

data = tordata[[1, 2, 3, 4, 12, 13, 17, 23,51, 9, 10]]
data.columns = ['GameType','DayOfWeek','VisitingTeam_Team','VisitingTeam_League','DayNight','Completion','Attendance','VisitingTeam_Hits','HomeTeam_Hits','VisitingScore','HomeScore']


# In[ ]:


## Create Winner column based PointDifferential
data['PointDifferential'] = data['HomeScore'] - data['VisitingScore']
data.loc[data['PointDifferential'] > 0, 'Winner'] = 'W'
data.loc[data['PointDifferential'] < 0, 'Winner'] = 'L'
data.head()
    


# In[ ]:


data = data.loc[data['GameType'] != 1] ## Exclude one game of double-header that has no attendance


# In[ ]:


## Assign a game number for each game of each season
gamesperyear = data.groupby(data.index.year)['GameType'].count().values ## Determine amount of games/year
data['GameNumber'] = ""
for i, year in enumerate(data.index.year.unique().values):
    data.loc[data.index.year == year, 'GameNumber'] = list(range(1,gamesperyear[i]+1))


# In[ ]:


## WinnerNumber column is useful for calculating WinLossRatio (next cell)
data['WinnerNumber'] = ""
data.loc[data['Winner'] == 'W', 'WinnerNumber'] = 1
data.loc[data['Winner'] == 'L', 'WinnerNumber'] = -1


# In[ ]:


## Create Winlossratio column which calculates win/loss for all prior games in a season
## Also creates WinLossRatioLast10 which is win/loss ratio for last 10 games

data['WinLossRatio'] = ''
data['WinLossRatioLast10'] = ''

for j, year in enumerate(data.index.year.unique().values):
    i = gamesperyear[j]
    ## Win/loss for all season
    data.loc[(data.index.year == year) & (data['GameNumber'] == 1),'WinLossRatio'] = 0
    data.loc[(data.index.year == year) & (data['GameNumber'].isin(list(range(2,i+1)))),'WinLossRatio'] = data.loc[data.index.year == year,'WinnerNumber'].cumsum()[:-1].values
    ## Win/loss for last 10 games
    data.loc[(data.index.year == year) & (data['GameNumber'] == 1),'WinLossRatioLast10'] = 0
    data.loc[(data.index.year == year) & (data['GameNumber'].isin(list(range(2,i+1)))),'WinLossRatioLast10'] = data.loc[data.index.year == year,'WinnerNumber'].rolling(min_periods=1, window=10).sum()[:-1].values


# In[ ]:


## Import weather data, set it to index
AllWheather_df = pd.read_csv('./Data/weatherstats_toronto_daily.csv',usecols = ['date','max_temperature','max_relative_humidity','max_wind_speed','avg_visibility','precipitation'])
AllWheather_df['date']=pd.to_datetime(AllWheather_df['date'], format='%y-%m-%d')
AllWheather_df.set_index('date', inplace = True)
AllWheather_df.head()


# In[ ]:


data = data.join(AllWheather_df,how='left')


# In[ ]:


data['year']=data.index.year
data['month']=data.index.month
data.head()


# In[ ]:


## Create Homeopener variable
data.loc[data['GameNumber'] == 1, 'HomeOpener'] = 1
data.loc[data['GameNumber'] != 1, 'HomeOpener'] = 0


# In[ ]:





# In[ ]:


tennis_df = pd.read_csv('./data/tournaments_1877-2017_unindexed.csv', encoding = "ISO-8859-1")


# In[ ]:


tennis_df[tennis_df['tourney_location'] == 'Toronto'].head()


# In[ ]:


soccer_df=pd.read_csv('./data/soccer.csv')


# In[ ]:


soccer_df.head()


# In[ ]:


soccer_df['Date'] = pd.to_datetime(soccer_df['Date'], format='%Y-%m-%d')
soccer_df.set_index('Date', inplace = True)


# In[ ]:


soccer_df = soccer_df[soccer_df['Home'] == 'Toronto']


# In[ ]:


soccer_df['Soccergame'] = 1
soccer_df = soccer_df.drop(['Game #','Home','HomeScore','Visitor','Attendance','VisitorScore'],axis=1)


# In[ ]:


data = data.join(soccer_df, how='left')


# In[ ]:


data['Soccergame'] = data['Soccergame'].fillna(0)


# In[ ]:





# In[ ]:





# In[ ]:


## Try precipitation as a binary variable, 0 = no rain, 1 = any rain
data.loc[data['precipitation']== 0,'PrecipitationBinary'] = 0 
data.loc[data['precipitation']!= 0,'PrecipitationBinary'] = 1 
data.groupby('PrecipitationBinary')['Attendance'].mean().plot.bar()


# In[ ]:


## Save predictor variables to csv
ShortTermPred_df = data[['DayOfWeek','VisitingTeam_Team','DayNight','Attendance','GameNumber','WinLossRatio','WinLossRatioLast10','max_temperature','precipitation','year','month','HomeOpener','Soccergame']]
ShortTermPred_df.to_csv('ShortTermPred.csv')


# In[ ]:





# In[ ]:





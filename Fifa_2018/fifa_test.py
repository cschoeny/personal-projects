# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:47:12 2018

@author: cscho
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

fifa = pd.read_csv('complete.csv')

#%% Basic exploration

## ALSO find top 5 players in each position, just for fun. Also top americans, also describe some stats age etc.
fifa.shape[0]
fifa.groupby('nationality')['ID'].count().size #num nationalities
fifa.groupby('club')['ID'].count().size #num clubs
fifa.groupby('league')['ID'].count().size #num leagues
print('Players:', '\t', fifa.shape[0], '\n',
      'Nationalities:', '\t', fifa.groupby('nationality')['ID'].count().size, '\n',
      'Clubs:', '\t\t', fifa.groupby('club')['ID'].count().size, '\n',
      'Leagues:', '\t', fifa.groupby('league')['ID'].count().size, sep='')

#Top-10 countries by raw number of players
fifa.groupby('nationality')['ID'].count().sort_values(ascending=False).head(10)
fifa.groupby('nationality')['ID'].count().sort_values(ascending=False).tail(30)


#Countries by number of players above an overall score of 80 (top 523 players in the world)
fifa[fifa.overall>=80].groupby('nationality')['ID'].count().sort_values(ascending=False).head(10)

#investigate difference between germany and england
#compare pdf of their respective overall rankings
sns.kdeplot(fifa[fifa.nationality=='Spain']['overall'], label='Spain', shade=True)
sns.kdeplot(fifa[fifa.nationality=='England']['overall'], label='England', shade=True)


#Do any countries specialize in world class players per position?
top_gk = fifa[fifa.Position=='GK'].head(50)
top_gk.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)

top_cb = fifa[fifa.Position=='Center-back'].head(50)
top_cb.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)

top_def = fifa[fifa.Position=='Outside-back'].head(50)
top_def.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)

top_cm = fifa[fifa.Position=='Center-mid'].head(50)
top_cm.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)

top_om = fifa[fifa.Position=='Outside-mid'].head(50)
top_om.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)

top_for = fifa[fifa.Position=='Forward'].head(50)
top_for.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)

#Who are the spain center mids that dominate?
top_cm[top_cm.nationality=='Spain'][['name', 'overall', 'club']]



#%% Look at heigh vs weight
#2D KDE plot
sns.jointplot(x='height_cm', y='weight_kg', data=fifa, kind="kde")

#Lets find the tallest and shortest countries and compare them
#First filter out to countries that have at least 50 players in the database.
fifa_sig = fifa.groupby('nationality')
fifa_sig = fifa_sig.filter(lambda x:x['nationality'].count()>=50)

#fifa_sig.groupby('nationality')['ID'].count().sort_values(ascending=False).tail(30)
#find tallest country on average
fifa_sig.groupby('nationality')['height_cm'].mean().sort_values(ascending=False).head(5)
fifa_sig.groupby('nationality')['height_cm'].mean().sort_values().head(5)

#now lets compare them
bosnia=fifa[fifa.nationality=='Bosnia Herzegovina']
saudi=fifa[fifa.nationality=='Saudi Arabia']
sns.kdeplot(bosnia.height_cm, bosnia.weight_kg, cmap='Reds')
sns.kdeplot(saudi.height_cm, saudi.weight_kg, cmap='Blues')

#%% Assign positions to players
fifa['Position']= np.nan

fifa.loc[fifa.prefers_lm == True, ['Position']] = 'Outside-mid'
fifa.loc[fifa.prefers_rm == True, ['Position']] = 'Outside-mid'
fifa.loc[fifa.prefers_lw == True, ['Position']] = 'Outside-mid'
fifa.loc[fifa.prefers_rw == True, ['Position']] = 'Outside-mid'
fifa.loc[fifa.prefers_cam == True, ['Position']] = 'Center-mid'
fifa.loc[fifa.prefers_cm == True, ['Position']] = 'Center-mid'
fifa.loc[fifa.prefers_cdm == True, ['Position']] = 'Center-mid'
fifa.loc[fifa.prefers_rb == True, ['Position']] = 'Outside-back'
fifa.loc[fifa.prefers_lb == True, ['Position']] = 'Outside-back'
fifa.loc[fifa.prefers_cb == True, ['Position']] = 'Center-back'
fifa.loc[fifa.prefers_st == True, ['Position']] = 'Forward'
fifa.loc[fifa.prefers_cf == True, ['Position']] = 'Forward'
fifa.loc[fifa.prefers_gk == True, ['Position']] = 'GK'

pos_order = ['GK', 'Center-back', 'Outside-back', 'Center-mid', 'Outside-mid', 'Forward']

#Get top leagues
leagues=['Spanish Primera División', 'English Premier League', 'Italian Serie A', 'German Bundesliga', 'French Ligue 1']

#Assign rank to a columns
fifa['Rank']=fifa.index+1
#%% Plot height & weight based on position
sns.boxplot(x='Position', y='height_cm', data=fifa, order=pos_order)
sns.violinplot(x='Position', y='height_cm', data=fifa, order=pos_order)

sns.boxplot(x='Position', y='weight_kg', data=fifa, order=pos_order)
sns.violinplot(x='Position', y='weight_kg', data=fifa, order=pos_order)

#calculate the correlation between height and weight per position, might display something
fifa.groupby('Position')[['height_cm', 'weight_kg']].corr()
#%% Looking at different leagues
fifa_sub = fifa.loc[fifa.league.isin(leagues)]
_ = sns.stripplot(x='league', y='overall', hue='Position', data=fifa_sub, dodge=0.6, jitter=True, alpha=.5, order=leagues, hue_order=pos_order)
loc, labels = plt.xticks()
_.set_xticklabels(labels, rotation=45)
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")

_=sns.boxplot(x='league', y='overall', hue='Position', data=fifa_sub, order=leagues, hue_order=pos_order)
loc, labels = plt.xticks()
_.set_xticklabels(labels, rotation=45)
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")

#how about we look at the ranks of the top 50 players in each league
fifa_sub_top = fifa_sub.groupby('league').head(50)
_ = sns.boxplot(x='league', y='Rank', data=fifa_sub_top, order=leagues)
_ = sns.stripplot(x='league', y='Rank', data=fifa_sub_top, order=leagues)
loc, labels = plt.xticks()
_.set_xticklabels(labels, rotation=45)

#lets try to make a stack plot
#the idea here is to measure the fraction of players ranked above a certain value, might be tough
#First lets get top 500 players
top=500
fifa_top = fifa.head(top)

#lets try some list comprehension
#league_strings = ['_%s' %x for x in leagues]

top_vec=[None]*(len(leagues))
for L in range(len(leagues)):
    top_vec[L] = [((fifa_top.Rank<=x+1) & (fifa_top.league==leagues[L])).sum() for x in range(top)]
#need to calculate the 'other' league
other = [None]*top
top_vec_numpy = np.array(top_vec)
for r in range(top):
    other[r] = r-np.sum(top_vec_numpy[:,r])+1

#now let's make the data frame
top_df = pd.DataFrame({leagues[0]:top_vec[0],
                     leagues[1]:top_vec[1],
                     leagues[2]:top_vec[2],
                     leagues[3]:top_vec[3],
                     leagues[4]:top_vec[4],
                     'Other Leagues':other}, index=range(1,501))

top_df_perc = top_df.divide(top_df.sum(axis=1), axis=0)
plt.stackplot(range(1,501), top_df_perc[leagues[0]], top_df_perc[leagues[1]],
              top_df_perc[leagues[2]], top_df_perc[leagues[3]],
              top_df_perc[leagues[4]], top_df_perc['Other Leagues'],
              labels=[*leagues, 'Other Leagues'])
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
plt.margins(0,0)
plt.title('Player Ranking Stacked Chart per League')
plt.xlabel('Player Ranking')

#lets get the final percentages
top_df_perc.iloc[-1]

#redo this for top 20, top 100, top 500, top 1000

#top 5 players not in the top 5 leagues?
fifa.loc[~fifa.league.isin(leagues)][['name', 'Rank', 'club', 'league', 'nationality', 'overall']].head(10)

#%% Let's compare English PK skill to German PK
#First let's look at penalities skils (first everyone then just forwards)
countries = ['England', 'Germany']
fifa_pen = fifa.loc[fifa.nationality.isin(countries)]
sns.violinplot(x='nationality', y='penalties',  data=fifa_pen, inner='quartile')
sns.violinplot(x='Position', y='penalties', hue='nationality', data=fifa_pen, split=True, inner='quartile', order=pos_order)

#Lets look at goalies
sns.violinplot(x='nationality', y='overall', data=fifa_pen[fifa_pen.Position=='GK'], inner='quartile')
#Let's check out the top-5 goalies per country
fifa_pen.loc[(fifa_pen['Position']=='GK') & (fifa_pen['nationality']=='Germany')][['name', 'club', 'overall']].head(7)
fifa_pen.loc[(fifa_pen['Position']=='GK') & (fifa_pen['nationality']=='England')][['name', 'club', 'overall']].head(7)


#%% Left footed stuff
#the variable is 'preferred_foot'

#lets see aveage rating of left vs. right
fifa.groupby('preferred_foot')['overall'].mean()
#use boot-strapping to make sure that this difference is just noise
iterations=10000
boot=[]
for i in range(iterations):
    boot_mean = fifa.sample(frac=1, replace=True).groupby('preferred_foot')['overall'].mean()
    boot.append(boot_mean)
    
boot=pd.DataFrame(boot)
boot.plot.kde()
((boot['Left']-boot['Right'])<0).count()

#first lets see the percentage of left footers
fifa[fifa.preferred_foot=='Left']['ID'].count()/fifa.shape[0]

#See which country that has more than 100 people has the most and least left-footers
fifa_sig = fifa.groupby('nationality')
fifa_sig = fifa_sig.filter(lambda x:x['nationality'].count()>=100)

fifa_left = pd.DataFrame(fifa_sig[fifa_sig.preferred_foot=='Left'].groupby('nationality')['ID'].count())
fifa_left['left_perc']= fifa_left['ID'].divide(fifa_sig.groupby('nationality')['ID'].count())
fifa_left_sorted = fifa_left.sort_values('left_perc')

_ = fifa_left_sorted.left_perc.plot.bar(rot=90)
plt.ylabel('Percentage of Players Left-Footed')

#see if any correlation with number of players in the top 500
#first lets get the best 11 from each country
fifa_best11 = fifa_sig.groupby('nationality').head(11)
#calculate average overall raiting per coutnries best 11
fifa_best11 = fifa_best11.groupby('nationality')['overall'].mean()
fifa_left['Overall'] = fifa_best11
#now we want to calculate the number per country in the top 1000
fifa_top1000 = fifa_sig[fifa_sig.Rank<=1500].groupby('nationality')['ID'].count()

#bubble plot
plt.scatter(fifa_best11, fifa_left.left_perc, s=10*fifa_top1000, alpha=0.5)
plt.ylabel('Percentage of Players Left-Footed')
plt.xlabel('Average Overall Rating if Top 11 Players')

#%% lets try some PCA
#first lets extract only the columns of interest
fifa_stats1 = fifa.loc[:,'overall':'weak_foot']
fifa_stats2 = fifa.loc[:,'crossing':'gk_reflexes']
fifa_stats = pd.concat([fifa_stats1, fifa_stats2], axis=1)


#first we standardize
from sklearn.preprocessing import StandardScaler
fifa_stats = StandardScaler().fit_transform(fifa_stats)

#now PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=10)
components = pca.fit_transform(fifa_stats)
comp_df = pd.DataFrame(components)

#lets try some neighbor stuff
from sklearn.neighbors import NearestNeighbors
#we'll just use numpy array
nbrs = NearestNeighbors(n_neighbors=6).fit(components)
distances, indices = nbrs.kneighbors(components)

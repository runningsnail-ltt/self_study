# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# df = pd.read_csv('data/table.csv',index_col='ID')
# print df.head()
#
# # 一、单级索引
#
# # 标签索引 loc
# print df.loc[1103] #单行索引
# print df.loc[[1103,2304]]
# print df.loc[1304:2103].head() # 左右全闭
#
# print df.loc[2402::-1].head()
#
# print df.loc[:,'Height'].head() # 单列索引
# print df.loc[:,['Height','Math']].head()
# #联合索引
# print df.loc[1102:2401,'Height':'Math'].head()
# #函数式索引
# print df.loc[lambda x:x['Gender']=='M'].head()
#
# #布尔索引
# print df.loc[df['Address'].isin(['street_7','street_4'])].head()
#
# for i in df['Address'].values:
#     print i[-1]
#
# print df.loc[[True if i[-1]=='4' or i[-1]=='7' else False for i in df["Address"].values]].head()
# # 本质上，loc能传入的只有布尔列表和索引子集构成的列表
#
# #iloc  位置索引
# print df.iloc[3:5]
# print df.iloc[3:4,7::-2]
# print df.iloc[(df['School']=='S_1').values].head()
#
# #[]
# #series d []操作
# s_int = pd.Series([1,2,3,4],index=[1,2,3,4])
# s_float = pd.Series([1,2,3,4],index=[1.,2.,3.,4.])
# print s_int
# print s_float
# # dataframe 的[]操作
# print df[1:2]
#
# row = df.index.get_loc(1102)
# print df[row:row+1]
#
# print df[['School','Math']].head()
# print df[df['Gender']=='F'].head()
#
# # 常用于列选择or 布尔选择，尽量避免行选择
#
# print df[df['Address'].isin(['street_1','street_2']) & df['Physics'].isin(['A','A+'])]
#
#
# math_interval = pd.cut(df['Math'],bins=[0,40,60,80,100])
# print math_interval.head()
#
# df_i = df.join(math_interval,rsuffix='_interval')[['Math','Math_interval']].reset_index().set_index('Math_interval')
# print df_i.head()
# print df_i.loc[[65,90]].head(10)
#
# #多级索引
#
# tuples = [('A','a'),('A','b'),('B','a'),('B','b')]
# mul_index = pd.MultiIndex.from_tuples(tuples,names=('Upper','Lower'))
# print mul_index
#
# print pd.DataFrame({'score':['perfect','good','fair','bad']},index=mul_index)
#
# df_using_mul = df.set_index(['Class','Address'])
# print df_using_mul.head()
# print df_using_mul.sort_index().loc[('C_2','street_6'):('C_3','street_4')]
# # 重复元素处理
# print df.duplicated('Class').head()
# print df['Class'].head()
#
# print df.drop_duplicates(['School','Class'])
#
# print df.shape
# np.random.rand()
#
df = pd.read_csv("./data/UFO.csv").head()
print df.head()
df.rename(columns={'duration (seconds)':'duration'},inplace=True)
print df.head()
df['duration'].astype('float')
print df[df['duration']>60]['shape'].value_counts().index[0]

bins_lng = np.linspace(-180,180,13)
bins_lat = np.linspace(-90,90,11)
cuts_lng = pd.cut(df['longitude'],bins=bins_lng)
cuts_lat = pd.cut(df['latitude'],bins=bins_lat)
df['cuts_lng'] = cuts_lng
df['cuts_lat'] = cuts_lat
print df.head()
print df.set_index(['cuts_lng','cuts_lat']).head()


df = pd.read_csv('data/Pokemon.csv')
print df.head()
print df.shape
print df['Type 2'].count()*1./df.shape[0]
df['Total'].astype('float')
print df[df['Total']>580]['Legendary'].value_counts(normalize=True)
print df[df['Type 1']=='Fighting'].sort_values(by='Attack',ascending=True).iloc[:3]






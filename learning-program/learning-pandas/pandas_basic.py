# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
print pd.__version__

# # 一、文件读取与写入
# # 1.读取
# df = pd.read_csv("./data/table.csv")
# print df.head()
# df_txt = pd.read_table("./data/table.txt")
# print df.head()
# df_excel = pd.read_excel("./data/table.xlsx")
# print df_excel.head()
#
# # 2.写入
# df.to_csv("data/new_table.csv")
# df.to_excel("data/new_table2.xlsx",sheet_name='Sheet1')
#
# # 二、基本数据结构
# # 1.Series
# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'],name='this is Series',dtype='float64')
# print s
# DataFrame
# df = pd.DataFrame({"col1":list("abcde"),"col2":range(5,10),"col3":[1.2,2.3,3.2,4.4,5.]},
#                   index=list('一二三四五'))
# df = pd.DataFrame({'col1':list('abcde'),'col2':range(5,10),'col3':[1.3,2.5,3.6,4.6,5.8]},
#                  index=["一","二","三","四","五"])
# # print df
# # #print type(df['col1'])# 从dataframe 中取出一列为series
# df.rename(columns={'col2':'new_col2'},inplace=True) # 修改列名
# print df

# df2 = df.rename({1: 9, 2: 10}, axis='index') # 修改行名
# print df2
# # 调用属性
# print df.index
# print df.columns
# print df.values
# print df.shape
# #调用方法
# print df.mean()
# # 索引对齐特性
#
# # 索引对齐特性
# df1 = pd.DataFrame({'A':[1,2,3]},index=[1,2,3])
# df2 = pd.DataFrame({'A':[1,2,3]},index=[3,1,2])
# print df2
# print df1-df2
# 列的删除与添加
# df2 = df.drop(index="五",columns="col1")
#
# print df2
# del df['col1']
# print df
#
# df['col1'] = list('abcde')
# print df

# s = df.mean()
# print s.index
# a = s.to_frame().T
# print a

# 常用基本函数
#1.head tail
#2.unique nunique
# df = pd.read_csv('data/table.csv')
# print df.head(10)
# print df['Physics'].unique() # 哪几个
# print df['Physics'].nunique() # 有几个
#
# print df['Physics'].count() #元素个数
# print df['Physics'].value_counts() # 返回每个元素有多少个
#
# print df.info()
#
# print df.describe() # 默认统计
#
# print df.describe(percentiles=[.05,.25,.75,.95])
#
# print df['Physics'].describe()
# print df['Math'].idxmax()
# #clip 截断  replace 替换
# print df['Address'].head()
#
# print df['Address'].replace(['street_1','street_2'],['one','two']).head()

#apply
# print df['Math'].head()
# print df['Math'].apply(lambda x:str(x)+'!').head()
#
# print df.apply(lambda x:x.apply(lambda x:str(x) + '!')).head()


#四 排序
#1 索引排序
# print df.set_index('Math').head() # 可设置索引
# print df.head()
# print df.set_index('Math').sort_index(ascending=False).head()
#
# # 值排序
# print df.sort_values(by='Class').head()
#
# # 多值排序
# print df.sort_values(by=['Address','Height'],ascending=False).head()


# 练习
# df = pd.read_csv("data/Game_of_Thrones_Script.csv")
# print df.head()
# print df['Name'].nunique()
# print df['Name'].value_counts(ascending=False).index[0]
# print df.assign(Words=df['Sentence'].apply(lambda x:len(x.split(" ")))).sort_values(by='Name').head()

df = pd.read_csv("./data/Kobe_data.csv",index_col='shot_id')
print df.head()
print pd.Series(list(zip(df['action_type'],df['combined_shot_type']))).value_counts().index[0]



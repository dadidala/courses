import pandas as pd
import seaborn as sns
import matplotlib. pyplot as plt

plt. rcParams ['font.sans-serif'] = ['SimHei']
plt. rcParams ['axes.unicode_minus' ] = False
df =pd. read_csv(r"C:\Users\周俊杰\Desktop\帮大忙了GPT\三上\统计学\data\chap02\example2_4.csv", encoding='gbk')
sns. set_style ('darkgrid')
sns.pairplot(df[['总股本','每股收益','每股净资产','每股现金流量']],
height=2,
diag_kind='hist',
kind='scatter')
sns.pairplot(df[['总股本','每股收益','每股净资产','每股现金流量']],
height=2,
diag_kind='kde',
markers='.',
kind='reg' )

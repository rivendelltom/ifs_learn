import pandas as pd
import numpy as np
df=pd.read_excel('t7.xlsx')#这个会直接默认读取到这个Excel的第一个表单
w = pd.Series([0.036 ,0.326, 0.192, 0.326, 0.120]
              ,index=[1,2,3,4,5])
def nromaldf(df):#归一化矩阵，笨办法筛选收益成本属性，之后优化
    i = [1, 3, 4,5]
    for i in i:
        df[i] = df[i] / (df[i].max())
    i = [2]
    for i in i:
        df[i] = (df[i].min())/df[i]
    return df
df=nromaldf(df)
df = df.mul(w,axis=1)#矩阵赋权
dfmin = pd.Series(df.min())
etemp = df.sub(dfmin, axis=1)
esum = (etemp ** 2).sum(axis=1)#获得欧氏距离
abssum = abs(etemp.sum(axis =1))#获得汉明距离
def comparision(esum,abssum):  # 构造对比矩阵
    n=len(esum)
    F=np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i==j:
                F[i,j]=0
            else:
                if np.abs(esum[i]-esum[j])<0.02:
                    F[i,j]=esum[i]-esum[j]
                else:
                    F[i,j]=esum[i]-esum[j]+abssum[i]-abssum[j]
    return F
df= comparision(esum,abssum)
print(df)
answer= df.sum(axis=1)
print(answer)

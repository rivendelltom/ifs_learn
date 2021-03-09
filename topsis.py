import pandas as pd
import numpy as np
df=pd.read_excel('t5.xlsx')#这个会直接默认读取到这个Excel的第一个表单
w = pd.Series([0.00854,0.008978,0.241101,0.274443,0.243986,
               0.049611,0.099215,0.008387,0.06539
               ],index=[1,2,3,4,5,6,7,8,9])

def maxnormaldf(df):#最大化消除量纲方法
    return df/(df.max())
df=maxnormaldf(df)

df = df.mul(w,axis=1)

def pis(df):#寻找正理想解
    dfmax = pd.Series(df.max())
    dfmin = pd.Series(df.min())
    pis = []
    pis.append(dfmax[1])
    for i in range(2, 5):
        pis.append(dfmin[i])
    for i in range(5, 10):
        pis.append(dfmax[i])
    return pis
def nis(df):#寻找负理想解
    dfmax = pd.Series(df.max())
    dfmin = pd.Series(df.min())
    nis = []
    nis.append(dfmin[1])
    for i in range(2, 5):
        nis.append(dfmax[i])
    for i in range(5, 10):
        nis.append(dfmin[i])
    return nis
pis = pis(df)
nis= nis(df)
def ranks(df,pis,nis):#排名方法
    pistemp = df.sub(pis, axis=1)
    print(pistemp)
    pistempsum = (pistemp ** 2).sum(axis=1)
    print(pistempsum)
    nistemp = df.sub(nis, axis=1)
    print(nistemp)
    nistempsum = (nistemp ** 2).sum(axis=1)
    print(nistempsum)
    return np.sqrt(nistempsum)/(np.sqrt(pistempsum)+np.sqrt(nistempsum))

print(ranks(df,pis,nis))
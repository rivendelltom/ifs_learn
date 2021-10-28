'''
求解属性值和权重值均为直觉模糊集合的多属性线性规划方法。
主要思想是吧直觉模糊集合转化为区间值进行权重的区间求解。
'''
from scipy import optimize as op
import pandas as pd#bikor算法实现
import  numpy as  np
np.set_printoptions(suppress=True)
w=[0.25,0.45,0.3]
def getdef(n):#获取矩阵
    return pd.read_excel('D:\study\\test\data\\t13.xlsx',sheet_name=n)
def getmatirx(df):
    df.iloc[:, [i % 2 == 1 for i in range(len(df.columns))]] = 1 - df.iloc[:,
                                                                   [i % 2 == 1 for i in range(len(df.columns))]]
    return df
def getliner(df):
    pass
def ranks(df):
    d1 = df.iloc[:, ::2]
    d2 = df.iloc[:, 1::2]
    df1=d1.T.reset_index(drop=True).T
    df2= d2.T.reset_index(drop=True).T
    print(df1)
    print(df2)
    gl=np.dot(df1,w)
    gu=np.dot(df2,w)
    print(gl)
    print(gu)
    g=gu/(1+gu-gl)
    return g
if __name__ == '__main__':
    df =getdef(0)
    print(df)
    df1=getmatirx(df)
    print(df1)
    print(ranks(df1))
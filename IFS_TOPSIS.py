import pandas as pd
import numpy as np
from matplotlib.cbook import flatten
'''ifs环境下的topsis实现

flatten是numpy.ndarray.flatten的一个函数，即返回一个一维数组。
flatten只能适用于numpy对象，即array或者mat，普通的list列表不适用！。
a.flatten()：a是个数组，a.flatten()就是把a降到一维，默认是按行的方向降 。
'''
def finpn(df):
        df=df
        pis = df.max()
        nis = df.min()
        for i in range(1,df.shape[1],2):
                temp = pis[i]
                pis[i] = nis[i]
                nis[i] = temp
        return pis, nis
def add_matrix(df):
        df=df
        df2=df.iloc[:,1::2].T.reset_index(drop=True).T
        df1=df.iloc[:,::2].T.reset_index(drop=True).T
        df3=1-df1-df2
        df4= pd.concat([df,df3],axis=1).T.reset_index(drop=True).T
        return df4

def ranks(df,pis,nis):#排名方法
        df=df
        pis=pis
        nis=nis
        pis1=1-pis[0::2].reset_index(drop=True)-pis[1::2].reset_index(drop=True)
        nis1=1-nis[0::2].reset_index(drop=True)-nis[1::2].reset_index(drop=True)
        pis2=pis.tolist()+pis1.tolist()
        nis2=nis.tolist()+nis1.tolist()
        print(pis2,nis2)
        pistemp = df.sub(pis2, axis=1)
        pistempsum = (pistemp ** 2).sum(axis=1)
        nistemp = df.sub(nis2, axis=1)
        nistempsum = (nistemp ** 2).sum(axis=1)
        return np.sqrt(nistempsum) / (np.sqrt(pistempsum) + np.sqrt(nistempsum))

if __name__ == '__main__':#主函数列出需要的矩阵，没有使用excel导入
        df = [[0.1875, 0.325, 0.21, 0.55, 0.24, 0.72],
              [0.20, 0.3625, 0.238, 0.52, 0.135, 0.825],
              [0.1, 0.5875, 0.2625, 0.43, 0.18, 0.755]]
        df = pd.DataFrame(df)

        pis,nis=finpn(df)
        df=add_matrix(df)
        print(df)
        print('方案收益值为\n ',ranks(df, pis,nis))

        b1 = pd.DataFrame([[0.3, 0.3], [0.1, 0.5], [0.7, 0.1], [0.4, 0.2]])
        w = [0.1, 0.4, 0.3, 0.2]
        print('直觉模糊加权集结算子', [1 - np.prod(np.power(1 - b1[0], w)), np.prod(np.power(b1[1], w))])


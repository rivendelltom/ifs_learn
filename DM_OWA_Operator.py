'''
np自带的insert函数非常强大，简单来说，就是传入三个参数，第一个参数是原数列，第二个单数是插入顺序，第三个参数是插入数列。
如果不指定轴参数，数组将以一维的形式进行排版，如果传入的参数，则按照给定的轴进行广播。
没有找到合适的方法对矩阵仅一列元素进行排序不改变整体，因此只能肉眼比大小，然后找出元素交换顺序，这里肯定还需要改进，
    目前看到的两个方法,一个是sort_index这个方法是对矩阵的索引进行排序，一个是sortvalues这个方法是对矩阵的值
   进行排序，两种方法都不适用于我的需求
'''
import pandas as pd#模糊综合评判
import numpy as np

def getdef():#获得矩阵
    return  pd.read_excel('D:\study\\test\data\\t12.xlsx')
def getentrx(df,w_author):#这里对矩阵进行加权
    df.iloc[:, [i % 2 == 0 for i in range(len(df.columns))]] =\
        1 - df.iloc[:,[i % 2 == 0 for i in range(len(df.columns))]]
    f = lambda df: df ** w_author  # 两个星号是幂的意思，和我现在用的power一样
    df = df.apply(f,axis=1)
    df.iloc[:, [i % 2 == 0 for i in range(len(df.columns))]] =\
        1 - df.iloc[:,[i % 2 == 0 for i in range(len(df.columns))]]
    return df
def getpoint(df):#这里计算矩阵的得分函数，然后根据得分函数重新排列矩阵。
    temp1= df.loc[3,1]
    temp2= df.loc[3,2]
    df.loc[3,1]=df.loc[3,3]
    df.loc[3,2]=df.loc[3,4]
    df.loc[3, 3] = temp1
    df.loc[3,4]=temp2
    return df
def ranks(df,w):#这里对方案进行选优，还是使用得分函数进行偏好关系的比较。
    d1 = df.iloc[:, ::2]
    d2 = df.iloc[:, 1::2]
    df1=d1.T.reset_index(drop=True).T
    df2= d2.T.reset_index(drop=True).T
    df2=1-df2
    df11= np.sqrt(1-np.prod(np.power(1-df1**2,w),axis=1))
    df22=1-np.sqrt(1-np.prod(np.power(1-df2**2,w),axis=1))
    df4=pd.concat([df11,df22],axis=1)
    df3=df11-df22
    return df3.sort_values(ascending=False)
if __name__ == '__main__':
    n = 4
    w_author = np.dot([0.35, 0.3, 0.25, 0.1], n)
    w_loc = [0.24, 0.26, 0.26, 0.24]
    w1 = np.insert(w_author, [0, 1, 2, 3], w_author)
    print(w1)
    w2 = np.array(w1)
    df=getdef()
    df1=getentrx(df,w2)
    print('初始矩阵为',df)
    print('加权矩阵为',df1)
    df2=getpoint(df1)
    print(df2)
    print(ranks(df2,w_loc))

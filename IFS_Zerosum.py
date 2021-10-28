'''
值为ifs的博弈论代码

一个很简单的小问题，range函数不支持小数步长，因此需要改成np.arange形式才能进行调参。
第二个问题是res返回所有的线性规划求解结果，比较冗长，如果仅需要x则可以通过res.x进行调用。

'''
from scipy import optimize as op
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)
def gety(df):#支持传入一个矩阵，其他参数还得调整
    c=np.array([0,0,0,1])
    A_ub=np.array(df)
    B_ub=np.array([0,0,0])
    A_eq=np.array([[1,1,1,0]])
    B_eq=np.array([1])
    x1=(0,1)
    x2=(0,1)
    x3=(0,1)
    x4=(None,0)
    res=op.linprog(c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3,x4))
    return res.x

if __name__ == '__main__':
    df=pd.DataFrame([[0.95,0.05,0.7,0.25,0.5,0.4],
                     [0.25,0.7,0.95,0.05,0.7,0.25],
                     [0.5,0.4,0.05,0.95,0.95,0.05]])
    l=0.5
    #对于奇偶列分别使用不同的函数操作，使用apply加匿名函数实现。
    df1=df.iloc[:,0::2].apply(lambda x :l*np.log(1-x))
    df2=df.iloc[:,1::2].apply(lambda x :(1-l)*np.log(x))
    '''重置列索引，需要把矩阵转置再转置'''
    df1=df1.T.reset_index(drop=True).T
    print(df1)
    df2=df2.T.reset_index(drop=True).T
    print(df2)
    #计算一个直觉模糊元的值，就是最后需要进行线性规划的原始矩阵
    df=df1+df2
    print(df)

    '''
    # dff=pd.concat([df1,df2],axis=1)
    # dff=dff.sort_index(axis=1)
    这两行代码的目的是将奇偶列操作后的矩阵复原，只需要简单的拼接后重置索引即可
    但这里不需要，作为一个方法记录
    
       求x的纳什均衡，就是求行策略，因此需要对行作线性规划。 
    '''
    df1=df.copy().T#因为要对源实矩阵作两次函数，因此复制保证不会被纂改
    df1.insert(loc=df1.shape[1],column=df1.shape[1],value=-1)
    #给矩阵添加新列，新列的索引就是df1.shape[1],因为左闭右开所以取不到右边界，右边界就是下一个索引
    print(df1)
    print(gety(df1))
    #求y的纳什均衡，就是求列策略，因此需要对列做线性规划
    df2=df.copy()
    df2.insert(loc=df2.shape[1],column=df2.shape[1],value=-1)
    print(df2)
    print(gety(df2))#对偶规划将矩阵转置再变号就相当与调用原规划，得到结果一致。
    # print(getx(df2.applymap(lambda x:-x)))


# def getx(df):
#     c=np.array([0,0,0,1])
#     A_ub=np.array(df)
#     B_ub=np.array([0,0,0])
#     A_eq=np.array([[1,1,1,0]])
#     B_eq=np.array([1])
#     x1=(0,1)
#     x2=(0,1)
#     x3=(0,1)
#     x4=(None,0)
#     res=op.linprog(-c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3,x4))
#     return res.x

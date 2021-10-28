'''
权重未知的直觉模糊多属性决策分式数学规划方法。
'''
import pandas as pd#bikor算法实现
import  numpy as  np
np.set_printoptions(suppress=True)
c=pd.DataFrame([[0.6708,0.8096],[0.6117,0.5959],[0.5748,0.7727]])#这些数据就是注释中的lingo代码所得。
print(c)
p=c[1]-c[0]
print(p)
p12=max(1-max((c.iloc[1,1]-c.iloc[0,0])/(p[0]+p[1]),0),0)
p23=max(1-max((c.loc[2,1]-c.loc[1,0])/(p[1]+p[2]),0),0)
p13=max(1-max((c.loc[2,1]-c.loc[0,0])/(p[0]+p[2]),0),0)
pmatrix=pd.DataFrame([[0.5,p12,p13],[1-p12,0.5,p23],[1-p13,1-p23,0.5]])
print(pmatrix)
n=3
for i in range(0,3):
    x=1/6*(sum(pmatrix.T[i])+1.5-1)
    print(x)
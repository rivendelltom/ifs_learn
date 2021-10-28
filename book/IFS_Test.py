import pandas as pd#AHP方法实现
from matplotlib.cbook import flatten
import numpy as np
import scipy as sp
a1= pd.DataFrame([[0.3,0.5],[0.4,0.5],[0.6,0.3]])
a2= pd.DataFrame([[0.2,0.4],[0.5,0.4],[0.5,0.1]])
print(a1)
print(a2)
#补集合运算
a3=a1.copy()
a3[[0,1]]=a3[[1,0]]#就是简单的两列索引互换，扩展到大型矩阵可以使用模运算和步长运算。
print(a3)

# #交运算
temp1=pd.Series(np.minimum(a1[0],a2[0]),name=0)
temp2=pd.Series(np.maximum(a1[1],a2[1]),name=1)
a4=pd.concat([temp1,temp2],axis=1)
print(a4)
# 并运算
temp1=pd.Series(np.maximum(a1[0],a2[0]),name=0)#需要注意的是max函数不可以，会提示运算元素类型不确定不知道该怎么运算的错误
temp2=pd.Series(np.minimum(a1[1],a2[1]),name=1)
a4=pd.concat([temp1,temp2],axis=1)
print(a4)
# 和运算
a5=pd.concat([pd.Series(a1[0]+a2[0]-a1[0]*a2[0]),pd.Series(a1[1]*a2[1])],axis=1)#熟练了之后就不用写temp直接concat链接矩阵，需要注意的是有中括号
print(a5)
# 积运算
a6=pd.concat([pd.Series(a1[0]*a2[0]),pd.Series(a1[1]+a2[1]-a1[1]*a2[1])],axis=1)#熟练了之后就不用写temp直接concat链接矩阵，需要注意的是有中括号
print(a6)
#数乘运算
miu= 2
a7 = pd.concat([pd.Series(1-np.power(1-a1[0],miu)),pd.Series(np.power(a1[1],miu))],axis=1)
print(a7)
#幂运算
a8= pd.concat([pd.Series(np.power(a1[0],miu)),pd.Series(1-np.power(1-a1[1],miu))],axis=1)
print(a8)
#截集运算
a10= pd.DataFrame([[0.3,0.5],[0.4,0.58],[0.6,0.3]])
a11= a10.copy()
a11[0]=a11[0]>=0.35#上截集
print(a11)
a12= a10.copy()
a12[1]=a12[1]<=0.5#下截集
print(a12)
a10[0]=a10[0]>=0.35#上下截集
a10[1]=a10[1]<=0.5
print(a10)
#相似度和距离
# 相似度，还是使用a1，a2进行计算。需要增加一列作为犹豫度
a1[2]=1-a1[0]-a1[1]
a2[2]=1-a2[0]-a2[1]
print(a1,'\n...\n',a2)
n=3
p1=1
temp31=(a1-a2).applymap(lambda x:abs(np.power(x,p1)))#灵活应用匿名函数和applymap函数对矩阵每一个元素进行运算
p2=2
temp32=(a1-a2).applymap(lambda x:abs(np.power(x,p2)))
temp33=temp31.sum(axis=1)/2/n
similar_mkv=1-(np.power((temp31.sum().sum())/2/n,1/p1))
similar_hanming=1-(np.power((temp32.sum().sum())/2/n,1/p2))
similar_chebi=1-max(temp33)
print('闵可夫斯基相似度为',similar_mkv,'汉明相似度为',similar_hanming,'切比雪夫相似度为',similar_chebi,
      '\n闵可夫斯基距离为',1-similar_mkv,'汉明距离为',1-similar_hanming,'切比雪夫距离为',1-similar_chebi)#如何将矩阵所有元素相加，调用两遍sum函数即可。
#直觉模糊集加权集结算子
b1=pd.DataFrame([[0.3,0.3],[0.1,0.5],[0.7,0.1],[0.4,0.2]])
w=[0.1,0.4,0.3,0.2]
print('直觉模糊加权集结算子',[1-np.prod(np.power(1-b1[0],w)),np.prod(np.power(b1[1],w))])
#直觉模糊集有序加权集结算子
b2=pd.DataFrame([[0.5,0.1],[0.1,0.2],[0.2,0.4],[0.3,0.2]])
w_loc=[0.155,0.345,0.345,0.155]
b2[2]=b2[0]-b2[1]#添加新列计算得分函数
b2.sort_values(2,inplace=True,ascending=False)#通过sortvalues函数对矩阵进行排序,注意这里可以传入两个参数，一个控制是否扩展到全部，一个控制升序。
print(b2)
b2[0]=1-b2[0]#提前把第一列减去1，方便之后广播
b2=np.prod(np.power(b2.drop([2],axis=1).T,w),axis=1)
print('直觉模糊有序加权集结算子',[1-b2[0],b2[1]])
#直觉模糊集混合加权集结算子

n=5
b3=pd.DataFrame([[0.2,0.5],[0.7,0.1],[0.5,0.2],[0.3,0.4],[0.6,0.2]])
w3_loc=[0.112,0.236,0.304,0.23,0.112]
w3_auther=np.dot([0.25,0.2,0.15,0.18,0.22],n)
b3[0]=1-b3[0]
b3=np.power(b3.T,w3_auther).T
b3[0]=1-b3[0]
b3[2]=b3[0]-b3[1]#添加新列计算得分函数
b3.sort_values(2,inplace=True,ascending=False)#通过sortvalues函数对矩阵进行排序
b3[0]=1-b3[0]#提前把第一列减去1，方便之后广播
b3=np.prod(np.power(b3.drop([2],axis=1).T,w3_loc),axis=1)
print('直觉模糊混合加权集结算子',[1-b3[0],b3[1]])
#广义直觉模糊集有序加权集结算子
b4=pd.DataFrame([[0.5,0.1],[0.1,0.2],[0.2,0.4],[0.3,0.2]])
w4_loc=[0.155,0.345,0.345,0.155]
b4[2]=b4[0]-b4[1]#添加新列计算得分函数
b4.sort_values(2,inplace=True,ascending=False)#通过sortvalues函数对矩阵进行排序
b4[0]=1-b4[0]*b4[0]
b4[1]=1-(1-b4[1])*(1-b4[1])#注意运算规则，不然不可能算对，这里有很多1-的形式
print(b4)
b4=b4.drop([2],axis=1).T
print(b4)
p4=1/2
b4=np.power(1-np.prod(np.power(b4,w4_loc),axis=1),p4)
print(b4)
print('广义直觉模糊有序加权集结算子',[b4[0],1-b4[1]])
#直觉模糊集混合加权集结算子
n=5
b5=pd.DataFrame([[0.2,0.5],[0.7,0.1],[0.5,0.2],[0.3,0.4],[0.6,0.2]])
w5_loc=[0.112,0.236,0.304,0.23,0.112]
w5_auther=np.dot([0.25,0.2,0.15,0.18,0.22],n)
b5[0]=1-b5[0]
b5=np.power(b5.T,w5_auther).T
b5[0]=1-b5[0]
b5[2]=b5[0]-b5[1]#添加新列计算得分函数
b5.sort_values(2,inplace=True,ascending=False)#通过sortvalues函数对矩阵进行排序
print(b5)
b5[0]=1-b5[0]*b5[0]
b5[1]=1-(1-b5[1])*(1-b5[1])
b5=b5.drop([2],axis=1).T
print(b5)
p4=1/2
b5=np.power(1-np.prod(np.power(b5,w5_loc),axis=1),p4)
print(b5)
print('广义直觉模糊混合加权集结算子',[b5[0],1-b5[1]])

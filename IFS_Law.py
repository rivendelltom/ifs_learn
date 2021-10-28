import pandas as pd#AHP方法实现
from matplotlib.cbook import flatten
import numpy as np
import scipy as sp

inf=9999999 #代表n

def ifs_jiao(coords1, coords2):  # 交运算

      t = list(zip(coords1, coords2))
      t1 = min(t[0])
      t2 = max(t[1])
      return [t1, t2]


def ifs_bing(coords1, coords2):  # 并运算

    t = list(zip(coords1, coords2))
    print(t)
    t1 = max(t[0])
    t2 = min(t[1])
    return [t1, t2]


def plus(coords1, coords2):  # 和运算，支持一对一（就算一个元素也要写成二维数组的形式），多对多
    d1=[]
    d2=[]
    d=[]
    for (x, y) in zip(coords1, coords2):
        d1.append(x[0]+y[0]-x[0]*y[0])
        d2.append(x[1]*y[1])
    t=list(zip(*[d1,d2]))
    for i in t:
        d.append(list(i))
    return d
def times(coords1, coords2):  # 机运算
    d1=[]
    d2=[]
    d=[]
    for (x, y) in zip(coords1, coords2):
        d1.append(x[0]*y[0])
        d2.append(x[1]+y[1]-x[1]*y[1])
    t=list(zip(*[d1,d2]))
    for i in t:
        d.append(list(i))
    return d
def ltimes(lamda, coords2):  # 数乘运算
    d1=[]
    d2=[]
    d=[]
    for x,y in coords2:
        d1.append((1-(1-x)**lamda))
        d2.append(y**lamda)
    t=list(zip(*[d1,d2]))
    for i in t:
        d.append(list(i))
    return d

def lpower(lamda, coords2):  # 乘方运算
    d1=[]
    d2=[]
    d=[]
    for x,y in coords2:
        # print(x)
        d1.append(x**lamda)
        # print(d1)
        d2.append((1-(1-y)**lamda))
    t=list(zip(*[d1,d2]))
    for i in t:
        d.append(list(i))
    return d


def distance(coords1, coords2,q):  # 计算距离的函数，q可以实现汉明，欧几里得，闵可夫斯基，切比雪夫距离
    n=len(coords1)
    # print(n)
    pai=[]
    d3=[]
    dis=0
    for (x, y) in zip(coords1, coords2):
        pai.append(np.array(1 -x[0]-x[1])-np.array(1- y[0]-y[1]))
        d3.append(np.ndarray.tolist(np.array(x)-np.array(y)))
    t1 ,t2= list(zip(*d3))
    if q==1:
        dis =1- (0.5*(1/n)*(sum(np.abs(t1)+np.abs(t2)+np.abs(pai))))**(1/q)
    if q>=2:
        dis =1-(0.5*(1/n)*(sum(np.power(t1,q)+np.power(t2,q)+np.power(pai,q))))**(1/q)
    if q == inf:
        t = zip(np.abs(t1) , np.abs(t2) , np.abs(pai))
        dis = 1-max(list(map(lambda x: (x[1] + x[0]+x[2])/(2*n), list(t))))
    return dis

def weight_distance(coords1, coords2,q,w):  # 计算加权的距离的函数
    n=len(coords1)
    pai=[]
    d3=[]
    dis=0
    for (x, y) in zip(coords1, coords2):
        pai.append(np.array(1 -x[0]-x[1])-np.array(1- y[0]-y[1]))
        d3.append(np.ndarray.tolist(np.array(x)-np.array(y)))
    t1 ,t2= list(zip(*d3))
    if q==1:
        dis =1- 0.5*(sum(w*(np.abs(t1)+np.abs(t2)+np.abs(pai))))
    if q>=2:
        dis =1- (0.5*np.sum(w * (np.power(t1, q) + np.power(t2, q) + np.power(pai, q))))**(1/q)
    # if q == inf:
    #懒得写了，切比雪夫距离一般用不到
    return dis

def score(coords1):  # 计算得分函数
    d=[]
    for x,y in coords1:
        d.append(0.5*(1+x**2-y**2))
    return d
def accuary(coords1):  # 计算精确函数
    d=[]
    for x,y in coords1:
        d.append(x**2+y**2)
    return d
'''一些简单的求证'''


# r1= [[0.60224478, 0.50081728], [0.41091797, 0.38037781], [0.49799925, 0.3999552], [0.39999402, 0.20004067],
#      [0.70089936, 0.20342314], [0.54685869, 0.36404414], [0.63890544, 0.21956757],
#      [0.72670034, 0.26658183],
#      [0.70140379, 0.39981306], [0.63702608, 0.26155653], [0.77805036, 0.244334], [0.6637266, 0.2221812],
#      [0.45529538, 0.61452352], [0.49580874, 0.3985400], [0.35741231, 0.72991492], [
#          0.33215769, 0.59686713]]
# r=score(r)
# print(r)
# df1 = [[0.3, 0.5],[0.4,0.5],[0.6,0.3]]
# print(accuary(df1))
# df2 = [[0.2,0.4],[0.5,0.4],[0.5,0.1]]
# df3=[[0.3,0.5]]
# df4=[[0.2,0.4]]
# print(ifs_plus(df1,df2))
# print(ifs_times(df1,df2))
# print(ifs_lamdatimes(2,df1))
# print(ifs_lamdapower(2,df1))
# print(distance(df1,df2,2))
# print(distance(df1,df2,1))
# print(distance(df1,df2,inf))
# w=np.array([0.5,0.2,0.3])
# print(weight_distance(df1,df2,1,w))
# print(weight_distance(df1,df2,2,w))

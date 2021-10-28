import pandas as pd
from matplotlib.cbook import flatten
import numpy as np
import scipy as sp
'''贝叶斯网络代码
    核心公式就是全概率公式
    p(a1)=p(a1|t1)p(t1)+p(a1|t2)p(t2)
    知道先验概率，知道条件概率，就可以得到后验概率

'''

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

if __name__ == '__main__':
    ventilation=[[0.45,0.3],[0.6,0.2],[0.68,0.3],[0.5,0.5]]
    collapse=[[0.55,0.2],[0.35,0.26],[0.32,0.26],[0.72,0.14]]
    gas=[[0.72,0.2],[0.4,0.3],[0.45,0.3],[0.55,0.2]]
    smoke=[[0.34,0.2],[0.58,0.4],[0.8,0.15],[0.34,0.25]]
    reduce=[[0.67,0.3],[0.45,0.4],[0.53,0.13],[0.73,0.15]]
    rescue=[[0.8,0.1],[0.35,0.2],[0.58,0.2],[0.5,0.43]]
    facility=[[0.54,0.25],[0.48,0.5],
              [0.85,0.13],[0.25,0.4],
              [0.38,0.41],[0.72,0.15],
              [0.63,0.39],[0.42,0.28]]
    evidence=[[0.8,0.2],[0.2,0.1],[0.3,0.4],[0.7,0.1],
              [0.44,0.5],[0.62,0.31],[0.55,0.35],[0.5,0.4],
              [0.2,0.2],[0.8,0.15],[0.72,0.16],[0.3,0.4]]

    #
    # t1=plus(times([ventilation[0]],[evidence[0]]),
    #         times([ventilation[2]],[evidence[1]]))
    # t2=plus(times([ventilation[1]],[evidence[0]]),
    #            times([ventilation[3]],[evidence[1]]))
    # a1=plus(times([gas[0]],t1),
    #            times([gas[2]],t2))
    # a2=plus(times([gas[1]],t1),
    #            times([gas[3]],t2))
    # print(a1,a2)

    # t1=plus(times([ventilation[0]],[evidence[4]]),
    #         times([ventilation[2]],[evidence[5]]))
    # t2=plus(times([ventilation[1]],[evidence[4]]),
    #            times([ventilation[3]],[evidence[5]]))
    # a1=plus(times([gas[0]],t1),
    #            times([gas[2]],t2))
    # a2=plus(times([gas[1]],t1),
    #            times([gas[3]],t2))
    # print(a1,a2)
    #
    # t1=plus(times([ventilation[0]],[evidence[8]]),
    #         times([ventilation[2]],[evidence[9]]))
    # t2=plus(times([ventilation[1]],[evidence[8]]),
    #            times([ventilation[3]],[evidence[9]]))
    # a1=plus(times([gas[0]],t1),
    #            times([gas[2]],t2))
    # a2=plus(times([gas[1]],t1),
    #            times([gas[3]],t2))
    # print(a1,a2)
    #
    # t1=plus(times([ventilation[0]],[evidence[0]]),
    #         times([ventilation[2]],[evidence[1]]))
    # t2=plus(times([ventilation[1]],[evidence[0]]),
    #            times([ventilation[3]],[evidence[1]]))
    # a1=plus(times([gas[0]],t1),
    #            times([gas[2]],t2))
    # a2=plus(times([gas[1]],t1),
    #            times([gas[3]],t2))
    # print(a1,a2)
    #
    # t1=plus(times([ventilation[0]],[evidence[4]]),
    #         times([ventilation[2]],[evidence[5]]))
    # t2=plus(times([ventilation[1]],[evidence[4]]),
    #            times([ventilation[3]],[evidence[5]]))
    # a1=plus(times([gas[0]],t1),
    #            times([gas[2]],t2))
    # a2=plus(times([gas[1]],t1),
    #            times([gas[3]],t2))
    # print(a1,a2)
    #
    # t1=plus(times([ventilation[0]],[evidence[8]]),
    #         times([ventilation[2]],[evidence[9]]))
    # t2=plus(times([ventilation[1]],[evidence[8]]),
    #            times([ventilation[3]],[evidence[9]]))
    # a1=plus(times([gas[0]],t1),
    #            times([gas[2]],t2))
    # a2=plus(times([gas[1]],t1),
    #            times([gas[3]],t2))
    # print(a1,a2)

    # t1=plus(times([[0.34,0.25]],[[0.8,0.2]]),
    #            times([[0.48,0.5]],[[0.2,0.1]]))
    # t2=plus(times([[0.48,0.25]],[[0.2,0.1]]),
    #            times([[0.2,0.1]],[[0.2,0.1]]))
    # t3=plus(times([[0.48,0.5]],[[0.8,0.2]]),
    #            times([[0.7,0.1]],[[0.8,0.2]]))
    # t2=plus(times([[0.2,0.1]],[[0.7,0.1]]),
    #            times([[0.2,0.1]],[[0.7,0.1]]))
    #
    # a1=plus(times([[0.54,0.25]],t1),
    #            times([[0.85,0.13]],t2))
    # a2=plus(times([[0.48,0.5]],t1),
    #            times([[0.25,0.4]],t2))
    # a3=plus(times([[0.38,0.41]],t1),
    #            times([[0.63,0.39]],t2))
    # a4=plus(times([[0.72,0.15]],t1),
    #            times([[0.42,0.28]],t2))
    # print(a1,a2,a3,a4)
    esd111 = [[0.54, 0.25]]
    esd101 = [[0.85, 0.13]]
    esd011 = [[0.38, 0.41]]
    esd001 = [[0.63, 0.39]]
    e1 = [[0.8, 0.2]]
    e0 = [[0.2, 0.1]]
    s1 = [[0.3, 0.4]]
    s0 = [[0.7, 0.1]]
    pd1 = times(times(e1, s1), esd111)
    pd2 = times(times(e1, s0), esd101)
    pd3 = times(times(e0, s1), esd011)
    pd4 = times(times(e0, s0), esd001)
    pd = plus(plus(pd1, pd2), plus(pd3, pd4))
    print(pd)


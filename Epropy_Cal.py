'''计算直觉模糊熵'''
import numpy as np
import math

# print(df[1][0])
def oldetro(df):
    pai = []
    n = []
    s = []
    #
    # for i in range(len(df)):
        # pai.append(((1 - abs(df[i][0] - df[i][1]))**2+(1-df[i][0] - df[i][1])**2)*0.5)
        # print(pai)
        # n.append((1-df[i][1]-df[i][0]))
        # print(n)
        # s.append(1/np.tan(0.25*math.pi-0.25*math.pi*abs(df[i][0]**2-df[i][1]**2)))
        # print(s)

def gete(df):
    df=df
    e = []
    for i in range(len(df)):
        huv = df[i][0] * math.log((df[i][0] / (0.5 * df[i][0] + df[i][1])), 2) + \
              (1 - df[i][0]) * math.log(((1 - df[i][0]) / (1 - 0.5 * (df[i][0] + df[i][1]))), 2)
        hvu = df[i][1] * math.log((df[i][1] / (0.5 * df[i][1] + df[i][0])), 2) + \
              (1 - df[i][1]) * math.log(((1 - df[i][1]) / (1 - 0.5 * (df[i][1] + df[i][0]))), 2)
        e.append( huv + hvu)
    return e
def etro(df,e):
    df=df
    e=e
    score=[]
    for i in range(len(df)):
        if df[i][0]>df[i][1]:
            score.append(df[i][0]-df[i][1]+e[i])
        elif df[i][0]>df[i][1]:
            score.append(df[i][0]-df[i][1]-e[i])
        else:
            score.append(0)
    return score
if __name__ == '__main__':
    df = [[0.4842, 0.1448], [0.5129, 0.1051], [0.4573, 0.0892],
          [0.5185, 0.0612], [0.5936, 0.0824]]
    e=gete(df)
    etro1=etro(df,e)
    print(etro1)

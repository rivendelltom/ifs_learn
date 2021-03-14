import pandas as pd
df=pd.read_excel('t1.xlsx')#这个会直接默认读取到这个Excel的第一个表单
w = pd.Series([0.106,0.126,0.030,0.023,0.112,0.127,0.143,
0.090,0.122,0.122],index=[1,2,3,4,5,6,7,8,9,10])
def nromaldf(df):#归一化矩阵，笨办法筛选收益成本属性，之后优化
    i = [6, 7, 9, 10]
    for i in i:
        df[i] = (df[i] - df[i].min()) / (df[i].max() - df[i].min())
    i = [1, 2, 3, 4, 5, 8]
    for i in i:
        df[i] = (df[i].max() - df[i]) / (df[i].max() - df[i].min())
    return df
nromaldf(df)
fmax = df[:].max()
fmin = df[:].min()
def ranks(df):
    s = ((fmax[:] - df[:]) / (fmax[:] - fmin[:])).dot(w)
    return s
def rankr(df):
    s2 = ((fmax[:] - df[:]) / (fmax[:] - fmin[:])) * w
    r = s2.max(axis=1)
    return r
def rankq(df,s,r):
    v = 0.2
    q = []
    q = v * (s - s.min()) / (s.max() - s.min()) + (1 - v) * (r - r.min()) / (r.max() - r.min())
    return q
print('计算结果s\n',ranks(df))
print('计算结果r\n',rankr(df))
print('计算结果q\n',rankq(df,ranks(df),rankr(df)))
df.to_excel('t2.xlsx')

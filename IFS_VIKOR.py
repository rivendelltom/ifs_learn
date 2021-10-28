import pandas as pd
import  numpy as  np
import re
import  IFS
'''直觉的 vikor算法实现
另一种奇偶列运算的实现方法，直接块级运算。
'''
# def vikor(df,w,v=0.2):
#     df = df.copy()
#     df1=df.iloc[0::2].reset_index(drop=True)
#     df2=df.iloc[1::2].reset_index(drop=True)
#     # print(df1)
#     # print(df2)
#     pisu = df1.max()
#     pisv= df2.min()
#     nisu = df1.min()
#     nisv= df2.max()
#     lower=(((df1 - pisu)**2+(df2-pisv)**2)*0.5)**0.5 / \
#           (((pisu - nisu) ** 2 + (pisv - nisv) ** 2) * 0.5) ** 0.5
#     s= np.sum(lower*w,axis=1)
#     r= np.max(lower*w,axis=1)
#     q= lambda s,r: v* (s - s.min()) / (s.max() - s.min()) +\
#                    (1 - v) * (r - r.min()) / (r.max() - r.min())
#     return s,r,q(s,r)
# if __name__ == '__main__':#主函数
#     url = 'D:\study\\test\data\\21.xlsx'
#     w = [0.093, 0.084, 0.088, 0.084, 0.078,
#     0.072, 0.077, 0.088,0.073, 0.264]
#     df=pd.read_excel(url,header=None).T
#     s ,r, q= vikor(df,w)
#     print('计算结果s\n',s,'\n','计算结果r\n',r,'\n','计算结果q\n',q )

def vikor(df,w,v=0.2):
    df = df.copy()
    df1=df.iloc[0::2].reset_index(drop=True)
    df2=df.iloc[1::2].reset_index(drop=True)
    print(df1)
    print(df2)
    pisu = df1.max()
    print(pisu)
    pisv= df2.min()
    nisu = df1.min()
    nisv= df2.max()
    lower=(((df1 - pisu)**2+(df2-pisv)**2)*0.5)**0.5 / \
          (((pisu - nisu) ** 2 + (pisv - nisv) ** 2) * 0.5) ** 0.5
    s= np.sum(lower*w,axis=1)
    r= np.max(lower*w,axis=1)
    q= lambda s,r: v* (s - s.min()) / (s.max() - s.min()) +\
                   (1 - v) * (r - r.min()) / (r.max() - r.min())
    return s,r,q(s,r)
if __name__ == '__main__':#主函数
    url = 'D:\study\\test\data\\21.xlsx'
    w = [0.093, 0.084, 0.088, 0.084, 0.078,
    0.072, 0.077, 0.088,0.073, 0.264]
    df=pd.read_excel(url,header=None).T
    print(df)
    s ,r, q= vikor(df,w)
    print('计算结果s\n',s,'\n','计算结果r\n',r,'\n','计算结果q\n',q )
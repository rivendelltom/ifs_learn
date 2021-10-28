'''
'''
from scipy import optimize as op
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)
def getlinerx(a,b,l):
    c=np.array([(1+l)*0.25,(1+l)*0.25,(1-l)*0.25,(1-l)*0.25,0,0])
    A_ub=np.array([[1,0,0,0,-(175*(0.6-a)+180*a)/0.6,-(80*(0.9-a)+90*a)/0.9],
                    [1,0,0,0,-(150*(0.6-a)+156*a)/0.6,-(175*(0.6-a)+180*a)/0.6],
                    [0,0,1,0,-(190*(0.6-a)+180*a)/0.6,-(108*(0.9-a)+90*a)/0.9],
                    [0,0,1,0,-(158*(0.6-a)+156*a)/0.6,-(190*(0.6-a)+180*a)/0.6],
                    [0,1,0,0,-(180*(1-b)+175*(b-0.2))/0.8,-(90*(1-b)+80*(b-0.1))/0.9],
                    [0,1,0,0,-(156*(1-b)+150*(b-0.1))/0.9,-(180*(1-b)+175*(b-0.2))/0.8],
                    [0,0,0,1,-(180*(1-b)+190*(b-0.2))/0.8,-(90*(1-b)+100*(b-0.1))/0.9],
                    [0,0,0,1,-(156*(1-b)+158*(b-0.1))/0.9,-(180*(1-b)+190*(b-0.2))/0.8]])
    B_ub=np.array([0,0,0,0,0,0,0,0])
    A_eq=np.array([[0,0,0,0,1,1]])
    B_eq=np.array([1])
    x5=(0,1)
    x6=(0,1)
    x1=(None,None)
    x2=(None,None)
    x3=(None,None)
    x4=(None,None)
    res=op.linprog(-c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3,x4,x5,x6))
    return res.x
def getlinery(a,b,l):
    c=np.array([(1+l)*0.25,(1+l)*0.25,(1-l)*0.25,(1-l)*0.25,0,0])
    A_ub=np.array([[-1,0,0,0,(175*(0.6-a)+180*a)/0.6,(150*(0.6-a)+150*a)/0.6],
                    [-1,0,0,0,(80*(0.9-a)+90*a)/0.9,(175*(0.6-a)+180*a)/0.6],
                    [0,0,-1,0,(190*(0.6-a)+180*a)/0.6,(158*(0.6-a)+156*a)/0.6],
                    [0,0,-1,0,(100*(0.9-a)+90*a)/0.9,(190*(0.6-a)+180*a)/0.6],
                    [0,-1,0,0,(180*(1-b)+175*(b-0.2))/0.8,(156*(1-b)+150*(b-0.1))/0.9],
                    [0,-1,0,0,(90*(1-b)+80*(b-0.1))/0.9,(180*(1-b)+175*(b-0.2))/0.8],
                    [0,0,0,-1,(180*(1-b)+190*(b-0.2))/0.8,(156*(1-b)+150*(b-0.1))/0.9],
                    [0,0,0,-1,(90*(1-b)+100*(b-0.1))/0.9,(180*(1-b)+190*(b-0.2))/0.8]])
    B_ub=np.array([0,0,0,0,0,0,0,0])
    A_eq=np.array([[0,0,0,0,1,1]])
    B_eq=np.array([1])
    x5=(0,1)
    x6=(0,1)
    x1=(None,None)
    x2=(None,None)
    x3=(None,None)
    x4=(None,None)
    res=op.linprog(c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3,x4,x5,x6))
    return res.x
def meanx(l):
    c = np.array([0, 0,1])
    A_ub = np.array([[181.25*(0.8-0.2*l),155*(0.9-0.3*l),-1]
                        ,[90*0.9*l,181.25*(0.8-0.2*l),-1]])
    B_ub = np.array([0, 0])
    A_eq = np.array([[1, 1,0]])
    B_eq = np.array([1])
    x1 = (0, 1)
    x2 = (0, 1)
    x3 = (None, None)
    res = op.linprog(c, A_ub, B_ub, A_eq, B_eq, bounds=(x1, x2, x3))
    return res.x
if __name__ == '__main__':
    print(pd.DataFrame([getlinerx(0,1,0.1),getlinerx(0.1,0.8,0.1),getlinerx(0.2,0.7,0.1),getlinerx(0.3,0.6,0.1),
           getlinerx(0.4,0.5,0.1),getlinerx(0.5,0.3,0.1),getlinerx(0.6,0.2,0.1)]))
    print(pd.DataFrame([getlinery(0,1,0.1),getlinery(0.1,0.8,0.1),getlinery(0.2,0.7,0.1),getlinery(0.3,0.6,0.1),
           getlinery(0.4,0.5,0.1),getlinery(0.5,0.3,0.1),getlinery(0.6,0.2,0.1)]))
    for l in np.arange(0, 1, 0.1):
        print(meanx(l))
        # , [(150 + 2 * 156 + 158) * 0.25 * (0.9 - 0.3 * l), (0.75 + 2 * 180 + 190) * 0.25 * (0.8 - 0.2 * l), -1]])
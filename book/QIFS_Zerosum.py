'''
'''
from scipy import optimize as op
import numpy as np
np.set_printoptions(suppress=True)
for l in np.arange(0,1,0.1):
    c=np.array([0,0,0,0.5])
    A_ub=np.array([[np.log(0.2)*l+(np.log(0.02))*(1-l)+(np.log(0.1))*l+(np.log(0.1))*(1-l),
                       np.log(0.9)*l+np.log(0.5)*(1-l)+np.log(0.75)*l+np.log(0.7)*(1-l),
                       np.log(0.7)*l+np.log(0.3)*(1-l)+np.log(0.5)*l+np.log(0.4)*(1-l),-1]

                      ,[np.log(0.45)*l+np.log(0.1)*(1-l)+np.log(0.3)*l+np.log(0.25)*(1-l),
                       np.log(0.2)*l+np.log(0.01)*(1-l)+np.log(0.1)*l+np.log(0.05)*(1-l),
                       np.log(1)*l+np.log(0.85)*(1-l)+np.log(0.95)*l+np.log(0.95)*(1-l),-1],

                   [np.log(0.65) * l + np.log(0.2) * (1 - l) + np.log(0.5) * l + np.log(0.4)* (1 - l),
                   np.log(0.45) * l + np.log(0.1) * (1 - l) + np.log(0.3) * l + np.log(0.25) * (1 - l),
                   np.log(0.2) * l + np.log(0.01) * (1 - l) + np.log(0.1) * l + np.log(0.05) * (1 - l), -1]])
    B_ub=np.array([0,0,0])
    A_eq=np.array([[1,1,1,0]])
    B_eq=np.array([1])
    x1=(0,1)
    x2=(0,1)
    x3=(0,1)
    x4=(None,0)
    res=op.linprog(c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3,x4))
    print(res.x)
print("...")
for l in np.arange(0,1,0.1):
    c=np.array([0,0,0,0.5])
    A_ub=np.array([[-(np.log(0.2)*l+(np.log(0.02))*(1-l)+(np.log(0.1))*l+(np.log(0.1))*(1-l)),
                       -(np.log(0.45)*l+np.log(0.1)*(1-l)+np.log(0.3)*l+np.log(0.25)*(1-l)),
                       -(np.log(0.65)*l+np.log(0.2)*(1-l)+np.log(0.5)*l+np.log(0.4)*(1-l)),1]

                      ,[-(np.log(0.9)*l+np.log(0.5)*(1-l)+np.log(0.75)*l+np.log(0.7)*(1-l)),
                       -(np.log(0.2)*l+np.log(0.01)*(1-l)+np.log(0.1)*l+np.log(0.05)*(1-l)),
                       -(np.log(0.45)*l+np.log(0.1)*(1-l)+np.log(0.3)*l+np.log(0.25)*(1-l)),1],

                   [-(np.log(0.7) * l + np.log(0.3) * (1 - l) + np.log(0.5) * l + np.log(0.4)* (1 - l)),
                   -(np.log(1) * l + np.log(0.85) * (1 - l) + np.log(0.95) * l + np.log(0.95) * (1 - l)),
                   -(np.log(0.2) * l + np.log(0.01) * (1 - l) + np.log(0.1) * l + np.log(0.05) * (1 - l)), 1]])
    B_ub=np.array([0,0,0])
    A_eq=np.array([[1,1,1,0]])
    B_eq=np.array([1])
    x1=(0,1)
    x2=(0,1)
    x3=(0,1)
    x4=(None,0)
    res=op.linprog(-c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3,x4))
    print(res.x)
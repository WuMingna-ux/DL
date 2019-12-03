# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:59:35 2019

@author: wumingna
"""
#import tensorflow as tf
#from tensorflow.keras import layers  #常见的神经网络都包含在keras.layer中
#print(tf.__version__)
#print(tf.keras.__version__)

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,4*np.pi)
y=np.sin(x)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['figure.figsize']=(8.0,6.0)
plt.title('sin图')
plt.rcParams['lines.linestyle']='-.'
plt.rcParams['lines.linewidth']=3
plt.plot(x, y, label='$sin(x)$')
plt.show()

fig=plt.figure() #生成画布
figa=plt.gca()  #获得当前画布焦点
N=100
xn=np.random.rand(N,2) #随机生成一个N*2的数组
x=np.linspace(0,1)  #在0，1之间得到一些均匀分布的数字，默认是50

a=np.random.rand()
b=np.random.rand()
f=lambda x:a*x+b   

plt.plot(x,f(x),'r')
yn=np.zeros([N,1])  #得到一个N*1的全0数组 
w = np.zero(3);
maxIter=10
for i in range(N):
    if(f(xn[i,0]) > xn[i,1]):
        yn[i]=1
        plt.plot(xn[i,0],xn[i,1],'bo',markersize=12)
    else:
        yn[i]=-1
        plt.plot(xn[i,0],xn[i,1],'go',markersize=12)
N = xn.shape[0]
f = lambda x:np.sign(w[0]*1+w[1]*x[0]+w[2]*x[1])
for _ in range(MaxIter):
    i=np.random.randint(N)
    if(yn[i] !=f(xn[i,0])):
        w[0]=w[0]+yn[i]*1*a
        w[1]=w[1]+yn[i]*xn[i,0]*a
        w[2]=w[2]+yn[i]*xn[i,1]*a

    
        
    
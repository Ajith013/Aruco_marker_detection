#!/usr/bin/env python
# coding: utf-8

# In[50]:



import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# In[51]:



def animate1(i):
    ax = plt.axes(projection='3d')
    data = pd.read_csv('data.csv')
    y1 = data['x'].astype(float)
    y2 = data['y'].astype(float)
    y3 = data['z'].astype(float)
    X,Y,Z = zip(*sorted(zip(y1,y2,y3)))
    ax.cla()
    #ax.scatter(y1, y2, y3)
    ax.plot(Z, label='Random 3D data')
    #ax.plot3D(X, Y, Z, label='Random 3D data')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate1, interval= 100)

plt.tight_layout()
plt.show()


# In[ ]:





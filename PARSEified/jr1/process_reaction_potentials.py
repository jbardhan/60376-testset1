import numpy as np

r33=np.loadtxt('ref-33.txt')    
r257=np.loadtxt('ref-257.txt')
s257=np.loadtxt('solv-257.txt')
s33=np.loadtxt('solv-33.txt')
reac33=s33-r33
reac257=s257-r257


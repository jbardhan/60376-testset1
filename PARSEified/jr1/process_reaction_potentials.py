import numpy as np
import matplotlib
import matplotlib.pyplot as plt

r33=np.loadtxt('ref-33.txt')    
r257=np.loadtxt('ref-257.txt')
s257=np.loadtxt('solv-257.txt')
s33=np.loadtxt('solv-33.txt')
reac33=0.592*(s33-r33)
reac257=0.592*(s257-r257)

bem_4 = np.loadtxt('reactpot_4.txt')
bem_10 = np.loadtxt('reactpot_10.txt')

#%matplotlib tk

atomrange = np.arange(len(bem_4))
data = {'low-res APBS':reac33,
        'high-res APBS':reac257,
        'low-res BEM':bem_4,
        'high-res BEM':bem_10}

plt.plot(atomrange, data['low-res APBS'],'r--',
         atomrange, data['high-res APBS'],'b--',
         atomrange, data['low-res BEM'],'r*',
         atomrange, data['high-res BEM'],'b*')
plt.xlabel('Atom index')
plt.ylabel('Reaction potential (kcal/mol/e)')
plt.show()

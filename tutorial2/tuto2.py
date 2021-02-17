#beta is given to be 1. (in the differentiation step, beta gets cancelled)
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3])
y = np.array([1.2,1.9,3.2])

def parameters(x,y):
    A = x.sum()
    B = y.sum()
    C = (x*x).sum()
    D = (x*y).sum()
    E = len(x)
    
    w0 = (C*B - A*D)/(C*E - A*A)
    w1 = (B - (E*w0))/A
    return w1,w0 
#slp is slope and  intr is intercept
slp, intr = parameters(x,y)

abline_values = [slp * i + intr for i in x]
plt.scatter(x,y)
plt.plot(x, y)
plt.plot(x, abline_values, 'g')
plt.show()

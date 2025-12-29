# # **Question `13`**

#importing libraries 
import math as mth
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp

#defining the linear equation function
def l_sys(x,y,a,b,c,d,h=0,k=0,i=50):
    X=[x]
    Y=[y]
    for num in range(i):
        x0 = X[-1]
        y0 = Y[-1]
        x1 = a*x0 + b*y0 + h
        y1 = c*x0 + d*y0 + k
        X.append(x1)
        Y.append(y1)
    return X, Y

#defining table function using pandas
def table(X,Y,A='X', B='Y', r=0):
    return pd.DataFrame({"Time": range(len(X)), str(A):np.round(X, r), str(B):np.round(Y, r)})

# ## *Question `13(a)`*

#The ouput is a tuple, assigning the lists to new variables
pred, prey = l_sys(x=1200,y=1000,a=1.2,b=-0.1,c=0.1,d=1,i=20)

#representing data in tabular form
table_a = table(pred, prey, 'Predator', 'Prey')
table_a

#Plotting linear systems (using original lists because table values has ben approximated)
plt.plot(table_a["Time"], pred, label='Predator',)
plt.plot(table_a["Time"], prey, label='Prey')
plt.legend(loc = 'upper left')
plt.title("PREDATOR - PREY GRAPH")
plt.xlabel('Time')
plt.ylabel('Population')

# ***Analysis***
# 
# > As time progresses, the predator and prey populations at an increasing rate, with the predator showing a faster rate than prey.

# ## *Question `13(b)`*

#assigning the lists to new variables
P, Q = l_sys(x=5000, y=2000, a=0.7, b=-0.05, c=-0.05, d=0.8)

#table
table_b = table(P, Q, 'P', 'Q', 4)
table_b

#graph
plt.plot(table_b["Time"], P, label='Predator')
plt.plot(table_b["Time"], Q, label='Prey' ,linestyle=':')
plt.legend()
plt.title("COMPETITION GRAPH")
plt.xlabel('Time')
plt.ylabel('Y-axis')

# ***Analysis***
# 
# >Both species compete for the same resources. Over time, their populations decline and approach an equilibrium. The competition limits the growth of both species although species P dominated initially due to a higher initial value.

# ## *Question `13(c)i`*

P = [1000]
Q = [2000]

def PP_G(P, Q):
    for n in range(50):
        P.append(0.8 * P[n] - 0.3 * Q[n]+8000)
        Q.append(0.2 * P[n] + 0.9*Q[n]+2000)
        
PP_G(P, Q)

plt.plot(P,Q,marker='o')
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.scatter(2500,25000, s=120, color='red', label='Fixed Point A')
plt.legend()

# ***Analysis***
# 
# >The constant immigration (8000 and 2000) shifts the trajectories toward a steady-state point, shown by the red dot (*Point A* - $(2500,25000)$), rather than steadily increasing or decreasing over time. Populations stabilize as times moves.

# ## *Question `13(c)ii`*

price, demand = l_sys(x=15, y=50, a=1, b=0.4, c=-0.3, d=1, h=-20, k=5, i=50)
table(price, demand, "Price", "Demand")

plt.plot(price,demand, marker='o')
plt.xlabel('Price')
plt.ylabel('Demand')
plt.scatter(16.66666666666666667,50, s=120, color='red', label='Fixed Point B')
plt.legend()

# ***Analysis***
# 
# >The model illustrates the **Law of Demand** (As price increases, quantity demanded decreases, and vice versa). Over iterations, the system converges to an equilibrium price and demand.

# ## *Question `13(c)iii`*

# ***CASE 1***: *initial condition where when $P > Q$*

SP,SQ = l_sys(x=2000,y=1500,a=1,b=-0.2,c=-0.4,d=1,h=1500,k=2000,i=10)
plt.plot(SP,SQ)
plt.xlabel('Species P')
plt.ylabel('Species Q')

# ***CASE 2:*** *initial condition where when $P = Q$*

SP_1,SQ_1 = l_sys(x=2000,y=2000,a=1,b=-0.2,c=-0.4,d=1,h=1500,k=2000,i=10)
plt.plot(SP_1,SQ_1)
plt.xlabel('Species P')
plt.ylabel('Species Q')

# ***CASE 3:*** *initial condition where when $P < Q$*

SP_2,SQ_2 = l_sys(x=1500,y=2000,a=1,b=-0.2,c=-0.4,d=1,h=1500,k=2000,i=10)
plt.plot(SP_2,SQ_2)
plt.xlabel('Species P')
plt.ylabel('Species Q')

# ***Analysis***
# 
# >Each initial condition leads to a different set of values and fixed points, but in each case, Species Q increases slightly but eventually falling as Species P thrives. Comparing the cases shows that, the lower the inital population of P relative to Q, Q does better initally, shows a positive correlation to Q, before falling and going extinct.

# ### *Question `13(d)`*

'''
Defining function EQ to find the eigenvalues
At fixed points, P[n+1] = P[n] = P and Q[n+1] = Q[n] = Q
'''
def EQ(a,b,c,d,h,k):
    P = sp.Symbol('P')
    Q = sp.Symbol('Q')
    E1 = sp.Eq(P,a*P + b*Q + h)
    E2 = sp.Eq(Q,c*P + d*Q + k)
    return(sp.solve((E1, E2), (P, Q)))

#Defining Function F to find fixed points
def F(a,b,c,d):
    k = a+d
    Dis = k**2 - 4*((a*d)-(b*c))
    x1 = np.absolute(k + Dis**0.5)/2
    x2 = np.absolute(k - Dis**0.5)/2
    return x1,x2

#Finding the fixed point for 3(ci)
EQ(0.8,-0.3,0.2,0.9,8000,2000)

#Finding the eigenvalues for 3(ci)
F(0.8,-0.3,0.2,0.9)

# Since the absolute value of the eigenvalues(~$0.88$) are equal and less than 1 (i.e. **$|0.88| < 1$**), its a sink.

#Finding the fixed point for 3(cii)
EQ(1,0.4,-0.3,1,-20,5)

#Finding the eigenvalues for 3(cii)
F(1,0.4,-0.3,1)

# Since the absolute value of the eigenvalues(~$1.06$) are equal and greater than 1 (i.e. **$|1.06| < 1$**), it's a source.

#Finding the fixed points for 3(ciii)
EQ(1,-0.2,-0.4,1,1500,2000)

#Finding the eigenvalues for 3(ciii)
F(1,-0.2,-0.4,1)

# The absolute values of the eigenvalues (~$1.28$ and ~$0.72$) are distinct with one greater and less than 1 respectively (i.e. $|1.28| > 1$ and $|0.71| < 1$) , hence it is a saddle.


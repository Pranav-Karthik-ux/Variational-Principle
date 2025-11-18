#computing the ground state energy level of quantum harmonic oscillator is variational principle 
from sympy import symbols, diff,  exp, integrate,oo,cos,sin,sqrt , lambdify, simplify
import numpy as np
import matplotlib.pyplot as plt
x,a=symbols('x a')

def kinetic(f,a,b):
    l=-h**2*diff(diff(f,x),x)/(2*m)
    T=integrate(f*l,(x,a,b))
    return T

def potential(f,p,a,b):
    v=integrate(f*p*f,(x,a,b))
    return v
h=1
m=1
w=1
f=exp(-a*x**2)
p=0.5*(m*x**2)*w**2
H=kinetic(f,-oo,oo)+potential(f,p,-oo,oo)
M=simplify(H/integrate(f*f,(x,-oo,oo)))
t=np.linspace(0.1,np.pi/2,30)
y=np.zeros(len(t))
analytic=0.5
for i in range(len(t)):
    y[i]=M.subs(a,t[i])
plt.plot(t,y,'-ok')
plt.errorbar(t, y)
plt.xlabel('varying parameter a')
plt.ylabel('value of energy computed')
plt.grid()
plt.title('Ground State Energy Level of Harmonic Oscillator')
plt.show()

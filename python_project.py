#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
import matplotlib.pyplot as pt


# In[2]:


#Laplace transform
#It transforms a function of a real variable t (often time) to a function of a complex variable s (complex frequency).
#the Laplace transform is a useful tool for dealing with linear systems described by ODEs. 
#the Laplace transform is defined for a larger class of functions than the related Fourier transform.


# In[3]:


#Basic and standard laplase can be found by integrating the function with exp(-st) from 0 to infinity with repect to t
t,s,n,a,b=symbols('t s n a b')
f=[1,t,t**n,exp(a*t),exp(-a*t),sin(a*t),cos(a*t),sinh(a*t),cosh(a*t)]


# In[4]:


integrate(f[0]*exp(-s*t),(t,0,oo))


# In[5]:


integrate(f[1]*exp(-s*t),(t,0,oo))


# In[6]:


integrate(f[2]*exp(-s*t),(t,0,oo))


# In[7]:


integrate(f[3]*exp(-s*t),(t,0,oo))


# In[8]:


integrate(f[4]*exp(-s*t),(t,0,oo))


# In[9]:


integrate(f[5]*exp(-s*t),(t,0,oo))


# In[10]:


integrate(f[6]*exp(-s*t),(t,0,oo))


# In[11]:


integrate(f[7]*exp(-s*t),(t,0,oo))


# In[12]:


integrate(f[8]*exp(-s*t),(t,0,oo))


# In[13]:


#first shifting property is to simply equations with exp(at)
#convert s----->(s-a)


# In[14]:


f=exp(a*t)*sin(b*t)
#find laplace of sin(b*t)
f1=sin(b*t)
laplace=integrate(f1*exp(-s*t),(t,0,oo))
#s---->s-a
laplace.subs(s,s-a)


# In[15]:


import numpy as np
from sympy.integrals import laplace_transform
from sympy.abc import t,s,a,b


# In[16]:


f=cos(t)
listu=[]
for i in np.arange(0,8*np.pi,0.2):
    listu.append(f.subs(t,i))
pt.plot(np.arange(0,8*np.pi,0.2),listu,label="f(t) graph")
g=laplace_transform(f,t,s)
g=g[0]
listy=[]#g(s) values
for i in np.arange(0,8*np.pi,0.2):
    listy.append(g.subs(s,i))
pt.plot(np.arange(0,8*np.pi,0.2),listy,label="f(s) graph")
pt.legend()


# In[17]:


f=exp(a*t)*sin(b*t)
#can solve this easily by first shifting property
#take f1
f1=sin(b*t)
g1=laplace_transform(f1,t,s)
g1=g1[0]
g2=g1.subs(s,s-a)
g=laplace_transform(f,t,s)
g=g[0]
if g.equals(g2):
    print('true')
    print("laplace transform of exp(a*t)*sin(b*t) is",g)
    print("laplace transform of sin(b*t) and then substituting s with s-a is",g2)

else:
    print('false')


# In[38]:


listy=[]
listu=[]
listi=[]
#let a=1 b=2
g=g.subs([(a,1),(b,2)])
g1=g1.subs([(a,1),(b,2)])
g2=g2.subs([(a,1),(b,2)])

for i in np.arange(0,8*np.pi,0.2):
    listy.append(g1.subs(s,i))
for i in np.arange(0,8*np.pi,0.2):
    listu.append(g2.subs(s,i))
for i in np.arange(0,8*np.pi,0.2):
    listi.append(g.subs(s,i))
fig, (ax1, ax2,ax3) = pt.subplots(1,3)
fig.suptitle('First shit visuallisation')
ax1.plot(np.arange(0,8*np.pi,0.2),listy)
ax2.plot(np.arange(0,8*np.pi,0.2),listu)
ax3.plot(np.arange(0,8*np.pi,0.2),listi)
ax1.set_title('Laplace before shifting')
ax2.set_title('Laplace after shifting')
ax3.set_title('Laplace done normally')
print('See after shifting both graphs become same')


# In[ ]:





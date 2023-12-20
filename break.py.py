#!/usr/bin/env python
# coding: utf-8

# In[1]:


#break
i=1
while i<10:
    if i==5:
        break
    print(i)
    i=i+1


# In[13]:


n=int(input())
d=2
flag=False
while d<n:
    if(n%d==0):
        flag=True
        break
    d=d+1
if flag:
    print("not prime")


# In[ ]:


n=int(input())
flag=False
for d in range(2,n,1):
    if(n%d==0):
        flag=True
        break
if flag:
    print("not prime")#10
else:                 #not prime
    print("prime")


# In[ ]:


n=int(input())
k=2
while k<=n:
    d=2
    flag=False
    while d<k:
        if(k%d==0):
            flag=True#10
            break     #2
        d=d+1         #3
    if (not (flag)):  #5
        print(k)      #7
    k=k+


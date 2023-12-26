#!/usr/bin/env python
# coding: utf-8

# In[6]:


i=1
while i<10:
    print(i)
    i=i+1
else:
    print("this will be printed")


# In[8]:


for i in range(1,10):
    print(i)
else:
    print("this will be printed")


# In[10]:


for i in range(1,10):
    if i==5:
        break
    print(i)
else:
    print("this will be printed")


# In[14]:


n=int(input())
for d in range(2,n,1):
    if n%d==0:
        break
else:
    print("prime number")


# In[19]:


n=int(input())
for i in range(2,n+1,2):
    if i%7==0:
        continue
    print(i)
    

# In[ ]:


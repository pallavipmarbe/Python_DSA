#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input())
for i in range(2,n+1,2):
    print(i)
    if i%7==0:
        continue
    print(i)


# In[5]:


n=int(input())
i=2
while i<=n:
    if i%7==0:
        i=i+2
        continue
    print(i)
    i=i+1


# In[7]:


i=3
if i<7:
    pass
print("hey")


# In[9]:


i=1
while i<=3:
    pass
    i=i+1
print("end")


# In[10]:


for i in range(1,4):
    pass
print("end")
#!/usr/bin/env python
# coding: utf-8

# insert and append elements in list

# In[2]:


li=[1,"pal",5,"bho"]
li


# In[3]:


li.append("ankush")
li


# In[7]:


li.insert(1,7)
li        #[1, 7, 'pal', 5, 'bho', 'ankush']


# In[9]:


li.extend([9,10,11])
li          #[1, 7, 'pal', 5, 'bho', 10, 'ankush', 9, 10, 11]


# removing elements from list

# In[11]:


li=[5,1,"pal",5,"bho"]
li


# In[13]:


li.remove(5)
li


# In[18]:


li.remove(6)
li


# In[29]:


li=[1,"pal",5,"bho"]
li


# In[31]:


li.pop()     #bho


# In[33]:


li.pop(181)


# In[1]:


len(li)


# In[3]:


li =['abcd', 'def']
li.insert(4,5)#exercise que
print(li)


# In[6]:


li = ['abcd',5,'def',5]
li.remove(5)#exercise que
print(li)


# In[8]:


li = [5,2,6,8]
li.pop(2)#exercise que
print(li)


# loops on list

# In[10]:


li=[1,2,"parikh",9,10,11,"ankush"]
li


# In[12]:


for i in range(len(li)):
    print(li[i])


# In[15]:


for i in range(2,len(li)):
    print(li[i])


# In[17]:


for ele in li:
    print(ele)


# In[19]:


for ele in li[2:]:
    print(ele)


# In[25]:


li = [1,2,3,4,5]
for i in li[1:4]: #exercise que
    print(i,end= " ")


# negative indexing

# In[27]:


li=[1,2,3,4,5]
li[0]


# In[29]:


li[-2]


# In[31]:


li[-8]


# sequencing in list

# In[33]:


li


# In[35]:


li[1:5:1]


# In[37]:


li[1:5:2]


# In[39]:


li


# In[41]:


li[1:]


# In[43]:


li[1::2]


# In[45]:


li[:3]


# In[47]:


li[-1]


# In[49]:


li[-3:-1]


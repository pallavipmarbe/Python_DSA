#!/usr/bin/env python
# coding: utf-8

# In[3]:


li=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
li[2][3]


# In[5]:


li[2][5]


# In[10]:


li[1][2]=20
li


# In[12]:


li = [[1,2,3],[4,5,6],[7,8,9]]
print(li[2][1])


# In[1]:


li = [[1,2,3],[4,5,6],[7,8,9]]
print(li[1][3])


# jagged list

# In[3]:


li=[[1,2,3,4],[8,7,6],[2,4],[9,8]]
li[0]


# In[5]:


li[2][3]


# list comprehension

# In[7]:


li=[1,2,3,4]
li_new=[]
for ele in li:
    li_new.append(ele**2)
print(li_new)


# In[9]:


li_new_c=[ele**2 for ele in li]
li_new_c


# In[11]:


li_even_square=[ele**2 for ele in li if ele%2==0]
li_even_square


# In[15]:


li_new_2=[ele for ele in li if ele%2==0 if ele%3==0]
print(li_new_2)                                        #[6]


# In[18]:


li_1=[1,2,3,4,5]
li_2=[2,4,6,7]
li_inter=[ele for ele in li_1 for ele2 in li_2 if ele==ele2]
print(li_inter)


# In[20]:


li=[1,2,3,4,5]
li_inter=[ele**2 if ele%2==0 else ele for ele in li]
li_inter


# In[22]:


s="parikh"
li=[ele for ele in s]
li


# In[24]:


li=["parikh","rohan","ankush"]
li_2d=[[s for s in ele]for ele in li]
li_2d


# In[29]:


li=[ele**2 for ele in range(5)]
print(li)


# In[31]:


li=[ele**2 for ele in range(10) if ele%3==0]
print(li)


# In[33]:


li=[[ij for j in range(4)]for i in range(3)]
print(li)


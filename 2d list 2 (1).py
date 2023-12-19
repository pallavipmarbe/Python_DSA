#!/usr/bin/env python
# coding: utf-8

# In[2]:


str=input().split()
n,m=int(str[0]),int(str[1])
li=[[int(j)for j in input().split()]for i in range(n)]


# In[4]:


li


# In[1]:


n=int(input())



# In[3]:


li


# In[9]:


str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]


# In[11]:


arr


# In[13]:


str=input().split()
n,m=int(str[0]),int(str[1])
b=str[2:]
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]


# In[15]:


arr


# In[17]:


n


# In[19]:


m


# In[22]:


li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n=3 
m=4
for i in range(n):
    for j in range(m):
        print(li[i][j],end=' ')
    print()


# In[24]:


li=[[1,2,3,4],[5,6],[9,10,11]]
n=3
for row in li:
    for ele in row:
        print(ele,end=' ')
    print()
    


# In[26]:


'ab'.join('abcd')


# In[28]:


'ab'.join(['1','2','3'])


# In[37]:


li=[[1,2,3,4],[5,6],[9,10,11]]                    #1 2 3 4
n=3                                               #5 6
for row in li:                                    #9 10 11
    output=' '.join([str(ele)for ele in row])
    print(output)


# In[41]:


def lar_col_sum(li):
    n=len(li)
    m=len(li[0])
    max_sum=-1
    max_col_index=-1
    for j in range(m):
        sum=0
        for ele in li:
            sum+=ele[j]
        if sum>max_sum:
            max_col_index=j
            max_sum=sum
    return max_sum,max_col_index
li=[[1,2,3,4],[8,7,6,5],[9,10,11,7]]
lar_sum,lar_col_index=lar_col_sum(li)
print(lar_sum,lar_col_index)

     


# In[ ]:





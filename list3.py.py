#!/usr/bin/env python
# coding: utf-8

# line seperate input

# In[2]:


n=int(input())


# In[4]:


n


# In[5]:


li=[]
for i in range(n):
    curr=int(input())
    li.append(curr)


# In[7]:


for ele in li:
    print(ele)


# space seperated input

# In[10]:


n=int(input())


# In[12]:


str=input()


# In[14]:


str


# In[16]:


li=[]
str_split=str.split(' ')
str_split


# In[18]:


str=input()


# In[20]:


str_split=str.split()
str_split


# In[26]:


li=[]
for ele in str_split:
    li.append(int(ele))


# In[34]:


li


# In[36]:


li=[int(x) for x in input().split()]


# In[37]:


for ele in li:
    print(ele)


# In[40]:


n=int(input())
li=[int (x)for x in input().split()]
for ele in li:
    print(ele)


# linear search

# In[2]:


n=int(input())


# In[6]:


li=[int(x) for x in input().split()]


# In[8]:


li


# In[10]:


ele=int(input())


# In[16]:


isFound=False
for i in range(len(li)):
    if li[i]==ele:
        print(i)
        isFound=True 
        break
if isFound is False:
    print(-1)


# In[18]:


ele=int(input())


# In[20]:


isFound=False
for i in range(len(li)):
    if li[i]==ele:
        print(i)
        isFound=True 
        break
if isFound is False:
    print(-1)


# linear search through functions

# In[1]:


def linear_search(li,ele):
    #li is the list and ele is the element to be searched
    for i in range(len(li)):
        if li[i]==ele:
            return i
    return -1
li=[1,2,3,6,5]
index=linear_search(li,9)
print(index)


# immutable

# In[3]:


x=3
a=3
print(3)


# In[5]:


id(a)


# In[7]:


id(x)


# In[8]:


a=4


# In[11]:


id(a)


# In[13]:


a


# In[14]:


x


# mutable

# In[1]:


li=[1,2,3,4]
li2=li
li2=[3,3,4]
li2[1]=4
print(li)


# passing variables through functions

# In[3]:


def increment(a):
    a=a+2
    return a
a=2
a=increment(a)
print(a)


# passing list through functions

# In[8]:


def increment(li):
    li[0]=li[0]+2
    return
li=[1,2,3,4]
increment(li)
print(li)


# In[10]:


def change(li):
    li[1] = li[1] + 2
li = [1,2,3,4,5]
change(li)#exercise que
print(li)


# In[12]:


def change(li):
    li[1] = li[1] + 2
    li = [3,3,3,4,5]
li = [1,2,3,4,5]
change(li)
print(li)


# In[ ]:





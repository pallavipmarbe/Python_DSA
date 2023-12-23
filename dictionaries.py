#!/usr/bin/env python
# coding: utf-8

# In[4]:


a={"the":1,"a":5,10000:"abc"}
type(a)


# In[5]:


print(a)


# In[6]:


len(a)


# In[7]:


b=a.copy()
b


# In[8]:


c=dict([("the",3),("a",10),(2,3)])
c


# In[13]:


d=dict.fromkeys(["abc",32,4],10)
d


# In[10]:


d=dict.fromkeys(["abc",32,4])
d


# In[14]:


a={1:2,3:4,"list":[1,23],"dct":{1:2}}
a


# In[15]:


a['list']


# In[16]:


a.get('list')


# In[17]:


print(a.get("li"))


# In[18]:


a.get('li',0)


# In[19]:


a.keys()


# In[20]:


a.items()


# In[21]:


for i in a:
    print(i)


# In[24]:


for i in a.values():
    print(i)


# In[25]:


for i in a:
    print(i,a[i])


# In[26]:


"list" in a 


# In[27]:


"li" in a 


# In[28]:


2 in a    #its a value not key


# In[29]:


a={1:2,3:4,"list":[1,23],"dct":{1:2}}
print(d[0])                  #dictionaries dont follow indexing and follow keys


# In[30]:


a={1:2,3:4,"list":[1,23],"dct":{1:2}}
print(d.get(0,5)) 


# print all words with frequency k

# In[31]:


s="this is a word string having many many word"
k=2
words=s.split()
words


# In[34]:


d={}
for w in words:
    if w in d:
        d[w]=d[w]+1
    else:
        d[w]=1
d


# In[35]:


d={}
for w in words:
        d[w]=d.get(w,0)+1
d


# In[36]:


for w in d:
    if d[w]==k:
        print(w)


# In[37]:


def printKFreqWords(s,k):
    words=s.split()
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)


# In[39]:


printKFreqWords(s,k)


# In[40]:


printKFreqWords(s,1)


# In[41]:


printKFreqWords(s,3)   #3 does not exist
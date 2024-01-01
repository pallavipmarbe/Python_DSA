#!/usr/bin/env python
# coding: utf-8

# In[9]:


#example
n=int(input())
r=int(input())
n_fact=1
for i in range(1,n+1):
    n_fact=n_fact*i
r_fact=1
for i in range(1,r+1):
    r_fact=r_fact*i
n_r_fact=1
for i in range(1,n-r+1):
    n_r_fact=n_r_fact*i
ans=n_fact//(r_fact*n_r_fact)
print(ans)


# In[24]:


def fact(a):
    n_fact=1
    for i in range(1,a+1):
        n_fact=n_fact*i
    return n_fact
    
n=int(input())
r=int(input())
n_fact=fact(n)
r_fact=fact(r)
n_r_fact=fact(n-r)
ans=n_fact//(r_fact*n_r_fact)
print(ans)


# In[30]:


def isPrime(n):
    for d in range(2,n):
        if (n % d==0):
            break
        else:
            return True         #isPrime(17)
        return False            #True


# In[31]:


isPrime(17)


# In[33]:


def primeFrom2ToN(n):
    for k in range(2,n+1):
        #check if k is prime and if k is prime print k
        is_k_prime=isPrime(k)
        if(is_k_prime):
            print(k)
    


# In[36]:


primeFrom2ToN(20)


# In[37]:


def ncr(n,r):
    n_fact=fact(n)
    r_fact=fact(r)
    n_r_fact=fact(n-r)
    ans=n_fact//(r_fact*n_r_fact)
    return ans


# In[39]:


ncr(5,2)


# In[41]:


def func(a):
    a = a + 10
    return a
a = 5
func(a)   #exercise que
print(a)


# In[42]:


def square(a):
    ans  = a*a
    return  ans
a = 4
a = square(a)  #exercise que
print(a)


# In[55]:


a1=10  #global variable
def f1():
    b1=12  #local variable
    print(b1)
print(a1)
f1()
#cant print local variable outside function print(b1)


# In[57]:


#you can access any global variabledefined before the function call
a2=10  #global variable
def f2():
    b2=12  #local variable
    print(b2)
    print(a2)
print(a2)
f2()
#can print global variable inside function print(a2)


# In[59]:


a = 14
def f():
    a=12
f()
print(a)    #exercise que


# In[60]:


a=14
def f():
    global a
    a=12   #exercise que
f()
print(a)


# In[61]:


a = 14
def f():
    a = 12
    return a   #exercise que
a = f()
print(a)


# In[65]:


def sum(a,b,c=0):
    print(c)
    return a+b+c
print(sum(2,3,4))
print(sum(3,4))


# In[67]:


#all non default arguments should be before argument with default values
def f(a=0, b=0, c=0):
    return a + b + c
result = f(1, 2)
print(result)


# In[69]:


def f1(a,b,c=2,d=0):
    return a+b+c+d
print(f1(2,3,4,5))
print(f1(2,3))
print(f1(2,3,5))


# In[2]:


def function(a,b,c=1):
    return a+b-c
value = function(10,12)   #exercise que
print(value)


# In[4]:


def function(a,b,c=1):
    return a+b-c
value = function(10,12,5)#exercise que
print(value)


# In[5]:


def function(a,b,c=1,d=5):
    return a+b+c+d
value = function(1,2,d=7)
print(value)
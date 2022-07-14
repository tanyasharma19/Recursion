#!/usr/bin/env python
# coding: utf-8

# Finding factorial of a number using recursion

# In[10]:


def findfactorial(n):
    assert n>=0 and int(n) == n, 'The number must be a positive integer only!'
    if (n<1):
        return 1
    else:
        return n*findfactorial(n-1)


# In[13]:


findfactorial(4)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[7]:


def generate_fibo(number=100):
    fib1, fib2 = 1, 1
    fibos = [0, fib1, fib2]
    for _ in range(number):
        fib1, fib2 = fib2, fib1 + fib2
        fibos.append(fib2)
    return fibos

def even_fibos(n):
    return [fibo for fibo in generate_fibo() if fibo % 2 == 0][:n]


# In[8]:


even_fibos(4)


# In[ ]:





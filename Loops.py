#!/usr/bin/env python
# coding: utf-8

# In[7]:


num_1 = int(input("Enter the number :"))
A = 0
B = 1
C = 0
while C <= num_1:
    A = B
    B = C
    C = A + B
    print(C)


# In[ ]:





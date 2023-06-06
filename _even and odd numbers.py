#!/usr/bin/env python
# coding: utf-8

# In[4]:


num_1 = [1,2,3,4,5,6,7,8,9]
even_count=0
odd_count=0
for number in num_1:
    if(number%2==0):
        even_count += 1
    elif(number % 2 !=0):
            odd_count += 1
print("Number of even numbers :",even_count)
print("Number of odd numbers :",odd_count)


# In[ ]:





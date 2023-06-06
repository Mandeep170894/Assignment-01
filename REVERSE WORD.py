#!/usr/bin/env python
# coding: utf-8

# In[4]:


word = input("Enter a word: ")

reversed_word = ""
index = len(word) - 1

while index >= 0:
    reversed_word += word[index]
    index -= 1

print("Reversed word:", reversed_word)


# In[ ]:





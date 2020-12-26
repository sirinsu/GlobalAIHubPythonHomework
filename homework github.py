#!/usr/bin/env python
# coding: utf-8

# In[4]:


value_list = []

#Getting 5 values from input

for i in range(5):
    val = input("Enter something please: ")
    value_list.append(val)
    
#Writing values and the type of these values to the screen.

i = 0
for value in value_list:
    i += 1 
    value_type = type(value)
    print(f"{i}.value: {value}")
    print(f"Type of {value}: {value_type}")
    print()
    
    
#input fonksiyonu her veriyi stringe dönüştürerek store ettiği için bütün value tipleri str gözükecek 


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[19]:


"""User Identification Program"""
user_information = [] #to store the input values for a single user
val = input("Please enter your first name: ")
user_information.append(val)
val = input("Please enter your last name: ")
user_information.append(val)
val = int(input("Please enter age: "))
user_information.append(val)
val = input("Please enter your date of birth (just year): ")
user_information.append(val)

print("---User Information---")
for info in user_information:
    print(info)

if age < 18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")


# In[ ]:





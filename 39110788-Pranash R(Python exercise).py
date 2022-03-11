#!/usr/bin/env python
# coding: utf-8

# Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7**4


# ** Split this string:**
# 
# s = "Hi there Sam!"
# *into a list. *

# In[2]:


s = "Hi there Sam!".split()
s


# ** Given the variables:**
# 
# planet = "Earth"
# diameter = 12742
# ** Use .format() to print the following string: **
# 
# The diameter of Earth is 12742 kilometers.

# In[3]:


planet = "Earth"
diameter = 12742
print("diameter of {} is {} kilometers".format(planet,diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[4]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[5]:


lst[3][1][2][0]


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[6]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[7]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[ ]:


Tuple is immutable
List is mutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domai

# In[9]:


def domainget(email):
    return email.split('@')[-1]
domainget('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[11]:


def finddog(st):
    return 'dog' in st.split()
finddog('Is there a dog here')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[12]:


def countdog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count
countdog('This dog runs faster than the other dog dude!')


# Final Problem
# 
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[13]:


def speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[14]:


speeding(100,4)


# In[15]:


speeding(70,3)


# In[ ]:





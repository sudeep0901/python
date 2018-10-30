#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
import subprocess
import sys
from pprint import pprint
print(sys.version)
sys.version_info


# In[39]:


# Running command and receiving output from python
# Ask the user for input
host = input("Enter a host to ping: ")

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['ping', '-a', host], stdout=subprocess.PIPE)

stdout, stderr = p1.communicate()
print(stdout, stderr)

names = ['sudeep', 'Mike', 'Dhanesh', 'Manasvi']


# In[34]:


# Running os commands using OS module in python
cmd = "echo %cd% >> currentdirectory.txt"
output = os.system(cmd)
print(output)

# Opening work application from python
cmd = "start winword"
os.system(cmd)


# In[35]:


for row in names:
    print(row)


# In[41]:


# % Formatting but not recommended due to error prone to list tupes and other collections
# , and large number of parameters also lead to less readablity
name = 'sudeep'
age = 34
"hello %s. You are %s. " % (name, age)


# In[44]:


# Use str.format - Instead
"Hello man {}, How are you doing? {}".format(name, "I am doing fine")


# In[45]:


"Hello man {1}, How are you doing? {0}".format(name, "I am doing fine")


# In[48]:
person = {'name': 'sudeep', 'greeting': 'i am fine'}
"Hello man {name}, How are you doing? {greeting}".format(**person)

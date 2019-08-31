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

#%%

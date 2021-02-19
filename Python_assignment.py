#!/usr/bin/env python
# coding: utf-8

# In[5]:


def print_5_rows():
    '''
    This function allows you to enter the name of csv file of your choice in your working directory.
    It reads the first five lines and prints them.
    The function takes no arguments.
    '''
    filename = str(input("Enter the name of the file:"))
    if not ".csv" in filename:
      filename += ".csv"
    import pandas as pd 
    data = pd.read_csv(filename, nrows = 5)
    print(data)
    
    


# In[ ]:


print_5_rows()


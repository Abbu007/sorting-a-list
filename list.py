#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[50]:


a=[3,2,8,4,1,7,6,5]
b=[]
c=range(0,8)
d=0
for i in c :
    for j in c:
        if a[i]<a[j]:
            d=a[i]
            a[i]=a[j]
            a[j]=d
print(a)


# In[72]:


a=[3,2,8,4,1,7,6,5]
b = []

while a:
    m = a[0]  
    for x in a: 
        if x < m:
            m = x
    b.append(m)
    a.remove(m)    

print(b)
        


# In[74]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[20]:


import qrcode
qr= qrcode.make("please login to my linkdein account")
data="https://www.linkedin.com/in/chethan-anand-d-k-a11b04228/"
qr=qrcode.make(data)
qr.save("linkedin.png")
qr.show()


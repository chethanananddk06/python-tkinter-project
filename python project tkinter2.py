#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
from tkinter import messagebox
import random
def rand_num():
    r = random.Random()
    n = r.randint(1,150)
    messagebox.showinfo("Random Number",str(n))

root = tk.Tk()
root.geometry("500x200")
button1 = tk.Button(root,text="generate random number",command=rand_num)
button1.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
root.mainloop()


# In[ ]:





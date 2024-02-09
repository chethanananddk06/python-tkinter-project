#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
import datetime
def show_time():
    dt = datetime.datetime.now()
    messagebox.showinfo("current date and time",dt)
    
root = tk.Tk()
root.geometry('800x300')
button1 = tk.Button(root,text = "show dateTime",command=show_time)
button1.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
root.mainloop()


# In[ ]:





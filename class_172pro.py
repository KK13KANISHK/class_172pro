# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:21:21 2023

@author: kanis
"""
from tkinter import *

root = Tk()
root.title("IDK")
root.geometry("100x100")

user_label = Label(root, test = "User_Name: ")
user_label.place(relx = 0.3, rely = 0.2, anchor = CENTER)

entry_name = Entry(root)
entry_name.place(relx = 0.6, rely = 0.2, anchor = CENTER)

user_email = Label(root, text = "Email_id: ")
user_email.place(relx = 0.3, rely = 0.3, anchor = CENTER)

entry_email = Entry(root)
entry_email.place(relx = 0.6, rely = 0.3, anchor = CENTER)

user = Label(root)

dictionary = {}

class Users: 
    
    def addUser(key, value): 
        global dictionary
        dictionary[key] = value
        lbl["text"] = dictionary

class GetUsers(Users): 
        
    def getUser(self):
        un = entry_name.get()
        ei = entry_email.get()
        Users.addUser(un, ei)

user = GetUsers()

btn = Button(root, text="Add User Details", command = user.getUser)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()

Darsh 
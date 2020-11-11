# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:14:37 2020

@author: User
"""

from tkinter import *
from tkinter import Menu,filedialog,scrolledtext

window=Tk()
window.title("Text Editor")
window.geometry("720x404")

def new_fn():
    scroll=scrolledtext.ScrolledText(window,width=30,height=15)
    scroll.grid(row=1,column=1)
    def save_fn():
        file=filedialog.asksaveasfile(filetypes=(("Text files",".txt"),))
        txt=scroll.get('1.0','end-1c')
        file_obj=open(file.name,"w")
        file_obj.write(txt)
        file_obj.close()
        print(txt)
        print(file.name)

    save_btn=Button(window,text="Save",command=save_fn)
    save_btn.grid(row=17,column=1)

def open_fn():
    file1=filedialog.askopenfilename(filetypes=(("Text files",".txt"),))
    print(file1)
    file1_obj=open(file1,"r")
    contents=file1_obj.read()
    scroll1=scrolledtext.ScrolledText(window,width=30,height=15)
    scroll1.grid(row=1,column=1)
    
    scroll1.insert(END,contents)
    
    print(contents)
    
    def save_in_open_fn():
        file2=filedialog.asksaveasfile(filetypes=(("Text files",".txt"),))
        txt2=scroll1.get('1.0','end-1c')
        file_obj2=open(file2.name,"w")
        file_obj2.write(txt2)
        file_obj2.close()
        print(txt2)
        print(file2.name)
    
    save_in_open_btn=Button(window,text="Save",command=save_in_open_fn)
    save_in_open_btn.grid(row=17,column=1)
    

menu=Menu(window)
new_item=Menu(menu)
menu.add_cascade(label="File",menu=new_item)
new_item.add_command(label="New",command=new_fn)
new_item.add_separator()
new_item.add_command(label="Open",command=open_fn)
window.config(menu=menu)
window.mainloop()
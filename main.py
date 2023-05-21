from tkinter import *
import webbrowser
import pyperclip
import random
import os
from tkinter import messagebox
# ////////////////start pro///////////////////
root =Tk()
# -------------------------------
root.title('phonebook gold')
# -------------------------------
root.geometry("600x300")
# -------------------------------
background ='#2c3e50'
root.config(bg=background)

#-----------fun add contact--------------
def add_contact ():
 contact_string=name_Entry.get()+ ':' + phone_Entry.get()
 listbox.insert(END,contact_string)
 name_Entry.delete(0,END)
 phone_Entry.delete(0,END)
 #-----------end--------------
#-----------fun delete contact--------------
def delete_contact():
   listbox.delete(ANCHOR)
#-----------end--------------
#-----------fun copy--------------
def copy_number():
   selected_contact=listbox.get(ANCHOR)
   number=selected_contact.split(': ')
   pyperclip.copy(number[1])


#-----------end--------------
#-----------fun exit--------------
def exit ():
    choice= messagebox.askquestion('Exit App', 'are you sure you want to close the  app ??')
    if choice == 'yes':
        root.destroy()
    else:
        return
# ----------end----------------




#===============================================================================================
# -------------con label------------------
name_label= Label(root,text='contact name:',bg=background,fg='white',font=('Calibri,12'),anchor='w',justify=LEFT)
name_label.place(relx=0.1,rely=0.1,anchor='c')
name_Entry= Entry(root,bg="white",fg=background,border=2)
name_Entry.place(relx=0.3,rely=0.1,anchor='c')
#-----------------end----------------------------
# -------------con number------------------
phone_label= Label(root,text=' contact number:',bg=background,fg='white',font=('Calibri,12'),anchor='w',justify=LEFT)
phone_label.place(relx=0.1,rely=0.2,anchor='c')
phone_Entry= Entry(root,bg="white",fg=background,border=2)
phone_Entry.place(relx=0.3,rely=0.2,anchor='c')
#-------------------end--------------------------
# -------------add con------------------
add_btn=Button(root,text='Add Contact' ,bg='#34495e' ,fg='white',borderwidth=3,padx=100, command=add_contact)
add_btn.place(relx=0.29,rely=0.35, anchor='c')

#-------------------end--------------------------

# -------------copy phone number------------------
copyphone=Button(root,text='copy phone number', bg=background, fg="white",border=3, padx=80,command=copy_number)
copyphone.place(relx=0.29,rely=0.55, anchor='c')
#------------------end--------------------------
# -------------delete contact btn------------------

deletephone = Button(root, text='delete contact ',bg=background,fg='white', borderwidth=3,padx=25,command=delete_contact)
deletephone.place(relx=0.15,rely=0.77,anchor='c')
#------------------end--------------------------

#------------------exit btn --------------------------
exit=Button(root,text='exit app',bg=background,fg='white', borderwidth=3,padx=47, command=exit)
exit.place(relx=0.42,rely=0.77,anchor='c')
#------------------end--------------------------
#------------------list box --------------------------
listbox=Listbox(root,width=40,height=15)

listbox.place(relx=0.75,rely=0.47,anchor='c')

#------------------end--------------------------
#==============================================================================================
root.mainloop()

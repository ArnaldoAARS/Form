

from tkinter import *




root=Tk()
root.title("Inner form")
root.config(width=110,height=110)
root.geometry("700x650")

myframe=Frame(root,bg="grey",bd="1")
myframe.config(width=250, height=400, background="red")
myframe.pack(expand="true")

button_frame=Frame(root,height=300)
button_frame.pack(padx=15, pady=15, expand="true")

def clean_entry(e):
    entryname.delete(0, END)
    entryname.config(fg="white")

def clean_lastname(e):
    entrylastname.delete(0, END)
    entrylastname.config(fg="red")

def clean_email(e):
    entry_email.delete(0, END)
    entry_email.config(fg="purple")

def clean_pass(e):
    entrypass.delete(0, END)    
    entrypass.config(fg="blue", show="*")
    






#_________________________________





name_text="First name"
lastname_text="Last name"
email_text="Email"
pass_text="Password"



entryname=Entry(myframe, fg="black", bg="#0E9FD0",width=60)
entryname.grid(row=0,column=0, sticky="nsew",columnspan=2)
entryname.insert(0,name_text)
entryname.bind("<FocusIn>",clean_entry)

entrylastname=Entry(myframe, fg="black", bg="#0E9FD0",width=60)
entrylastname.grid(row=1,column=0, sticky="nsew",columnspan=2)
entrylastname.delete(0, END)
entrylastname.insert(0, lastname_text)
entrylastname.bind("<FocusIn>", clean_lastname)

entry_email=Entry(myframe, fg="black", bg="#0E9FD0",width=60)
entry_email.grid(row=2,column=0, sticky="nsew",columnspan=2)
entry_email.delete(0, END)
entry_email.insert(0, email_text)
entry_email.bind("<FocusIn>", clean_email)


entrypass=Entry(myframe, fg="black", bg="#0E9FD0",width=60)
entrypass.grid(row=3,column=0, sticky="nsew",columnspan=2)
entrypass.delete(0, END)
entrypass.insert(0, pass_text)
entrypass.bind("<FocusIn>", clean_pass)





login_button=Button(button_frame,text="Log in")
login_button.grid(row=0,column=0, columnspan=2, sticky="we")

create_button=Button(button_frame,text="Create user")
create_button.grid(row=1, column=0, columnspan=2, sticky="we")


exit_button=Button(button_frame,text="Exit")
exit_button.grid(row=2, column=0, columnspan=2, sticky="we")

root.mainloop()
    
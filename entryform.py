from tkinter import *
import sqlite3
from tkinter import messagebox
from unicodedata import name

from soupsieve import select



def Createuser():
    new_user=Toplevel()

    conection=sqlite3.connect("New_user")
    mycursor=conection.cursor()
    conection.commit()
    conection.close

    def createtable():
        mycursor.execute("CREATE TABLE USERS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(25), LASTNAME VARCHAR(25), EMAIL VARCHAR(45) UNIQUE, PASSWORD VARCHAR(35))")

    def createuser():
        
            conection=sqlite3.connect("New_user")
            mycursor=conection.cursor()
            values=name.get(),lastname.get(),email.get(),password.get()
            mycursor.execute("INSERT INTO USERS VALUES(NULL,?,?,?,?)",(values)) 
            conection.commit()
            conection.close
            messagebox.showinfo("Success", "Acount successfully created")
            new_user.destroy()
        
        
        
    name=StringVar()
    lastname=StringVar()
    email=StringVar()
    password=StringVar()




    labelframe=Frame(new_user)
    labelframe.pack()

    header=Label(labelframe,font="Ariel",text="AARS",width=30, height=2,fg="black",bg="#C8DCE4")
    header.grid(row=0,column=0)


    myframe=Frame(new_user,bg="grey",bd="1")
    myframe.config(width=200, height=400, background="red")
    myframe.pack(expand="true")

    button_frame=Frame(new_user,height=300)
    button_frame.pack(padx=1, pady=1, expand="true")

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


    lable1=Label(myframe,text="Create a new client",height=3,bg="grey", fg="white",font=15)
    lable1.grid(row=0,column=0,sticky="ew",columnspan=2)


    entryname=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30),textvariable=name)
    entryname.grid(row=1,column=0, sticky="nsew",columnspan=2)
    entryname.insert(0,name_text)
    entryname.bind("<FocusIn>",clean_entry)

    entrylastname=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30),textvariable=lastname)
    entrylastname.grid(row=2,column=0, sticky="nsew",columnspan=2)
    entrylastname.delete(0, END)
    entrylastname.insert(0, lastname_text)
    entrylastname.bind("<FocusIn>", clean_lastname)

    entry_email=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30), textvariable=email)
    entry_email.grid(row=3,column=0, sticky="nsew",columnspan=2)
    entry_email.delete(0, END)
    entry_email.insert(0, email_text)
    entry_email.bind("<FocusIn>", clean_email)


    entrypass=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30),textvariable=password)
    entrypass.grid(row=4,column=0, sticky="nsew",columnspan=2)
    entrypass.delete(0, END)
    entrypass.insert(0, pass_text)
    entrypass.bind("<FocusIn>", clean_pass)



    create_button=Button(myframe,text="Create user",font=20,command=createuser)
    create_button.grid(row=5, column=0, columnspan=2, sticky="we")
    #create_button.bind("<FocusIn>,", opentab)

    exit_button=Button(button_frame,text="Exit",font=20)
    exit_button.grid(row=2, column=0, columnspan=2, sticky="we")




#______________MAIN ROOT_____________________________________________________________
root=Tk()
root.title("Inner form")
root.config(width=110,height=110)
root.geometry("540x450")
root.resizable(0,0)

labelframe=Frame(root)
labelframe.pack()

header=Label(labelframe,font="Ariel",text="Client Sign In",width=30, height=2,fg="black",bg="#C8DCE4")
header.grid(row=0,column=0)


myframe=Frame(root,bg="grey",bd="1")
myframe.config(width=200, height=400, background="red")
myframe.pack(expand="true")

button_frame=Frame(root,height=300)
button_frame.pack(padx=1, pady=1, expand="true")

'''clean leters in entry'''
def clean_entry(e):
    entryname.delete(0, END)
    entryname.config(fg="white")


def clean_pass(e):
    entrypass.delete(0, END)    
    entrypass.config(fg="blue", show="*")
    

'''Funtios of buttons'''

def close():
    root.destroy()


def login():
    
    
    conection=sqlite3.connect("new_user")
    mycursor=conection.cursor()
    data=names.get(),passwords.get()
    mycursor.execute("SELECT NAME, PASSWORD FROM USERS" )
    value=mycursor.fetchall()
    
    if data in value :
        messagebox.showinfo("good","exito")
    else:
        messagebox.showerror("nope","no yet")      
names=StringVar()
passwords=StringVar()

#_________________________________





name_text="First name"
pass_text="Password"


lable1=Label(myframe,text="To enter please insert your info below ",height=3,bg="grey", fg="white",font=15)
lable1.grid(row=0,column=0,sticky="ew",columnspan=2)


entryname=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30),textvariable=names)
entryname.grid(row=1,column=0, sticky="nsew",columnspan=2)
entryname.insert(0,name_text)
entryname.bind("<FocusIn>",clean_entry)




entrypass=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30),textvariable=passwords)
entrypass.grid(row=4,column=0, sticky="nsew",columnspan=2)
entrypass.delete(0, END)
entrypass.insert(0, pass_text)
entrypass.bind("<FocusIn>", clean_pass)


login_button=Button(myframe,text="Log in",font=20,command=login)
login_button.grid(row=5,column=0, columnspan=2, sticky="we")


create_label=Label(button_frame,font=("Ariel"),text="If you dont have an acount already, create one")
create_label.grid(row=0,column=0)

create_button=Button(button_frame,text="Create user",font=20,command=Createuser)
create_button.grid(row=1, column=0, columnspan=2, sticky="we")

exit_button=Button(button_frame,text="Exit",font=20,command=close)
exit_button.grid(row=2, column=0, columnspan=2, sticky="we")









root.mainloop()
    
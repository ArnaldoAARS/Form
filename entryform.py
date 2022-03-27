

from tkinter import *







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




#_________________________________





name_text="First name"
pass_text="Password"


lable1=Label(myframe,text="To enter please insert your info below ",height=3,bg="grey", fg="white",font=15)
lable1.grid(row=0,column=0,sticky="ew",columnspan=2)


entryname=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30))
entryname.grid(row=1,column=0, sticky="nsew",columnspan=2)
entryname.insert(0,name_text)
entryname.bind("<FocusIn>",clean_entry)




entrypass=Entry(myframe, fg="black", bg="#0E9FD0",width=40,font=(30))
entrypass.grid(row=4,column=0, sticky="nsew",columnspan=2)
entrypass.delete(0, END)
entrypass.insert(0, pass_text)
entrypass.bind("<FocusIn>", clean_pass)


login_button=Button(myframe,text="Log in",font=20)
login_button.grid(row=5,column=0, columnspan=2, sticky="we")


create_label=Label(button_frame,font=("Ariel"),text="If you dont have an acount already, create one")
create_label.grid(row=0,column=0)


create_button=Button(button_frame,text="Create user",font=20)
create_button.grid(row=1, column=0, columnspan=2, sticky="we")


exit_button=Button(button_frame,text="Exit",font=20,command=close)
exit_button.grid(row=2, column=0, columnspan=2, sticky="we")

root.mainloop()
    